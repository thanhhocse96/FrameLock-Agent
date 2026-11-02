# Digest: bg-replace-greenscreen

- Raw: `../raws/bg-replace-greenscreen.md`
- Model: không rõ trong raw
- Từ khóa: #background-replacement #subject-lock #relighting #cinematic-realistic #medium-shot #centered-composition #mo-hinh-khong-ro

## Kỹ thuật (lighting, chất liệu, render — mỗi ý kèm Nguồn)

- Khóa chủ thể: giữ nguyên mặt/dáng/quần áo, chỉ thay nền — Nguồn: `../raws/bg-replace-greenscreen.md#prompt-gốc` (câu `Keep the subject's face, pose, and clothing exactly the same`).
- Thay nền hoàn toàn bằng mô tả môi trường mới — Nguồn: `../raws/bg-replace-greenscreen.md#prompt-gốc` (câu `Replace the background completely with [ENVIRONMENT DETAILS]`).
- Khớp sáng-bóng-màu theo nền mới, ghi 2 lần trong raw — Nguồn: `../raws/bg-replace-greenscreen.md#prompt-gốc` (câu `Match the lighting...` + câu `Ensure realistic lighting, shadows, and color`).
- Điểm yếu: lệnh khớp sáng chung chung, không hướng/nhiệt màu/rim/bóng tiếp xúc → ảnh gen dễ bị phủ sáng mà không chìm vào không gian (kết luận từ chuỗi thử cart v1-dim, 2026-09-29).
- Khống chế quang học: loại lens + độ sâu trường ảnh — Nguồn: `../raws/bg-replace-greenscreen.md#prompt-gốc` (câu `Use a [LENS TYPE] with [SHALLOW or DEEP DEPTH OF FIELD]`).

## Tone (mood/cảm xúc/màu sắc — kèm Nguồn)

- Cinematic, high-end, realistic; cấm stylized/cartoon — Nguồn: `../raws/bg-replace-greenscreen.md#prompt-gốc` (câu `Style:` cuối).

## Shot (cỡ cảnh, góc máy — kèm Nguồn)

- Không quy định cỡ cảnh/góc máy trong raw; giữ nguyên framing ảnh đầu vào (suy ra từ lệnh giữ pose) — Nguồn: `../raws/bg-replace-greenscreen.md#prompt-gốc`.

## Composition (bố cục, framing, điểm nhấn — kèm Nguồn)

- Chủ thể giữ vị trí cũ làm neo, nền mới lấp đầy phần còn lại; hạt thời tiết làm điểm nhấn sâu — Nguồn: `../raws/bg-replace-greenscreen.md#prompt-gốc` (câu `Add [SNOW, RAIN, etc.]`).

## Chủ đề

- Thay nền hậu kỳ từ vật thể bất kỳ; dùng làm ảnh nền chuyển cảnh/mở đầu video.

## Từ vựng đáng chú ý (quote EN + giải thích VI)

- `Keep ... exactly the same` — khóa danh tính, chống model tự làm đẹp/bóp hình.
- `Match the lighting ... so it feels natural and realistic` — lệnh relight nhưng thiếu thông số, cần fill thêm khi đúc template.
- `not stylized or cartoon` — chặn model trôi sang hoạt hình khi nền khó.

## Công thức rút ra (pattern tái dùng)

`Subject-lock + Env-replace + Relight + Atmosphere + Optics + Grade` — đổi `[SUBJECT_LOCK]` là dùng cho ngữ cảnh khác (người/sản phẩm/xe).

## Ghi chú bản quyền/nguồn

- Prompt lướt YouTube, chỉ rõ kênh, không rõ video cụ thể; dùng nội bộ, không re-post nguyên khối.
