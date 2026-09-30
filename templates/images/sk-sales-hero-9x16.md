# Template: SK_SALES_HERO_9x16 — ảnh hero chuẩn bán hàng

> Fill-test 2026-09-29: Soul v2 text-only (không ref) rớt — cá còn đầu, túi sai màu, props thừa.
> Kết luận: template này BẮT BUỘC kèm ≥2 ref thật (scene + nguyên liệu + bao bì), không chạy prompt chay.

- Dùng cho: ảnh tĩnh bán hàng 9:16 (top-down fisheye, nguyên liệu sống + bao bì), mở đầu chuỗi sơ chế / thumbnail dọc.
- Nguồn pattern: production `.local/work/higgsfield/2026-09-29-soche/s1-master-final/` (chưa có digest — đúc từ experiment đã user-chốt, ngoại lệ có ghi nhận).
- Biến (EN `UPPER_SNAKE`): `[PRODUCT]`, `[FISH]`, `[TRAY]`, `[PROPS]`, `[PACK]`, `[STYLE]` (tùy chọn).

## Prompt mẫu (tiếng Anh, fill sẵn ví dụ cá đục SK)

```text
Vertical 9:16 strong circular fisheye top-down food photography on a rustic wooden table, visible round fisheye distortion at the frame edges, warm cinematic lighting, photorealistic: an empty black clay pot (uncooked, nothing inside) at the center; beside the pot a LONG white polystyrene styrofoam tray (opaque white foam, NOT transparent plastic) holding [FISH]; underneath the tray [PACK] lies flat and empty, SLIGHTLY BIGGER than the tray so its edges extend beyond the tray on all sides, with part of its SK logo visibly peeking out; [PROPS] arranged around the pot; a light touch of frost and tiny ice crystals on the frozen fish; [STYLE]; no people, no hands, no cooked food, no text except the partial real product logo
```

## Prompt kết quả khi gen (tiếng Anh — bắt buộc, không dịch sang Việt)

Fill ví dụ cá đục SK (đã user-chốt 2026-09-29):

```text
Vertical 9:16 strong circular fisheye top-down food photography on a rustic wooden table, visible round fisheye distortion at the frame edges, warm cinematic lighting, photorealistic: an empty black clay pot (uncooked, nothing inside) at the center; beside the pot a LONG white polystyrene styrofoam tray (opaque white foam, NOT transparent plastic) holding cleaned snakehead fish — whole bodies with heads cut off, no eyes, intact silvery skin — arranged neatly in 2 rows; underneath the tray the SK product pouch lies flat and empty, SLIGHTLY BIGGER than the tray so its edges extend beyond the tray on all sides, with part of its SK logo visibly peeking out; small bowls of black peppercorns, sliced red chilies, sliced scallions and glass spice jars arranged around the pot; a light touch of frost and tiny ice crystals on the frozen fish; appetizing frozen-seafood commercial look; no people, no hands, no cooked food, no text except the partial real product logo
```

## Cách fill biến (tiếng Việt)

- `[PRODUCT]` — tên SP + món (vd `cá đục kho tiêu SK`). Quyết định bối cảnh món ăn.
- `[FISH]` — mô tả nguyên liệu chính xác tới mức loài + tình trạng (vd `cleaned snakehead fish, heads cut off, 2 rows`). Biến quan trọng nhất — model hay tự bịa cá lạ nếu ghi chung chung.
- `[TRAY]` — loại khay + màu + độ đục (vd `LONG white polystyrene styrofoam tray, opaque, NOT transparent plastic`). Luôn phủ định vật liệu sai đã từng gặp.
- `[PROPS]` — đạo cụ quanh nồi, liệt kê khép kín (vd `small bowls of black peppercorns, sliced red chilies, sliced scallions and glass spice jars`). Thừa 1 món là model tự thêm rác.
- `[PACK]` — bao bì + vị trí + tỉ lệ vs khay (vd `the SK product pouch ... SLIGHTLY BIGGER than the tray`). Ghi rõ tỉ lệ, không để model tự đoán.
- `[STYLE]` — phong cách chốt (vd `appetizing frozen-seafood commercial look`). Tùy chọn.

## Biến thể (tối đa 3, tiếng Anh)

1. Ngang 16:9 (thumbnail ngang): đổi `Vertical 9:16` → `Horizontal 16:9`, giữ nguyên còn lại.
2. Không tuyết (hàng tươi, không cấp đông): bỏ câu `a light touch of frost...`.
3. Không người → có tay (shot hành động): thay `no people, no hands` → `a woman's hands arranging ingredients at the top edge` + ref mặt nếu cần giữ nhân vật.
