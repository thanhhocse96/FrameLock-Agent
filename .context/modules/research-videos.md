# Module: research-videos

> Invariant riêng cho `research/videos/`. Khác ảnh ở trục thời gian: shot, chuyển động camera, nhịp dựng.

## Layout

```
research/videos/
  raws/<slug>.md        ← prompt text nguyên văn (kể cả prompt chia shot/scene)
  digests/<slug>.md     ← phân tích theo schema dưới
  mapping.md            ← index duy nhất (SoT tra cứu)
```

## Schema raw (`raws/<slug>.md`)

```markdown
# <tên gợi nhớ>

- Nguồn: <influencer/kênh>
- URL: <link prompt gốc>
- Ngày thu thập: <YYYY-MM-DD>
- Model (nếu raw nói rõ, không đoán): <vd Runway Gen-3 / Pika / Sora>

## Prompt gốc (giữ cấu trúc shot/scene nếu có)

<quote nguyên văn tiếng Anh>
```

## Schema digest (`digests/<slug>.md`)

```markdown
# Digest: <slug>

- Raw: `../raws/<slug>.md`
- Model: <tên model hoặc "không rõ trong raw">
- Từ khóa: #kỹ-thuật #tone #shot #composition #chủ-đề #model

## Kỹ thuật (lighting, motion, render — mỗi ý kèm Nguồn)
## Tone (mood/cảm xúc/nhịp cảm — kèm Nguồn)
## Shot (cỡ cảnh, góc máy, camera move từng shot — kèm Nguồn)
## Composition (bố cục, framing trong khung hình động — kèm Nguồn)
## Cấu trúc thời gian (shot 1→n, chuyển cảnh, nhịp)
## Chủ đề
## Từ vựng đáng chú ý (quote EN + giải thích VI, nhất là động từ motion)
## Công thức rút ra (pattern tái dùng)
## Ghi chú bản quyền/nguồn
```

## Mapping

Mỗi digest = 1 dòng bảng trong `mapping.md`: `| digest | model | kỹ thuật | tone | shot | composition | cấu trúc thời gian | chủ đề |`.
Động từ motion giữ tiếng Anh (`dolly-in`, `pan-left`, `slow-push`).
