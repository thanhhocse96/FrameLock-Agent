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
| `hf-run.md` | `higgsfield/` | `higgsfield-run` | 1.2.0 | 2026-09-29 | 1.2.0 — gộp `work/higgsfield/` (docs + `models/` + `INDEX.md`) vào `workflows/higgsfield/`, xóa `work/` |

## Platform dirs

| Dir | Nội dung | Version |
|-----|---------|---------|
| `workflows/higgsfield/` | `README.md` + `INDEX.md` + `models/` + 5 script `.py` | 1.2.2 |

## Quy ước chạy experiment (gộp từ `work/README.md`)

1. Thêm platform mới → tạo `workflows/<platform>/` với `README.md` + `INDEX.md`, hỏi user trước (ASK).
2. Mỗi lần chạy → 1 thư mục `.local/work/<provider>/<YYYY-MM-DD-slug>/` (`input.md` EN, `params.json`, `output/`, `result.md` VI, `run.log`), thêm 1 dòng vào `workflows/<platform>/INDEX.md`.
3. API key/token **không bao giờ** vào repo — chỉ đọc từ env hoặc `.local/` (xem `PITFALLS.md` #9–#12).
4. Output tốt → promote: copy prompt vào `research/*/raws/` (ghi nguồn là experiment) → digest → mapping → template.
5. Ngôn ngữ: `README.md`/`INDEX.md`/`result.md` tiếng Việt; prompt trong `input.md` tiếng Anh.

Provider mới → tạo `workflows/<platform>/` + `README.md` (index script + version) + skill/section tương ứng, hỏi user trước (ASK — tách/gộp thư mục).
