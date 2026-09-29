# MILESTONES — AI-GAN

Quy trình mỗi milestone: scaffold → user duyệt schema → thêm data thật → tick, commit, sang mốc kế.

## Quy ước đánh số

| Giai đoạn | Cách đánh số | Ghi chú |
|-----------|--------------|---------|
| Bootstrap | **M1, M2…** (tuần tự) | Working memory agent; không phải semver |

---

## M1 — Bootstrap context system ⬅ CURRENT

Scaffold hệ governance + thư mục rỗng đúng pipeline, chưa cần data thật.

- [x] `AGENTS.md` (§0–§5: startup, invariants, routing, self-check)
- [x] `.context/` (README, GLOBAL, MILESTONES, TENSIONS_OPEN/ACTIVE, PITFALLS, modules/*)
- [x] `research/images/` + `research/videos/` (`raws/`, `digests/`, `mapping.md` seed + schema)
- [x] `templates/` (`images/`, `videos/`, `drafts/`, `Index.md`)
- [x] `work/` structure-only (`README.md`, `higgsfield/README.md` + `INDEX.md`; sản phẩm ở `.local/work/`)
- [x] `docs/README.md` + `README.md` + `.gitignore` (`.local/`)
- [ ] User duyệt M1 (schema digest/mapping/template OK) → sang M2

## M2 — Seed 1 pipeline thật (dự kiến)

- [ ] 1 raw ảnh thật (`research/images/raws/`) có nguồn + URL + ngày
- [ ] 1 digest ảnh link về raw + 1 dòng `mapping.md`
- [ ] 1 raw video + 1 digest video + 1 dòng `mapping.md`
- [ ] 1 template fill thử từ digest + `Index.md` trỏ tới
- [ ] 1 experiment higgsfield thử (sản phẩm ở `.local/work/higgsfield/<slug>/` + 1 dòng `workflows/higgsfield/INDEX.md`)
- [ ] User acceptance: tìm lại được digest qua mapping, dùng được template

## M3 — Mở rộng + quy ước từ vựng (backlog)

- [ ] ≥5 digest mỗi bên (ảnh/video), mapping có từ khóa kỹ thuật/chủ đề/model ổn định
- [ ] Taxonomy từ khóa chốt vào `TENSIONS_ACTIVE.md`

---

## HISTORY

| Ngày | Milestone | Ghi chú |
|------|-----------|---------|
| 2026-09-28 | M1 | Scaffold Phase 0 theo duyệt user (raw = text prompt) |
