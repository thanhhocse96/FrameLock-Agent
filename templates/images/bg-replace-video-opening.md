# Template: Object-to-Opening — nền chuyển cảnh mở đầu video từ vật thể bất kỳ

- Dùng cho: ảnh — tạo ảnh nền chuyển cảnh/mở đầu video từ 1 vật thể bất kỳ (giữ vật, thay nền, khớp sáng)
- Nguồn pattern: `../../research/images/digests/bg-replace-greenscreen.md` (đã test fill qua chuỗi cart 2026-09-29: v1-dim, v4-checkout, v5-trunk, M1-corridor, M2-elevator)
- Biến (EN `UPPER_SNAKE`): `[SUBJECT_LOCK]`, `[ENVIRONMENT_DETAILS]`, `[LIGHT_DIRECTION]`, `[LIGHT_COLOR_TEMP]`, `[LIGHT_INTENSITY]`, `[AMBIENT_FILL]`, `[RIM_LIGHT]`, `[SHADOW_GROUNDING]`, `[ATMOSPHERE]`, `[LENS_TYPE]`, `[DEPTH_OF_FIELD]`, `[COLOR_GRADE]`

## Prompt mẫu (tiếng Anh, fill sẵn ví dụ thật từ chuỗi cart)

```text
Transform this image into a supermarket frozen aisle at daytime. Keep the shopping cart shape, blue handles, metal grid, and all frozen fish packs with labels and text exactly the same, no text distortion, no reshaping. Remove the black background completely. Replace the background completely with open freezer glass cabinets on the left, stacked yellow and red promo boxes on the right, beige tile floor, overhead long fluorescent tubes dimmed.

Relight the subject to match the new environment: key light is dim soft overhead fluorescent from directly above, color temperature 4500K, low contrast, no harsh glare. Fill shadows with cool ambient bounce inside the basket. Add faint cool rim on metal wires. Ground the packs with soft contact shadows inside the basket and faint floor reflection under the cart. Add none. Shot on 35mm lens with medium depth of field, foreground packs sharp, background slightly blurred. Match white balance, saturation and grain. Style: photorealistic, no people in foreground, not stylized or cartoon.
```

## Prompt kết quả khi gen (tiếng Anh — bắt buộc, không dịch sang Việt)

```text
Transform this image into [ENVIRONMENT_DETAILS]. Keep [SUBJECT_LOCK] exactly the same, no distortion, no reshaping. Remove the original background completely. Replace the background completely with [ENVIRONMENT_DETAILS].

Relight the subject to match the new environment: key light from [LIGHT_DIRECTION], color temperature [LIGHT_COLOR_TEMP], contrast and hardness [LIGHT_INTENSITY]. Fill shadows with [AMBIENT_FILL]. Add rim/back light [RIM_LIGHT]. Ground the subject with [SHADOW_GROUNDING].

Add [ATMOSPHERE] (if needed). Shot on [LENS_TYPE] with [DEPTH_OF_FIELD]. Match white balance, saturation and grain with [COLOR_GRADE]. Style: cinematic, high-end, realistic, not stylized or cartoon.
```

## Cách fill biến (tiếng Việt, mỗi biến 1 dòng + ví dụ)

- `[SUBJECT_LOCK]` — liệt kê cái cấm sửa: vd `the shopping cart shape, blue handles, metal grid, and all packs with labels and text`. Không ghi chung chung `subject`.
- `[ENVIRONMENT_DETAILS]` — nền mở đầu video, phải kèm nguồn sáng trong cảnh: vd `frozen aisle with glass cabinets left, promo stacks right, beige tile floor, dimmed fluorescent tubes`.
- `[LIGHT_DIRECTION]` — hướng key light nhìn từ vật: vd `dim soft overhead fluorescent from directly above`.
- `[LIGHT_COLOR_TEMP]` — nhiệt màu + màu rim: vd `4500K with faint cool rim on metal`.
- `[LIGHT_INTENSITY]` — độ gắt/mềm + tương phản: vd `low contrast, no harsh glare`.
- `[AMBIENT_FILL]` — sáng môi trường nâng vùng tối: vd `cool ambient bounce inside the basket`.
- `[RIM_LIGHT]` — viền tách vật khỏi nền: vd `faint cool rim on metal wires`.
- `[SHADOW_GROUNDING]` — bóng tiếp xúc + phản chiếu mặt đặt: vd `soft contact shadows inside the basket and faint floor reflection`.
- `[ATMOSPHERE]` — hạt/khí quyển hoặc `none`: vd `none`, `light frost haze`.
- `[LENS_TYPE]` — vd `35mm`, `50mm`.
- `[DEPTH_OF_FIELD]` — mở đầu video nên đủ sâu để vật nét: vd `medium depth of field, foreground sharp, background slightly blurred`.
- `[COLOR_GRADE]` — vd `matched white balance, saturation and grain`.

## Biến thể (tối đa 3, vẫn tiếng Anh)

1. Giữ sáng gốc (nền mới cùng điều kiện sáng với ảnh gốc):
```text
Replace the background completely with [ENVIRONMENT_DETAILS] under lighting identical to the original photo. Keep [SUBJECT_LOCK] pixel-identical, only decontaminate edges. Do not relight. Match only white balance, grain and [DEPTH_OF_FIELD] with [LENS_TYPE]. [COLOR_GRADE].
```

2. Mở đầu đêm (relight mạnh):
```text
Relight [SUBJECT_LOCK] for a night version of [ENVIRONMENT_DETAILS]: key [LIGHT_DIRECTION] at [LIGHT_COLOR_TEMP], deep shadows [LIGHT_INTENSITY], strong [RIM_LIGHT], reflective [SHADOW_GROUNDING], [ATMOSPHERE], [LENS_TYPE] + [DEPTH_OF_FIELD], [COLOR_GRADE].
```

3. Nối clip (end frame trùng start clip kế):
```text
Same composition as [SUBJECT_LOCK] placed for video opening: [ENVIRONMENT_DETAILS], relight [LIGHT_DIRECTION] + [LIGHT_COLOR_TEMP] + [LIGHT_INTENSITY], fill [AMBIENT_FILL], rim [RIM_LIGHT], grounding [SHADOW_GROUNDING]. Framing leaves the subject in the same screen position as the next clip's first frame. [LENS_TYPE] + [DEPTH_OF_FIELD]. [COLOR_GRADE]. Photorealistic, no stylization.
```
