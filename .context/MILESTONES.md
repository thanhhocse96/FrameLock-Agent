# MILESTONES — AI-GAN

Quy trình mỗi milestone: scaffold → user duyệt schema → thêm data thật → tick, commit, sang mốc kế.

## Quy ước đánh số

| Giai đoạn | Cách đánh số | Ghi chú |
|-----------|--------------|---------|
| Bootstrap | **M1, M2…** (tuần tự) | Working memory agent; không phải semver |

---

## M1 — Bootstrap context system ⬅ CURRENT

Scaffold hệ governance + thư mục rỗng đúng pipeline, chưa cần data thật.
Compact image-only từ 2026-10-09 (D-010): chỉ giữ nhánh ảnh, xóa video/API.

- [x] `AGENTS.md` (§0–§5: startup, invariants, routing, self-check)
- [x] `.context/` (README, GLOBAL, MILESTONES, TENSIONS_OPEN/ACTIVE, PITFALLS, modules/*)
- [x] `research/images/` (`raws/`, `digests/`, `mapping.md` seed + schema)
- [x] `templates/` (`images/`, `drafts/`, `Index.md`)
- [x] `workflows/` research-only (`add-raw.md`, `digest.md`, `template.md`, `INDEX.md`)
- [x] `docs/README.md` + `README.md` + `.gitignore` (`.local/`)
- [ ] User duyệt M1 (schema digest/mapping/template OK) → sang M2

## M2 — Seed 1 pipeline thật (dự kiến)

- [ ] 1 raw ảnh thật (`research/images/raws/`) có nguồn + URL + ngày
- [ ] 1 digest ảnh link về raw + 1 dòng `mapping.md`
- [ ] 1 template fill thử từ digest + `Index.md` trỏ tới
- [ ] User acceptance: tìm lại được digest qua mapping, dùng được template

## M3 — Mở rộng + quy ước từ vựng (backlog)

- [ ] ≥5 digest ảnh, mapping có từ khóa kỹ thuật/chủ đề/model ổn định
- [ ] Taxonomy từ khóa chốt vào `TENSIONS_ACTIVE.md`

---

## HISTORY

| Ngày | Milestone | Ghi chú |
|------|-----------|---------|
| 2026-09-28 | M1 | Scaffold Phase 0 theo duyệt user (raw = text prompt) |
