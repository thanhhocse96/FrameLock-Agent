#!/usr/bin/env python3
"""Run Recraft V4.1 Utility text‑to‑image generation.

Uses the Higgsfield SDK (or raw cURL) to submit a prompt and poll until the
image is ready.  The script mirrors the structure of the other workflow runners
(run_minimax_h3.py, run_grok_imagine_20.py, …).

Typical use:

    HF_KEY="KEY_ID:KEY_SECRET" python run_recraft_utility.py \
        --prompt "A cinematic scene at sunset" \
        --aspect-ratio "9:16" \
        --output-format "webp"

The ``HF_KEY`` environment variable must contain the Higgsfield API key
``KEY_ID:KEY_SECRET`` (see ``.local/work/higgsfield/.env``).
"""

import os
import sys
import json
import time
import argparse
import requests

# ---------------------------------------------------------------------------
# Helper: load HF_KEY from the project .env (WSLENV passes it through)
# ---------------------------------------------------------------------------
def load_hf_key() -> str:
    env_key = os.getenv("HF_KEY")
    if not env_key:
        # fallback: read from .local/work/higgsfield/.env
        env_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "local", "work", "higgsfield", ".env"
        )
        if os.path.isfile(env_path):
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("HF_KEY="):
                        _, val = line.split("=", 1)
                        return val.strip()
    return env_key


# ---------------------------------------------------------------------------
# API endpoint
# ---------------------------------------------------------------------------
RECRaft_ENDPOINT = "https://api.higgsfield.ai/recraft/v4.1/utility/text-to-image"


def subscribe(prompt: str, aspect_ratio: str = "1:1", resolution: str = "1k",
              output_format: str = "jpg", colors: list | None = None) -> dict:
    """Submit the generation request and return the request ID + status URL."""
    hf_key = load_hf_key()
    headers = {
        "Authorization": f"Key {hf_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "prompt": prompt,
        "resolution": resolution,
        "aspect_ratio": aspect_ratio,
        "output_format": output_format,
    }
    if colors:
        payload["colors"] = colors

    resp = requests.post(RECRaft_ENDPOINT, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()        # contains request_id, status_url, etc.


def poll_until_done(status_url: str, request_id: str, max_wait: int = 300,
                    interval: int = 10) -> dict:
    """Poll the status endpoint until a terminal state is reached."""
    start = time.time()
    while True:
        elapsed = time.time() - start
        if elapsed > max_wait:
            raise TimeoutError(f"Request {request_id} did not complete within {max_wait}s")
        r = requests.get(status_url)
        r.raise_for_status()
        data = r.json()
        status = data.get("status")
        if status in ("completed", "failed", "canceled", "nsfw"):
            return data
        time.sleep(interval)


def main(argv: list | None = None) -> None:
    parser = argparse.ArgumentParser(description="Recraft V4.1 Utility text‑to‑image")
    parser.add_argument("--prompt", required=True, help="Text prompt for image generation")
    parser.add_argument("--aspect-ratio", default "1:1",
                        choices=["1:1", "2:1", "1:2", "3:2", "2:3", "4:3", "3:4",
                                 "5:4", "4:5", "6:10", "14:10", "10:14", "16:9", "9:16"])
    parser.add_argument("--resolution", default "1k", choices=["1k"])
    parser.add_argument("--output-format", default "jpg", choices=["jpg", "png", "webp"])
    parser.add_argument("--colors", nargs="*", default=None,
                        help="Optional list of RGB colors, each as three integers 0‑255, e.g. --colors 255 0 0 0 255 0")
    parser.add_argument("--max-wait", type=int, default=300, help="Maximum seconds to wait for completion")
    parser.add_argument("--poll-interval", type=int, default=10, help="Seconds between polls")
    args = parser.parse_args(argv)

    # Build colors list if provided
    colors = None
    if args.colors:
        if len(args.colors) % 3 != 0:
            print("Error: --colors expects groups of three integers (R G B).", file=sys.stderr)
            sys.exit(1)
        colors = [{"rgb": [int(c) for c in args.colors[i:i+3]]} for i in range(0, len(args.colors), 3)]

    # 1️⃣ Submit request
    result = subscribe(args.prompt, args.aspect_ratio, args.resolution,
                       args.output_format, colors)
    request_id = result.get("request_id")
    status_url = result.get("status_url")
    if not request_id or not status_url:
        print("Unexpected response from Recraft API:", result, file=sys.stderr)
        sys.exit(1)

    print(f"Submitted Recraft request {request_id} – now polling…")

    # 2️⃣ Poll until terminal
    final = poll_until_done(status_url, request_id, max_wait=args.max_wait,
                            interval=args.poll_interval)
    status = final.get("status")

    if status == "completed":
        images = final.get("images", [])
        if images:
            url = images[0].get("url")
            print("✅ Image ready!")
            print("URL:", url)
            # Optional: download and save locally
            out_dir = os.path.join(
                os.path.dirname(__file__), "..", "local", "work", "higgsfield",
                f"2026-09-30-recraft-{args.prompt[:20].replace(' ', '-')}"
            )
            os.makedirs(out_dir, exist_ok=True)
            # download the image
            img_data = requests.get(url).content
            out_path = os.path.join(out_dir, "output." + args.output_format)
            with open(out_path, "wb") as f:
                f.write(img_data)
            print(f"🖼️  Saved to {out_path}")
        else:
            print("✅ Request completed but no images returned.")
    elif status == "failed":
        error = final.get("error", "unknown error")
        print(f"❌ Request failed: {error}", file=sys.stderr)
        sys.exit(1)
    elif status == "canceled":
        print("⏳ Request was canceled.", file=sys.stderr)
        sys.exit(1)
    elif status == "nsfw":
        print("⚠️  Request flagged as NSFW.", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"❓ Unexpected status: {status}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()