"""Upload 1 file len storage tam Higgsfield, tra ve public_url.

Doc: https://docs.higgsfield.ai/docs/concepts/file-uploads.md
Quy uoc repo: file local -> presigned upload -> public_url lam image_url/video_url.
KHONG gui key vao presigned storage URL.

Cach dung:
  python work/higgsfield/upload_asset.py --file .local/work/higgsfield/assets/tui-ca-duc.png --content-type image/png
  -> in ra public_url (copy vao params.json image_urls)
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

UA = {"Accept": "application/json", "User-Agent": "curl/8.0"}


def _key():
    key = os.environ.get("HF_KEY", "").strip()
    if not key:
        print("Thieu HF_KEY.", file=sys.stderr)
        raise SystemExit(2)
    return key


def main():
    ap = argparse.ArgumentParser(description="Upload asset len Higgsfield, lay public_url.")
    ap.add_argument("--file", required=True)
    ap.add_argument("--content-type", required=True,
                    help="vd image/jpeg, image/png, image/webp, video/mp4 (phai khop file that)")
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        raise SystemExit("Khong thay file: %s" % args.file)
    headers = dict(UA)
    headers["Authorization"] = "Key " + _key()
    headers["Content-Type"] = "application/json"

    body = json.dumps({"content_type": args.content_type}).encode("utf-8")
    req = urllib.request.Request("https://api.higgsfield.ai/files/generate-upload-url",
                                 data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            info = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise SystemExit("HTTP %s: %s" % (e.code, e.read().decode("utf-8", "replace")))

    upload_url = info.get("upload_url") or ""
    public_url = info.get("public_url") or ""
    up_headers = info.get("upload_headers") or {}
    if not upload_url or not public_url:
        raise SystemExit("Thieu upload_url/public_url: %s" % json.dumps(info)[:300])

    with open(args.file, "rb") as f:
        data = f.read()
    put_headers = {"Content-Type": args.content_type, "User-Agent": "curl/8.0"}
    for k, v in up_headers.items():
        if isinstance(v, str):
            put_headers[k] = v
    put = urllib.request.Request(upload_url, data=data, headers=put_headers, method="PUT")
    try:
        with urllib.request.urlopen(put, timeout=300) as resp:
            resp.read()
    except urllib.error.HTTPError as e:
        raise SystemExit("Upload HTTP %s: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))

    print(public_url)


if __name__ == "__main__":
    main()
