# Template: Background Replace trên nhân vật phông xanh (draft)

- Dùng cho: ảnh — thay nền hoàn toàn, giữ nguyên nhân vật chụp phông xanh
- Nguồn pattern: chat 2026-09-29 (prompt gốc lướt YouTube, mất URL — chưa có `research/images/digests/` thật, nên giữ `drafts/` theo PITFALLS #6)
- Biến (EN `UPPER_SNAKE`): `[SUBJECT_LOCK]`, `[ENVIRONMENT_DETAILS]`, `[LIGHT_DIRECTION]`, `[LIGHT_COLOR_TEMP]`, `[LIGHT_INTENSITY]`, `[AMBIENT_FILL]`, `[RIM_LIGHT]`, `[SHADOW_GROUNDING]`, `[ATMOSPHERE]`, `[LENS_TYPE]`, `[DEPTH_OF_FIELD]`, `[COLOR_GRADE]`

> Prompt gốc (giữ tiếng Anh, nguồn YouTube mất URL):
> `Transform this image into a [NEW LOCATION / ENVIRONMENT]. Keep the subject's face, pose, and clothing exactly the same. Replace the background completely with [ENVIRONMENT DETAILS]. Match the lighting on the subject to the new environment so it feels natural and realistic. Add [SNOW, RAIN, etc.] (if needed). Use a [LENS TYPE] with [SHALLOW or DEEP DEPTH OF FIELD]. Ensure realistic lighting, shadows, and color that match the scene. Style: cinematic, high-end, realistic (not stylized or cartoon).`

## Prompt mẫu (tiếng Anh, fill sẵn 1 ví dụ minh họa — chưa phải digest thật)

```text
Transform this image into a snowy mountain street at blue hour. Keep the subject's face, facial structure, pose, and clothing exactly the same — 100% identity preservation, no beautification, no body reshaping. Remove green spill on edges and hair completely. Replace the background completely with a snow-covered alpine street, warm shop windows on the left, cool overcast sky, wet asphalt with reflections.

Relight the subject to match the new environment: key light is a soft cool overcast skylight from front-right above ([LIGHT_DIRECTION]), color temperature 6500K with warm practical rim from shop windows on the left ([LIGHT_COLOR_TEMP]). Moderate contrast, soft shadows ([LIGHT_INTENSITY]). Add cool ambient fill to lift shadow side, no harsh top-down shadow ([AMBIENT_FILL]). Add faint warm rim light on left edge of face, hair and shoulder from shop windows ([RIM_LIGHT]). Ground the subject with a soft contact shadow under feet matching wet asphalt reflection, plus subtle ambient occlusion in clothing folds ([SHADOW_GROUNDING]).

Add light falling snow with natural motion blur and slight atmospheric haze for depth ([ATMOSPHERE]). Shot on 50mm lens, shallow depth of field, background slightly blurred but shop lights recognizable as bokeh ([LENS_TYPE], [DEPTH_OF_FIELD]). Match skin-tone saturation and white balance to scene, warm highlights with cool shadows, subtle film grain for cohesion ([COLOR_GRADE]). Style: cinematic, high-end, realistic, not stylized or cartoon.
```

## Prompt kết quả khi gen (tiếng Anh — bắt buộc, không dịch sang Việt)

```text
Transform this image into [ENVIRONMENT_DETAILS]. Keep [SUBJECT_LOCK] exactly the same — 100% identity preservation, no beautification, no body reshaping. Remove green spill on edges and hair completely. Replace the background completely with [ENVIRONMENT_DETAILS].

Relight the subject to match the new environment: key light from [LIGHT_DIRECTION], color temperature [LIGHT_COLOR_TEMP], contrast and hardness [LIGHT_INTENSITY]. Fill shadows with [AMBIENT_FILL]. Add rim/back light [RIM_LIGHT]. Ground the subject with [SHADOW_GROUNDING].

Add [ATMOSPHERE] (if needed). Shot on [LENS_TYPE] with [DEPTH_OF_FIELD]. Match white balance, saturation and grain with [COLOR_GRADE]. Style: cinematic, high-end, realistic, not stylized or cartoon.
```

## Cách fill biến (tiếng Việt)

- `[SUBJECT_LOCK]` — ghi rõ cái gì cấm sửa: vd `the subject's face, facial structure, pose, and clothing`. Không ghi chung chung `subject`.
- `[ENVIRONMENT_DETAILS]` — bối cảnh phải kèm nguồn sáng có sẵn trong cảnh: vd `snow-covered alpine street, warm shop windows on the left, cool overcast sky, wet asphalt`. Càng ghi rõ vị trí đèn, prompt relight càng có neo.
- `[LIGHT_DIRECTION]` — hướng key light nhìn từ nhân vật: vd `soft cool skylight from front-right above`, `low warm sunset from left behind`. Đây là biến prompt gốc thiếu nên hay sai hướng sáng.
- `[LIGHT_COLOR_TEMP]` — nhiệt màu + màu rim: vd `6500K overcast key + 3200K warm practical rim from left`. Ép model tách key/fill thay vì phủ sáng chung.
- `[LIGHT_INTENSITY]` — độ gắt/mềm + tương phản: vd `soft diffused, low contrast`, `hard direct sun, high contrast with sharp shadow`.
- `[AMBIENT_FILL]` — ánh sáng môi trường hắt lên vùng tối: vd `cool ambient bounce to lift shadow side`.
- `[RIM_LIGHT]` — viền tách người khỏi nền: vd `faint warm rim on left edge of hair/shoulder`. Không có rim là trông dán nổi.
- `[SHADOW_GROUNDING]` — bóng tiếp xúc + phản chiếu mặt đất: vd `soft contact shadow under feet on wet asphalt + faint reflection`. Đây là thứ khiến người "đứng vào" không gian.
- `[ATMOSPHERE]` — hạt/lớp khí quyển: vd `light falling snow + haze`, `dust in backlight`, hoặc `none`.
- `[LENS_TYPE]` — vd `50mm`, `35mm`, `85mm portrait lens`.
- `[DEPTH_OF_FIELD]` — vd `shallow depth of field, background bokeh`, `deep focus, background sharp`.
- `[COLOR_GRADE]` — vd `warm highlights / cool shadows, matched skin tone, subtle grain`.

## Biến thể (tối đa 3, vẫn tiếng Anh)

1. Giữ nguyên ánh sáng gốc (chỉ đổi nền, không relight — khi nền cùng điều kiện sáng với ảnh gốc):
```text
Replace the background completely with [ENVIRONMENT_DETAILS] with lighting condition identical to the original photo. Keep [SUBJECT_LOCK] pixel-identical, only decontaminate green edges. Do not relight the subject. Match only white balance, grain and [DEPTH_OF_FIELD] with [LENS_TYPE]. [COLOR_GRADE].
```

2. Đổi ngày → đêm (relight mạnh, test bóng đổ):
```text
Relight [SUBJECT_LOCK] for night version of [ENVIRONMENT_DETAILS]: key light [LIGHT_DIRECTION] at [LIGHT_COLOR_TEMP], deep shadows [LIGHT_INTENSITY], strong [RIM_LIGHT] from neon/practical, reflective [SHADOW_GROUNDING] on wet ground, [ATMOSPHERE], [LENS_TYPE] + [DEPTH_OF_FIELD], [COLOR_GRADE].
```

3. Khung tổng quát hóa ngữ cảnh khác (sản phẩm/vật nuôi/xe — thay SUBJECT_LOCK):
```text
Transform this image into [ENVIRONMENT_DETAILS]. Keep [SUBJECT_LOCK, e.g. product label, logo, shape / pet's fur pattern and pose] exactly the same. Relight with key [LIGHT_DIRECTION] + [LIGHT_COLOR_TEMP] + [LIGHT_INTENSITY], fill [AMBIENT_FILL], rim [RIM_LIGHT], grounding [SHADOW_GROUNDING]. Add [ATMOSPHERE]. Shot on [LENS_TYPE] with [DEPTH_OF_FIELD]. [COLOR_GRADE]. Photorealistic, no stylization.
```

## Vì sao bản gốc lỗi sáng + học từ compositing master (tóm tắt để test)

- Bản gốc chỉ nói `Match the lighting` chung chung → model phủ lớp sáng/tối toàn cục, không relight vật lý (không có diffuse/specular theo normal, không có HDRI môi trường).
- Quy trình chuẩn Color → Light → Edges (PHLEARN / Photoshop Training Channel): khớp white balance/saturation trước, rồi hướng/cường độ sáng, rồi viền + spill + grain.
- Total Relighting (Google SIGGRAPH 2021): matting giữ tóc + ước lượng geometry/albedo + light-map diffuse/specular từ panorama nền rồi render lại — đó là cái prompt text-only không làm được, nên phải mô tả chi tiết từng nguồn sáng để "giả lập" HDRI bằng chữ.
- Relightful Harmonization (CVPR 2024, Adobe): mã hóa ánh sáng nền + align với env-map panorama; xử lý xóa bóng gắt cũ + tạo self-occlusion shadow mới — prompt cần ra lệnh rõ `remove original studio shadow, generate new shadow consistent with [LIGHT_DIRECTION]`.
- Lỗi hay gặp: thiếu rim → nổi khỏi nền; thiếu contact shadow/reflection → bay; sai color temp → da lạc tông; DOF/grain lệch → lộ ghép.
