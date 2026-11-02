# Archive — ba request Husband Frame 1→2

Ngày: 2026-10-12. Prompt do agent viết và user yêu cầu thử trong dự án; không phải raw influencer. Chỉ lưu text prompt, settings và provenance, không lưu key, media binary hoặc request base64. Đây là lịch sử thử, không phải template đạt.

Nguồn: settings.json, request.json, job.json, status.json và catalog.json của từng artifact local. Phân tích/feedback nằm ở [DA-005](husband-f1-f2-experiment.md). Đã dừng theo user sau ba run.

## Input chung

- `Husband-Frame-1.png`: SHA-256 `5cde14109de68f017388193db27d1d5f09b195db27fb27907931f7d0c7ce0a71`; media tại `.local/work/openrouter/`, không commit.
- `Husband-Frame-2.png`: SHA-256 `a08975f4730edea6100692d2b8eef0f3a43eb1d9c9c275207c26159e0806b6b4`; media tại `.local/work/openrouter/`, không commit.

## Run 1 — 2026-10-12-husband-f1-f2-delta

- Artifact local: `.local/work/openrouter/2026-10-12-husband-f1-f2-delta/`.
- Hai frame conditioning giống byte-for-byte trong request run 1; không chỉ cùng filename.

### Settings và kết quả API

```json
{
  "model": "bytedance/seedance-1-5-pro",
  "duration": 4,
  "resolution": "480p",
  "aspect_ratio": "16:9",
  "generate_audio": false,
  "seed": 12102026,
  "catalog_canonical_slug": "bytedance/seedance-1-5-pro-20260320",
  "estimated_cost_usd": 0.046116,
  "actual_cost_usd": 0.0487128,
  "job_id": "gen-vid-1791777837-4M2vndhiNUb32o5rC0Ir",
  "status": "completed",
  "changed_fields_vs_run_1": []
}
```

### Prompt đầy đủ (EN)

```text
A continuous accelerated cooking shot connecting the supplied first and last frames. The man finishes gently laying the first raw fish fillet into the pan and releases it. He brings two additional fillets into the pan by hand from the upper edge, placing them one at a time beside the original fillet. Each fillet stays a separate solid piece after placement. His bare hand withdraws, then his hand brings the red spatula into view from the upper edge. In a brief cooking time-lapse, the three fillets become lightly golden as butter foams and faint steam rises. The camera moves smoothly closer and slightly higher toward the pan, ending in the supplied tight close-up with three distinct golden fillets and the hand-held red spatula. Keep the same pan and kitchen. One continuous shot with stable object shapes and natural hand contact.
```

## Run 2 — 2026-10-12-husband-f1-f2-morph

- Artifact local: `.local/work/openrouter/2026-10-12-husband-f1-f2-morph/`.
- Hai frame conditioning giống byte-for-byte trong request run 1; không chỉ cùng filename.

### Settings và kết quả API

```json
{
  "model": "bytedance/seedance-1-5-pro",
  "duration": 4,
  "resolution": "480p",
  "aspect_ratio": "16:9",
  "generate_audio": false,
  "seed": 12102026,
  "catalog_canonical_slug": "bytedance/seedance-1-5-pro-20260320",
  "estimated_cost_usd": 0.046116,
  "actual_cost_usd": 0.0487128,
  "job_id": "gen-vid-1791779142-y9kYanO61cQiD4Sfl85h",
  "status": "completed",
  "changed_fields_vs_run_1": [
    "prompt"
  ]
}
```

### Prompt đầy đủ (EN)

```text
A continuous accelerated cooking shot connecting the supplied first and last frames. The man finishes gently laying the first raw fish fillet into the pan and releases it. He brings two additional fillets into the pan by hand from the upper edge, placing them one at a time beside the original fillet. Each fillet stays a separate solid piece after placement. His bare hand withdraws, then his hand brings the red spatula into view from the upper edge. During the final cooking transition, the three fish fillets smoothly morph into their corresponding cooked shapes in the ending frame. Each fillet remains separate, following a continuous path into its final position. Their surfaces gradually turn golden as butter foams and a brief veil of steam passes over the pan. The camera moves smoothly closer and slightly higher toward the pan, ending in the supplied tight close-up with three distinct golden fillets and the hand-held red spatula. Keep the same pan and kitchen. One continuous shot with three separate fillets throughout the cooking transition and natural hand contact.
```

