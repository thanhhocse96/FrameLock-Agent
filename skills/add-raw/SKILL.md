---
name: add-raw
description: Copy an influencer prompt verbatim into research images or videos raws with source URL and date. Use when adding a raw prompt, thu thap prompt, or starting the raw-to-digest pipeline.
---

# Add Raw

Thu thập prompt nguyên văn influencer vào kho `research/`. Raw là text, bất biến.

## Quy tắc (từ AGENTS.md + PITFALLS.md)

- `research/images/raws/<slug>.md` hoặc `research/videos/raws/<slug>.md` — chỉ `.md`/`.txt`, không media binary (media → `.local/`).
- Đầu file bắt buộc: nguồn influencer/kênh + URL + ngày thu thập (`YYYY-MM-DD`) + model (nếu raw nói rõ, không đoán).
- Quote prompt gốc giữ tiếng Anh. Sửa lỗi copy → file mới `<slug>_v2.md`, không sửa file cũ.
- Xong raw thì dừng — digest là việc của skill `make-digest`.

## Schema raw

```markdown
# <tên gợi nhớ>

- Nguồn: <influencer/kênh>
- URL: <link prompt gốc>
- Ngày thu thập: <YYYY-MM-DD>
- Model (nếu raw nói rõ, không đoán): <vd Midjourney v6>

## Prompt gốc

<quote nguyên văn tiếng Anh>
```

## Các bước

1. Hỏi user: ảnh hay video, slug nào, nguồn/URL/ngày nào (nếu thiếu).
2. Ghi file raw đúng schema trên (UTF-8 không BOM).
3. Báo đường dẫn raw để bước digest trỏ về.
