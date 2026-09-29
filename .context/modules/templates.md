# Module: templates

> Quy tắc đúc template từ digest. Template chưa test → `drafts/`.

## Layout

```
templates/
  Index.md              ← index duy nhất (SoT)
  images/<slug>.md      ← template ảnh đã test
  videos/<slug>.md      ← template video đã test
  drafts/<slug>.md      ← template nháp (chưa fill thử)
```

## Schema template

```markdown
# Template: <tên>

- Dùng cho: <ảnh / video — trường hợp nào>
- Nguồn pattern: `<path tới 1+ digest>` (vd `../../research/images/digests/<slug>.md`)
- Biến (EN `UPPER_SNAKE`): `[SUBJECT]`, `[STYLE]`, `[CAMERA]`, ...

## Prompt mẫu (tiếng Anh, fill sẵn 1 ví dụ từ digest thật)

## Prompt kết quả khi gen (tiếng Anh — bắt buộc, không dịch sang Việt)

## Cách fill biến (tiếng Việt, mỗi biến 1 dòng + ví dụ)
## Biến thể (tối đa 3, vẫn tiếng Anh)
```

## Quy tắc merge

1. Viết nháp vào `drafts/`.
2. Fill thử với ≥1 digest thật (dán kết quả fill vào PR/chat khi duyệt).
3. Pass → move sang `images/` hoặc `videos/` + thêm 1 dòng vào `Index.md`.
4. `Index.md` mỗi dòng: `| template | dùng cho | nguồn digest | biến |`.
