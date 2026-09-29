# Phân tích: Background Replace trên nhân vật phông xanh

- Ngày: 2026-09-29
- Prompt gốc: lướt YouTube, mất URL (không lập `research/images/raws/` để tránh digest mồ côi — PITFALLS #1)
- Draft kèm theo: `./bg-replace-greenscreen.md`
- Trạng thái: chờ bạn gọi để thử nghiệm fill biến

## 1. Prompt gốc (giữ tiếng Anh)

```text
Transform this image into a [NEW LOCATION / ENVIRONMENT]. Keep the subject's face, pose, and clothing exactly the same. Replace the background completely with [ENVIRONMENT DETAILS]. Match the lighting on the subject to the new environment so it feels natural and realistic. Add [SNOW, RAIN, etc.] (if needed). Use a [LENS TYPE] with [SHALLOW or DEEP DEPTH OF FIELD]. Ensure realistic lighting, shadows, and color that match the scene. Style: cinematic, high-end, realistic (not stylized or cartoon).
```

## 2. Template này có gì? (6 khối)

1. Preserve: `Keep face, pose, clothing exactly the same` — khóa danh tính.
2. Replace: `Replace background with [ENVIRONMENT DETAILS]` — thay nền hoàn toàn.
3. Light-match chung: `Match the lighting... natural and realistic` — 1 câu mơ hồ, không hướng/màu/độ gắt.
4. Atmosphere: `Add [SNOW, RAIN]` — hạt khí quyển.
5. Optics: `[LENS TYPE] + [SHALLOW/DEEP DOF]`.
6. Quality: `cinematic, high-end, realistic (not cartoon)`.

## 3. Có tách sang ngữ cảnh khác được không? Có.

Khung tổng quát: Subject-lock + Env-replace + Relight + Optics + Grade.
Chỉ cần đổi `[SUBJECT_LOCK]`:

- Người: `face, facial structure, pose, clothing`
- Sản phẩm: `label, logo, shape, material`
- Pet/xe: `fur pattern and pose / body shape`

Phần relight/optics/grade giữ nguyên.

## 4. Yêu cầu nhân vật / ánh sáng / nền

- Nhân vật: bản gốc `exactly the same` vẫn bị model làm đẹp/bóp mặt. Bản v2 ép: `100% identity preservation, no beautification, no reshaping + remove green spill on edges/hair`.
- Ánh sáng: điểm yếu nhất — thiếu hướng, nhiệt màu, độ gắt, fill, rim, bóng tiếp xúc. Model chỉ phủ sáng/tối toàn cục.
- Bối cảnh: `[ENVIRONMENT_DETAILS]` phải kèm nguồn sáng trong cảnh (vd `warm shop windows left + cool overcast sky + wet asphalt`). Không có neo sáng thì `match lighting` vô nghĩa.

## 5. Vì sao gen ra không hòa vào không gian?

Model text-only grade màu overlay, không relight vật lý (không normal/geometry/HDRI). Người thật cần:

- Key có hướng + màu + độ gắt riêng
- Fill/ambient nâng vùng tối
- Rim tách khỏi nền
- Contact shadow + reflection + AO nếp áo để đứng xuống đất
- WB da + grain + DOF khớp

Thiếu 5 thứ này là trông dán nổi.

## 6. Bậc thầy lighting/compositing làm thế nào?

- Color → Light → Edges (PHLEARN, Photoshop Training Channel): khớp WB/saturation trước, rồi hướng/cường độ, rồi viền/spill/grain.
- Total Relighting (Google SIGGRAPH 2021): matting giữ tóc → geometry/albedo → light-map diffuse/specular từ panorama nền → render lại. Prompt chữ phải giả lập HDRI bằng cách tả từng đèn.
- Relightful Harmonization (CVPR 2024, Adobe): mã hóa sáng nền + align env-map, xóa bóng studio cũ + tạo self-shadow mới theo hướng nền.
- NVIDIA VideoRelighting: HDRI 2:1 làm môi trường sáng rồi composite lên.
- Cinematic Compositing 2026: tách vùng preserve-and-relight (da mặt) vs geometry-preserving.

## 7. Checklist gọi lên khi thử nghiệm

Khi bạn nói thử nghiệm, mình sẽ hỏi:

1. `[ENVIRONMENT_DETAILS]` + nguồn sáng trong cảnh là gì?
2. `[LIGHT_DIRECTION]` nhìn từ nhân vật (vd front-right above)?
3. Ngày hay đêm? `[LIGHT_COLOR_TEMP]` + `[LIGHT_INTENSITY]`?
4. Có rim không? `[RIM_LIGHT]` màu gì, từ đâu?
5. Mặt đất nào? `[SHADOW_GROUNDING]` (contact shadow + reflection)?
6. `[ATMOSPHERE]`? `[LENS_TYPE]` + `[DEPTH_OF_FIELD]`?

Rồi xuất 1 prompt tiếng Anh hoàn chỉnh từ `./bg-replace-greenscreen.md` để bạn paste đi gen. Kết quả tốt → promote theo pipeline raw → digest → mapping → `templates/images/`.
