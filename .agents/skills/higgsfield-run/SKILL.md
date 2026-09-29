---
name: higgsfield-run
description: Run a Higgsfield text or image-to-video experiment via the committed scripts, log to local work dir, and index one row in work INDEX.md. Use when running higgsfield, chay thu API, experiment video, or promoting output to research.
metadata:
  version: "1.1.0"
  updated: "2026-09-29"
---

# Higgsfield Run

Chạy thử API Higgsfield theo pipeline promote. Script là đường chính, MCP là đường phụ.

## ⚠️ Script chạy trên WSL (Debian)

Máy này không có Python Windows thật. Chạy từ repo root:

```
wsl -d Debian -- python3 workflows/higgsfield/<script>.py --params <params.json> --outdir .local/work/higgsfield/<YYYY-MM-DD-slug>
```

Venv/key/toolchain (machine-local): `.local/ENVIRONMENT.md`.

## Quy tắc (từ work/ + PITFALLS.md #9–#12)

- Script commit trong repo: `workflows/higgsfield/run_minimax_h3.py`, `run_soul_v2.py`, `run_grok_imagine_20.py`, `run_marketing_studio_image.py`, `upload_asset.py` + `work/higgsfield/models/*.params.example.json`. Key chỉ từ env (`HF_KEY`, `HF_CREDENTIALS`) hoặc `.local/work/higgsfield/.env` — cấm paste key vào repo.
- Sản phẩm mỗi lần chạy → `.local/work/higgsfield/<YYYY-MM-DD-slug>/` (`input.md` prompt EN, `params.json`, `output/`, `result.md` VI, `run.log`). Không commit media/key.
- `params.json` tối thiểu: model+version, prompt_source (template/digest đã fill), seed, size, duration_sec.
- Mỗi lần chạy thêm 1 dòng `work/higgsfield/INDEX.md`. Output tốt → promote: copy prompt EN vào `research/*/raws/` (ghi nguồn là experiment path) → skill `add-raw`/`make-digest` tiếp. Không trỏ digest trực tiếp vào `.local/`.
- Gen thường dùng script; MCP Higgsfield (`opencode.json` → `https://mcp.higgsfield.ai/mcp`, OAuth) chỉ khi cần `create_character`/Soul ID hoặc lục history.

## Các bước

1. Chọn template nguồn từ `templates/Index.md` (prompt EN) → fill biến.
2. Copy params mẫu, chạy script, ví dụ:
   `wsl -d Debian -- python3 workflows/higgsfield/run_minimax_h3.py --params <params.json> --outdir .local/work/higgsfield/<YYYY-MM-DD-slug>`
3. Viết `result.md` (VI): đạt/không đạt, so với digest nào, có promote không.
4. Thêm 1 dòng `INDEX.md`. Nếu promote, copy prompt vào `raws/` rồi báo để chạy digest.
