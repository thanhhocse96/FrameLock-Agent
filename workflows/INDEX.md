# INDEX — workflows (source of truth + version tracker)

> Mỗi workflow/command đổi nội dung → bump version + 1 dòng changelog ở đây.
> Mirror sang `.opencode/commands/` + `.claude/commands/` bằng `scripts/sync-agents.py`.

## Quy ước version (semver)

- **MAJOR**: đổi layout (thêm/bỏ platform dir, đổi pipeline).
- **MINOR**: đổi nội dung skill/command (bước mới, schema mới, move script).
- **PATCH**: sửa doc/path, chính tả.

## Workflows

| Workflow (`workflows/`) | Platform | Skill (`skills/`) | Version | Updated | Changelog |
|---|---|---|---|---|---|
| `add-raw.md` | — (research) | `add-raw` | 1.0.0 | 2026-09-29 | Khởi tạo |
| `digest.md` | — (research) | `make-digest` | 1.0.0 | 2026-09-29 | Khởi tạo |
| `template.md` | — (research) | `make-template` | 1.0.0 | 2026-09-29 | Khởi tạo |
| `hf-run.md` | `higgsfield/` | `higgsfield-run` | 1.1.0 | 2026-09-29 | 1.1.0 — script move `work/higgsfield/*.py` → `workflows/higgsfield/` + chốt chạy trên WSL |

## Platform dirs

| Dir | Scripts | Version |
|-----|---------|---------|
| `workflows/higgsfield/` | `run_minimax_h3.py`, `run_soul_v2.py`, `run_grok_imagine_20.py`, `run_marketing_studio_image.py`, `upload_asset.py` | 1.1.0 |

Provider mới → tạo `workflows/<platform>/` + `README.md` (index script + version) + skill/section tương ứng, hỏi user trước (ASK — tách/gộp thư mục).
