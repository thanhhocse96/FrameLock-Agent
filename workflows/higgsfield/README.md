# workflows/higgsfield — script chạy API Higgsfield (platform dir)

> Version: 1.1.0 (2026-09-29) · Skill điều phối: `skills/higgsfield-run/SKILL.md`
> Changelog: 1.1.0 — move từ `work/higgsfield/*.py` sang đây (nội dung script không đổi).

## ⚠️ Chạy trên WSL (Debian), không chạy Python Windows

Máy này không có Python Windows thật (chỉ stub). Mọi script chạy qua WSL từ repo root:

```powershell
wsl -d Debian -- python3 workflows/higgsfield/run_minimax_h3.py --params <params.json> --outdir .local/work/higgsfield/<YYYY-MM-DD-slug>
```

Venv/key/toolchain chi tiết (machine-local): `.local/ENVIRONMENT.md`.
Key chỉ từ env (`HF_KEY`, `HF_CREDENTIALS`) — cấm paste key vào repo.

## Scripts

| Script | Model / việc | Version |
|--------|--------------|---------|
| `run_minimax_h3.py` | MiniMax H3 text/image-to-video (2K, 5–15s) | 1.1.0 |
| `run_soul_v2.py` | Soul 2 text-to-image (keyframes) | 1.1.0 |
| `run_grok_imagine_20.py` | Grok Imagine 2.0 edit + text-to-image (giữ ref) | 1.1.0 |
| `run_marketing_studio_image.py` | Marketing Studio image (campaign edit, giữ ref) | 1.1.0 |
| `upload_asset.py` | Upload asset lấy URL ref | 1.1.0 |

Doc model + params mẫu ở `work/higgsfield/models/`. Index experiment ở `work/higgsfield/INDEX.md`.
Sản phẩm mỗi lần chạy → `.local/work/higgsfield/<slug>/` (gitignored).
