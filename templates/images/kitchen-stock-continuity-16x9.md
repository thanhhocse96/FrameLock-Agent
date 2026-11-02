# Template: KITCHEN_STOCK_CONTINUITY_16x9 — stock bếp chuỗi hành động giữ mặt + prop

> Fill-test 2026-10-06: 5 runs đạt liên tiếp (K2 lowangle, A1 place, A2 flip, A3 season, P1 plate), 0 rớt prompt sau khi đủ ref.
> Kết luận: template này BẮT BUỘC kèm ref đã nén 768px (~85KB): mặt người + món ăn + (tùy shot) ref động tác; ref PNG gốc 2MB treo request. Khung 2 mặt + 2 face ref là vùng cấm (T1 clone vợ ×2 dù đã khóa chữ).

- Dùng cho: ảnh stock bếp 16:9 trong chuỗi nấu ăn liên tục (đặt → trở → nêm → trình bày), giữ identity nhân vật + prop + bếp xuyên suốt.
- Nguồn pattern: production `.local/work/openrouter/2026-10-06-pan-*-1k/` (5 runs đạt) + pack `.local/work/openrouter/2026-10-06-char-*-1k/`; phân tích lỗi đầy đủ ở `journal/2026-10-06-iqf-kitchen-stock-retro.md`.
- Biến (EN `UPPER_SNAKE`): `[CHARACTER]`, `[ACTION]`, `[FOOD_STATE]`, `[CAMERA]`, `[FOCUS]`, `[PROPS]`, `[KITCHEN]`, `[LOCK_NEGATIVE]`

## Prompt mẫu (tiếng Anh, skeleton)

```text
[CAMERA] in [KITCHEN]. [CHARACTER], [ACTION]. [FOOD_STATE]. [PROPS]. [FOCUS]. Warm cinematic light. [LOCK_NEGATIVE]. Photorealistic, 16:9, no text, no logo, no watermark, no extra people
```

## Prompt kết quả khi gen (tiếng Anh — bắt buộc, không dịch sang Việt)

Fill ví dụ A1 tay đặt cá (đã chạy đạt 2026-10-06, $0.024):

```text
Medium close-up in a cozy home kitchen in the evening, camera at a slight low angle near the rim of a dark nonstick frying pan with shallow oil. The same Vietnamese man as the face reference photo, identical face, grey crew-neck t-shirt, torso leaning naturally over the stove, arm extended down, hand gently laying a raw pale-pink grouper fillet like the raw fish reference into the pan, fingers just releasing the fish, candid cooking posture, face softly out of focus at the top edge. Warm cinematic light, focus locked on the hand and fish. No spatula in frame, no floating utensils, photorealistic, 16:9, no text, no logo, no watermark, no extra people
```

## Cách fill biến (tiếng Việt)

- `[CHARACTER]` — khóa identity bằng ref + 1 câu: vd `The same Vietnamese man as the face reference photo, identical face, grey crew-neck t-shirt`. Tuổi ghi số + `no wrinkles` (cấm ghi `early 30s` — Flux vẽ thành ~50, xem retro P1). Wardrobe phải khớp pack.
- `[ACTION]` — đúng 1 động tác + tư thế thân: vd `torso leaning naturally over the stove, arm extended down, hand gently laying ...`. Người nấu phải nghiêng candid, cấm đứng nhìn máy (lỗi tranh truyền thần, retro C1).
- `[FOOD_STATE]` — trạng thái món khớp shot trước/sau: vd `raw pale-pink grouper fillet` (A1) khác `golden seared ... sizzling in foaming butter` (A2/A3). Ref món giữ nguyên miếng cá.
- `[CAMERA]` — khóa cỡ cảnh theo trục siết đã design: A1 rộng → A2 tight chảo lấp khung → A3/K2 về low-angle thấy người. Ghi số/tỉ lệ, không tính từ mơ hồ.
- `[FOCUS]` — khóa điểm nét + vùng nhòe nêu tên: vd `focus locked on the hand and fish` + `the man intentionally defocused`. Shot nào cũng phải có.
- `[PROPS]` — liệt kê khép kín + quy tắc dụng cụ: vd `red spatula held by the hand` hoặc `No spatula in frame`. Mọi dụng cụ có tay cầm hoặc ra khỏi khung (retro P4).
- `[KITCHEN]` — loại bếp + buổi + chất bếp: vd `cozy home kitchen in the evening ... gas stove`. Khóa từ shot đầu, cấm đổi giữa chuỗi (retro B3).
- `[LOCK_NEGATIVE]` — cấm morph/logo/người thừa: `no floating utensils` + (shot 2 người) `exactly one woman, no twins` — lưu ý T1 chứng minh khóa chữ không thắng được 2 face ref đối xứng, trường hợp đó bỏ ref mặt người thứ 2.

## Biến thể (tối đa 3, tiếng Anh)

1. Tight siết vào món (A2): `[CAMERA]` → `Tight close-up ... filling most of the frame`, `[FOCUS]` → `focus locked on the fish and spatula`, người ra khỏi khung.
2. Trình bày ra đĩa (P1): `[CAMERA]` → `Medium side shot ... pan on the left, white plate on wooden board on the right`, `[PROPS]` → `Half a lemon and a small spoon on the board`.
3. Một mình một bếp (né lỗi clone): bỏ người thứ 2 khỏi `[CHARACTER]`, thay bằng `empty chair and a waiting rice bowl at the side of the table`.

(End of file - total 37 lines)