## Run 3 — 2026-10-12-husband-f1-f2-blocking-10s

- Artifact local: `.local/work/openrouter/2026-10-12-husband-f1-f2-blocking-10s/`.
- Hai frame conditioning giống byte-for-byte trong request run 1; không chỉ cùng filename.

### Settings và kết quả API

```json
{
  "model": "bytedance/seedance-1-5-pro",
  "duration": 10,
  "resolution": "480p",
  "aspect_ratio": "16:9",
  "generate_audio": false,
  "seed": 12102026,
  "catalog_canonical_slug": "bytedance/seedance-1-5-pro-20260320",
  "estimated_cost_usd": 0.11528999999999999,
  "actual_cost_usd": 0.1210296,
  "job_id": "gen-vid-1791779877-8POWDv7mjJgLnQUbDmgA",
  "status": "completed",
  "changed_fields_vs_run_1": [
    "prompt",
    "duration"
  ]
}
```

### Prompt đầy đủ (EN)

```text
A single continuous ten-second cooking shot connecting the supplied first and last frames. The same man, pan and kitchen remain consistent. The camera moves closer slowly during placement, keeping the upper frame boundary available for the hand to enter and exit. It pushes closer more noticeably after placement and settles in the supplied ending close-up.
0.0-1.0 seconds: The man gently lowers and releases the first raw fish fillet into the pan. It rests in the oil. His empty hand withdraws completely beyond the upper edge of the image.
1.0-2.0 seconds: The hand stays fully outside the frame while retrieving another raw fillet off-screen. The first fillet stays in place. The retrieval area is never revealed; no plate is brought into the shot.
2.0-3.5 seconds: The hand re-enters through the upper edge already firmly holding the second raw pink fillet from its first visible moment. It carries that fillet down to an empty area beside the first, makes contact with the pan, releases it, then withdraws empty completely beyond the upper edge.
3.5-4.5 seconds: The hand remains fully outside the frame while retrieving the third raw fillet. The two placed fillets stay separate and stationary.
4.5-6.0 seconds: The hand re-enters already holding the third raw pink fillet. It lowers it into the remaining empty area, releases it only after contact, and withdraws empty fully out of frame. There are now exactly three separate raw fillets in the pan.
6.0-8.4 seconds: With the bare hand completely outside the frame, a visible cooking time-lapse occurs. Only the three fillets already resting in the pan gradually become golden and smoothly change into their corresponding cooked shapes. Each piece remains separate and follows a continuous path into its ending position. Butter gradually foams and a light veil of steam rises. Nothing is added to, laid over, or merged with an existing fillet. The camera continues moving closer.
8.4-9.4 seconds: A hand enters through the upper edge already holding the red spatula. The other hand steadies the pan handle at the right. The spatula gently approaches the cooked fish as the camera converges on the supplied ending composition.
9.4-10.0 seconds: Settle on the tight close-up of three distinct golden fillets with foaming butter and the hand-held red spatula, matching the ending frame. Continuous camera movement, no cut, no dissolve, no sudden layout jump. Fish never appears from an empty visible hand; every additional fillet crosses the frame boundary already held. No extra fish pieces, no cooked fish carried in by hand, and no merging or splitting fillets.
```

## Chi phí và giới hạn

Tổng usage ba run: **$0.2184552**. Run 2 chỉ đổi prompt so với run 1; run 3 đổi prompt và duration. Một mẫu mỗi cấu hình không đủ gán xác suất thành công hoặc chứng minh giới hạn kiến trúc. Các prompt này không đạt toàn bộ strict spec; user chấp nhận hình ảnh run 1 và yêu cầu dừng sau run 3.
