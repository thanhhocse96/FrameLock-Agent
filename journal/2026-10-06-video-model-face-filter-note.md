# Note — model video OpenRouter và filter mặt người (2026-10-06)

> Đọc trước khi chọn model cho clip có người. Nguồn: experiment thật, không đoán.

## Ma trận đã kiểm chứng

| Model | Ảnh conditioning có người photorealistic | Bằng chứng |
|---|---|---|
| `heygen/heygen-video-1` | ĂN (pass) | `2026-10-06-heygen-a1-5s` — first_frame mặt chồng rõ, 5s 480p, $0.05 completed |
| `bytedance/seedance-2.0-fast` | CHẶN (fail) | `params-seedance-f15-f2-5s.json` — submit `400 InputImageSensitiveContentDetected.PrivacyInformation`, `content[1]` (last_frame tay + chảo) bị coi là người thật. Request id `02179127374078340df8d8926005c369421892d4819382e5b5ca3` |
| `bytedance/seedance-2.0/image-to-video` (Higgsfield) | ĂN (pass) | `2026-10-06-seedance2-f2-f3-t3-6s` — frame người + kẹp đích 6s 480p completed. Filter người thật chỉ dính bản OpenRouter fast |
| `google/veo-3.1-lite` | ĂN (pass) | `2026-10-06-veo-f4-f5-6s` — kẹp 4→5 có người 6s completed, $0.3 |

## Luật định tuyến (áp dụng khi viết prompt clip)

1. Clip có người (mặt/tay photorealistic trong frame) → HeyGen, Seedance 2.0 bản Higgsfield, hoặc test Veo. KHÔNG dùng Seedance bản OpenRouter fast.
2. Clip không người (cận cá, bơ sủi, timelapse vi mô) → model nào cũng được, ưu tiên Seedance (min 4s + kẹp 2 đầu + có audio option).
3. Filter của provider không phân biệt người AI hay thật — cứ giống người thật là chặn (chống deepfake). Không cố lách bằng cách đổi frame tương tự, đổi model mới là fix đúng.
4. HeyGen chỉ kẹp `first_frame` — đuôi clip để model tự diễn, cắt 2-3s đẹp ở dựng.

## Vận hành (phụ)

- `403 Key limit exceeded (total limit)` trưa 2026-10-06: hết hạn mức key chứ không phải hết credit — nâng limit ở trang keys rồi chạy lại, request chưa submit thì không mất tiền.
- Chạy HeyGen frame 1.5 đã build params (`params-heygen-f15-5s.json`) nhưng user abort trước khi có kết quả → chưa tốn tiền, chưa ghi INDEX. Cần thì chạy lại 1 lệnh.
