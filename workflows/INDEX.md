# INDEX — workflows research (source of truth + version tracker)

> Mỗi workflow/command đổi nội dung → bump version + 1 dòng changelog ở đây.
> Mirror sang `.opencode/commands/` + `.claude/commands/` bằng `scripts/sync-agents.py`.

## Quy ước version (semver)

- **MAJOR**: đổi layout (thêm/bỏ workflow, đổi pipeline).
- **MINOR**: đổi nội dung skill/command (bước mới, schema mới).
- **PATCH**: sửa doc/path, chính tả.

## Workflows

| Workflow (`workflows/`) | Skill (`skills/`) | Version | Updated | Changelog |
|---|---|---|---|---|
| `add-raw.md` | `add-raw` | 1.0.0 | 2026-09-29 | Khởi tạo |
| `digest.md` | `make-digest` | 1.0.0 | 2026-09-29 | Khởi tạo |
| `template.md` | `make-template` | 1.0.0 | 2026-09-29 | Khởi tạo |

> Compact image-only D-010 (2026-10-09): xóa `hf-run.md`, `workflows/higgsfield/`, `workflows/openrouter/` + mọi script/API/MCP liên quan.

## Skill phân tích video

Phạm vi research video được user mở lại ngày 2026-10-12; không khôi phục runner/API vào workflows.

| Skill canonical | Version | Updated | Changelog |
|---|---|---|---|
| `skills/video-delta-analysis/SKILL.md` | 1.2.0 | 2026-10-12 | Trigger first/last-frame; ghi case/run phục vụ Business; layout cho case mới theo AGENTS §7, giữ nguyên legacy; mirror theo `scripts/sync-agents.py` |
| `skills/write-video-script/SKILL.md` | 0.1.0 | 2026-10-28 | Skill mới bản nháp: kịch bản kể chuyện/B2B, bàn giao beat và kiểm tra claim; căn cứ digest Foyege, chỉ kiểm tra văn bản |
| `skills/direct-ai-performance/SKILL.md` | 0.1.0 | 2026-10-28 | Skill mới bản nháp: ý đồ → hành vi/prompt, đánh giá diễn xuất riêng artifact, kiểm soát chi phí; chưa kiểm chứng production |
