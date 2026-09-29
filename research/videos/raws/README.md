# raws (video) — prompt text nguyên văn

> Chỉ `.md`/`.txt`. Giữ cấu trúc shot/scene nếu prompt gốc có. Không video binary. Media mẫu → `.local/`.

File mẫu đặt tên `<slug>.md`:

```markdown
# <tên gợi nhớ>

- Nguồn: <influencer/kênh>
- URL: <link prompt gốc>
- Ngày thu thập: <YYYY-MM-DD>
- Model (nếu raw nói rõ, không đoán): <vd Runway Gen-3 / Pika / Sora>

## Prompt gốc (giữ cấu trúc shot/scene nếu có)

<quote nguyên văn tiếng Anh>
```

Raw bất biến: lỗi copy → tạo `<slug>_v2.md`, không sửa file cũ.
