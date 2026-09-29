"""Chay MiniMax H3 text / image-to-video qua Higgsfield API (stdlib-only).

Doc model: work/higgsfield/models/minimax-h3.md
Quy uoc repo: work/ structure-only — script nay chi doc key tu env,
moi san pham ghi vao .local/work/higgsfield/<slug>/.
Khong audio (MiniMax H3 khong co param am thanh; SFX lam o khau dung).

Env:
  HF_KEY="KEY_ID:KEY_SECRET"  (Python + cURL, theo doc chinh thuc)

Cach dung:
  python work/higgsfield/run_minimax_h3.py --params work/higgsfield/models/minimax-h3.params.example.json --outdir .local/work/higgsfield/2026-09-28-minimax-h3-test
  python work/higgsfield/run_minimax_h3.py --params <params.json> --outdir <dir> --mode image-to-video
  python work/higgsfield/run_minimax_h3.py --params <params.json> --outdir <dir> --no-download
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error

TEXT_ENDPOINT = "https://api.higgsfield.ai/minimax/h3/text-to-video"
IMAGE_ENDPOINT = "https://api.higgsfield.ai/minimax/h3/image-to-video"
TERMINAL_OK = "completed"
TERMINAL_FAIL = ("failed",)
TERMINAL_OTHER = ("nsfw", "canceled")


def _auth_headers():
    key = os.environ.get("HF_KEY", "").strip()
    if not key:
        print("Thieu HF_KEY. Dat: $env:HF_KEY='KEY_ID:KEY_SECRET' (khong commit key).", file=sys.stderr)
        raise SystemExit(2)
    # UA dang curl: urllib mac dinh gui 'Python-urllib/x.y' de bi Cloudflare chan (403 error 1010).
    return {"Authorization": "Key " + key, "Content-Type": "application/json",
            "Accept": "application/json", "User-Agent": "curl/8.0"}


def _post_json(url, payload, headers, timeout=60):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        raise SystemExit("HTTP %s: %s" % (e.code, body))


def _get_json(url, headers, timeout=60):
    req = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _load_params(path, mode):
    with open(path, encoding="utf-8") as f:
        full = json.load(f)
    api_keys = ("prompt", "duration", "resolution", "aspect_ratio", "aigc_watermark")
    if mode == "image-to-video":
        api_keys = api_keys + ("image_url", "end_image_url")
    payload = {k: full[k] for k in api_keys if k in full}
    if not payload.get("prompt"):
        raise SystemExit("params.json thieu 'prompt' (bat buoc).")
    if mode == "image-to-video":
        if not (payload.get("image_url") or "").startswith("https://"):
            raise SystemExit("image-to-video bat buoc image_url https public (upload truoc).")
        if payload.get("end_image_url") and not payload["end_image_url"].startswith("https://"):
            raise SystemExit("end_image_url phai la URL https public.")
    meta = {k: v for k, v in full.items() if k not in api_keys}
    return payload, meta


def _download(url, dest, headers, timeout=300):
    req = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as resp, open(dest, "wb") as f:
        while True:
            chunk = resp.read(1024 * 256)
            if not chunk:
                break
            f.write(chunk)


def main():
    ap = argparse.ArgumentParser(description="Chay MiniMax H3 text-to-video (Higgsfield).")
    ap.add_argument("--params", required=True, help="Duong dan params.json")
    ap.add_argument("--outdir", required=True, help="Thu muc .local/work/higgsfield/<slug>/")
    ap.add_argument("--no-download", action="store_true", help="Chi poll, khong tai video")
    ap.add_argument("--mode", default="text-to-video", choices=("text-to-video", "image-to-video"))
    ap.add_argument("--poll-interval", type=int, default=5)
    ap.add_argument("--poll-timeout", type=int, default=600)
    args = ap.parse_args()
    endpoint = IMAGE_ENDPOINT if args.mode == "image-to-video" else TEXT_ENDPOINT
    model_id = "minimax/h3/image-to-video" if args.mode == "image-to-video" else "minimax/h3/text-to-video"

    headers = _auth_headers()
    payload, meta = _load_params(args.params, args.mode)
    os.makedirs(args.outdir, exist_ok=True)
    outdir = os.path.abspath(args.outdir)

    with open(os.path.join(outdir, "input.md"), "w", encoding="utf-8") as f:
        f.write("# input — MiniMax H3\n\n- Model: %s\n"
                "- Params: params.json (copy)\n- Prompt source: %s\n\n## Prompt (EN)\n\n%s\n"
                % (model_id, meta.get("prompt_source", "?"), payload["prompt"]))
    with open(os.path.join(outdir, "params.json"), "w", encoding="utf-8") as f:
        json.dump({"model": model_id, "endpoint": endpoint,
                   **payload, **{k: v for k, v in meta.items() if k != "endpoint"}},
                  f, ensure_ascii=False, indent=2)

    print("POST %s" % endpoint)
    submit = _post_json(endpoint, payload, headers)
    status = submit.get("status", "")
    request_id = submit.get("request_id", "?")
    status_url = submit.get("status_url", "")
    print("request_id=%s status=%s" % (request_id, status))
    with open(os.path.join(outdir, "run.log"), "w", encoding="utf-8") as f:
        f.write(json.dumps(submit, ensure_ascii=False, indent=2) + "\n")
    if not status_url:
        raise SystemExit("API khong tra status_url — xem run.log.")

    deadline = time.time() + args.poll_timeout
    result = submit
    while result.get("status") not in (TERMINAL_OK,) + TERMINAL_FAIL + TERMINAL_OTHER:
        if time.time() > deadline:
            raise SystemExit("Poll timeout — kiem tra status_url thu cong.")
        time.sleep(args.poll_interval)
        result = _get_json(status_url, headers)
        print("... status=%s" % result.get("status", "?"))
        with open(os.path.join(outdir, "run.log"), "a", encoding="utf-8") as f:
            f.write(json.dumps(result, ensure_ascii=False) + "\n")

    if result.get("status") != TERMINAL_OK:
        raise SystemExit("Ket thuc khong thanh cong: %s" % json.dumps(result, ensure_ascii=False))

    video_url = ((result.get("video") or {}).get("url")) or ""
    print("completed. video=%s" % video_url)
    if video_url and not args.no_download:
        os.makedirs(os.path.join(outdir, "output"), exist_ok=True)
        dest = os.path.join(outdir, "output", "minimax-h3.mp4")
        _download(video_url, dest, {"User-Agent": "curl/8.0"}, timeout=300)
        print("da tai: %s" % dest)
    print("Them 1 dong vao work/higgsfield/INDEX.md (thu cong).")


if __name__ == "__main__":
    main()
