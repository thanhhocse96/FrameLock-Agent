# Module: research-images

> Invariant riêng cho `research/images/`. Schema chung: raw → digest → mapping.

## Layout

```
research/images/
  raws/<slug>.md        ← prompt text nguyên văn (bất biến)
  digests/<slug>.md     ← phân tích theo schema dưới
  mapping.md            ← index duy nhất (SoT tra cứu)
```

## Schema raw (`raws/<slug>.md`)

```markdown
# <tên gợi nhớ>

- Nguồn: <influencer/kênh>
- URL: <link prompt gốc>
- Ngày thu thập: <YYYY-MM-DD>
- Model (nếu raw nói rõ, không đoán): <vd Midjourney v6>

## Prompt gốc

<quote nguyên văn tiếng Anh>
```

## Schema digest (`digests/<slug>.md`)

```markdown
# Digest: <slug>

- Raw: `../raws/<slug>.md`
- Model: <tên model hoặc "không rõ trong raw">
- Từ khóa: #kỹ-thuật #tone #shot #composition #chủ-đề #model

## Kỹ thuật (lighting, chất liệu, render — mỗi ý kèm Nguồn)
## Tone (mood/cảm xúc/màu sắc — kèm Nguồn)
## Shot (cỡ cảnh, góc máy — kèm Nguồn; vd close-up, wide, low-angle)
## Composition (bố cục, framing, điểm nhấn — kèm Nguồn)
## Chủ đề
## Từ vựng đáng chú ý (quote EN + giải thích VI)
## Công thức rút ra (pattern tái dùng)
## Ghi chú bản quyền/nguồn
```

## Mapping

Mỗi digest = 1 dòng bảng trong `mapping.md`: `| digest | model | kỹ thuật | tone | shot | composition | chủ đề | từ vựng |`.
Từ khóa dùng kebab-case tiếng Anh cho kỹ thuật/model (`cinematic-lighting`), tiếng Việt cho chủ đề (`chân-dung`).
