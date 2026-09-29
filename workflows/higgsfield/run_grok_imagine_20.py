"""Chay Grok Imagine 2.0 image edit / text-to-image qua Higgsfield API (stdlib-only).

Doc model: work/higgsfield/models/grok-imagine-2.0.md
Quy uoc repo: work/ structure-only — script nay chi doc key tu env,
moi san pham ghi vao .local/work/higgsfield/<slug>/.

Env:
  HF_KEY="KEY_ID:KEY_SECRET"  (Python + cURL, theo doc chinh thuc)

Cach dung:
  python work/higgsfield/run_grok_imagine_20.py --params work/higgsfield/models/grok-imagine-2.0.params.example.json --outdir .local/work/higgsfield/2026-09-28-grok-k7
  python work/higgsfield/run_grok_imagine_20.py --params <params.json> --outdir <dir> --no-download
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error

ENDPOINT = "https://api.higgsfield.ai/xai/grok-imagine-image-2.0"
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


def _load_params(path):
    with open(path, encoding="utf-8") as f:
        full = json.load(f)
    api_keys = ("prompt", "quality", "image_urls", "resolution", "aspect_ratio")
    payload = {k: full[k] for k in api_keys if k in full and full[k] is not None}
    if not payload.get("prompt"):
        raise SystemExit("params.json thieu 'prompt' (bat buoc).")
    for u in payload.get("image_urls") or []:
        if not isinstance(u, str) or not u.startswith("https://"):
            raise SystemExit("image_urls phai la URL https public (upload truoc qua /files/generate-upload-url). Gap: %r" % (u,))
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
    ap = argparse.ArgumentParser(description="Chay Grok Imagine 2.0 (Higgsfield).")
    ap.add_argument("--params", required=True, help="Duong dan params.json")
    ap.add_argument("--outdir", required=True, help="Thu muc .local/work/higgsfield/<slug>/")
    ap.add_argument("--no-download", action="store_true", help="Chi poll, khong tai anh")
    ap.add_argument("--poll-interval", type=int, default=5)
    ap.add_argument("--poll-timeout", type=int, default=600)
    args = ap.parse_args()

    headers = _auth_headers()
    payload, meta = _load_params(args.params)
    os.makedirs(args.outdir, exist_ok=True)
    outdir = os.path.abspath(args.outdir)

    with open(os.path.join(outdir, "input.md"), "w", encoding="utf-8") as f:
        f.write("# input — Grok Imagine 2.0\n\n- Model: xai/grok-imagine-image-2.0\n"
                "- Params: params.json (copy)\n- Prompt source: %s\n- Keyframe: %s\n- Refs: %s\n\n## Prompt (EN)\n\n%s\n"
                % (meta.get("prompt_source", "?"), meta.get("keyframe", "?"),
                   meta.get("ref_roles", "?"), payload["prompt"]))
    with open(os.path.join(outdir, "params.json"), "w", encoding="utf-8") as f:
        json.dump({"model": "xai/grok-imagine-image-2.0", "endpoint": ENDPOINT,
                   **payload, **{k: v for k, v in meta.items() if k != "endpoint"}},
                  f, ensure_ascii=False, indent=2)

    print("POST %s" % ENDPOINT)
    submit = _post_json(ENDPOINT, payload, headers)
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

    images = result.get("images") or []
    print("completed. images=%d" % len(images))
    if images and not args.no_download:
        os.makedirs(os.path.join(outdir, "output"), exist_ok=True)
        for i, img in enumerate(images):
            url = (img or {}).get("url") or ""
            if not url:
                continue
            dest = os.path.join(outdir, "output", "grok-20-%d.jpg" % (i + 1))
            _download(url, dest, {"User-Agent": "curl/8.0"}, timeout=300)
            print("da tai: %s" % dest)
    print("Duyet anh trong output/, chon keyframe roi them 1 dong vao work/higgsfield/INDEX.md (thu cong).")


if __name__ == "__main__":
    main()
