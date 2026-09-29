---
name: make-template
description: Forge a reusable prompt template from digests, test-fill it, and index it in templates Index.md. Use when creating a template, duc cong thuc, or merging from drafts.
metadata:
  version: "1.0.0"
  updated: "2026-09-29"
---

# Make Template

Đúc template tái dùng từ digest. Template chưa test → `drafts/`, đạt mới merge.

## Quy tắc

- Nháp: `templates/drafts/<slug>.md`. Merge khi fill được từ ≥1 digest thật → `templates/images/` hoặc `templates/videos/` + 1 dòng `templates/Index.md`.
- Biến template đặt tên EN `UPPER_SNAKE` (`[SUBJECT]`, `[STYLE]`, `[CAMERA]`...).
- Prompt mẫu và mọi prompt kết quả khi gen đều xuất tiếng Anh. Hướng dẫn fill + `Index.md` viết tiếng Việt.
- Schema: dùng cho (ảnh/video, trường hợp nào), nguồn pattern (path 1+ digest), prompt mẫu EN (fill sẵn 1 ví dụ từ digest thật), cách fill biến (VI), tối đa 3 biến thể EN.
- `Index.md` mỗi dòng: `| template | dùng cho | nguồn digest | biến |`.

## Các bước

1. Đọc 1+ digest nguồn (tra qua `mapping.md`, không glob mò).
2. Viết nháp vào `templates/drafts/` theo schema `.context/modules/templates.md`.
3. Fill thử với ≥1 digest thật, dán kết quả fill khi duyệt.
4. Pass → move sang `images/`/`videos/` + thêm 1 dòng `Index.md`. Báo đường dẫn template + dòng index.
