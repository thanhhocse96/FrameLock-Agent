# Template: Kịch bản video thương mại ngắn — keyframe neo + clip một-động-tác (draft)

- Dùng cho: video — quảng cáo sản phẩm ngắn dạng chuỗi keyframe → clip image-to-video kẹp 2 đầu (MiniMax H3), 9:16 hoặc 16:9
- Nguồn pattern: journal production thật, chưa có `research/videos/digests/` nên giữ `drafts/` theo PITFALLS #6:
  - `journal/2026-09-28-ca-duc-kho-tieu-retro.md` (neo-cuối–sinh-lùi, viết mềm, 1 clip 1 động tác)
  - `journal/2026-09-28-keyframe-splitting.md` (khóa camera, tỉ lệ số, ref cùng trạng thái)
  - `journal/2026-09-29-cart-video-timelapse-note.md` (ngữ pháp H3 kẹp 2 đầu, 3 cách nối timelapse)
  - `journal/2026-09-29-master-soche-fail-log.md` (cặp khẳng–phủ vật liệu, so kèo MS/Grok)
- Biến (EN `UPPER_SNAKE`): `[PRODUCT]`, `[END_FRAME]`, `[PROP_LIST]`, `[STATE_AXIS]`, `[CAMERA]`, `[MOTION]`, `[ATMOSPHERE]`, `[LOCK_NEGATIVE]`, `[DURATION_SEC]`

## Prompt mẫu (tiếng Anh, fill sẵn ví dụ Cá đục kho tiêu từ journal — chưa phải digest thật)

Keyframe neo (frame cuối, chốt trước):

```text
Top-down fisheye shot, 16:9, 2K. A rustic clay pot of caramelized sand goby stew (ca duc kho tieu), glossy amber sauce gently bubbling, on a black induction cooktop with a faint blue energy ring. A woman's hands in dark sleeves lift the pot; beside it a finished product pouch, small bowls of fish sauce, sugar, black pepper, garlic. Warm cinematic side light, shallow steam rising. RAW-to-final state: fully cooked, ready to serve. NOT raw fish, NOT transparent plastic tray, no text on pouch except SK logo.
```

Clip kẹp 2 đầu (1 động tác duy nhất, viết mềm):

```text
Single unbroken take, no cut, no dissolve. Fish sauce pours gently from the tall bottle into the clay pot in a thin continuous stream; the camera pushes in with small amplitude at slow speed. Fine mist and warm steam drift upward while the pot stays sharp. NOT slamming, NOT bursting, no morphing of bottle or pot, labels hold readable.
```

## Prompt kết quả khi gen (tiếng Anh — bắt buộc, không dịch sang Việt)

Khối keyframe (sinh frame cuối trước, rồi sinh lùi):

```text
[CAMERA]. [END_FRAME] featuring [PRODUCT] with [PROP_LIST]. [ATMOSPHERE]. State lock: [STATE_AXIS]. [LOCK_NEGATIVE].
```

Khối clip (mỗi clip đúng 1 `[MOTION]`, thời lượng `[DURATION_SEC]`):

```text
Single unbroken take, no cut, no dissolve. [MOTION]; the camera [CAMERA]. [ATMOSPHERE]. [LOCK_NEGATIVE]. Hold sharp for the last second.
```

## Cách fill biến (tiếng Việt)

- `[PRODUCT]` — sản phẩm + trạng thái đúng frame: vd `caramelized sand goby stew, fully cooked` (K7) khác `raw cleaned sand goby, uncooked` (K1). Ref phải cùng trạng thái sống/chín với frame cần gen.
- `[END_FRAME]` — tả frame cuối (neo) chứa đủ prop đã duyệt: vd `rustic clay pot on induction cooktop, product pouch beside it`. Neo là frame sửa tới cùng; frame giữa chấp nhận 90%.
- `[PROP_LIST]` — liệt kê prop kèm vật liệu khóa cặp khẳng–phủ: vd `opaque white foam tray, NOT transparent plastic; TALL sauce bottle, twice the jar height`. Tỉ lệ ghi bằng số, không bằng tính từ.
- `[STATE_AXIS]` — trục trạng thái xuyên chuỗi: vd `K1-K4 raw, K5 heat on, K6 boiling, K7 served`. Mỗi frame chỉ lùi 1 trạng thái so với frame sau nó.
- `[CAMERA]` — keyframe: khóa cỡ cảnh + góc máy (`top-down fisheye`, `close-up 45-degree`); clip: 1 camera move chuẩn H3 nguyên cụm (`pushes in with small amplitude at slow speed`, `first-person POV hyperlapse`, `whips right`) + timestamp `[Shot N] At MM:SS.mmm` nếu nhiều nhịp.
- `[MOTION]` — đúng 1 động tác tịnh tiến, viết mềm: vd `sauce pours gently in a thin continuous stream`, `background aisles streak into motion blur while the cart stays sharp`. Cấm từ mạnh (`slams`, `burst`) — tra `docs/nsfw-filter-words.md` trước khi gen.
- `[ATMOSPHERE]` — hơi/khói/sáng: vd `fine mist and warm steam drift upward`, `lighting shifts cool freezer to warm checkout`. Mỗi prompt 1 subject motion + 1 camera move + 1 atmosphere.
- `[LOCK_NEGATIVE]` — khóa kênh đứng yên + cấm morph/chữ: vd `no morphing of bottle or pot, labels hold readable, no text except SK logo, blank label otherwise`.
- `[DURATION_SEC]` — clip thường 5s; timelapse qua địa điểm phải 8–10s (dựng hình + lướt + đáp mới kịp).

## Biến thể (tối đa 3, vẫn tiếng Anh)

1. T1 Hyperlapse push (timelapse qua địa điểm — khuyên dùng):
```text
First-person POV hyperlapse, single unbroken take, no cut, no dissolve. [PRODUCT] stays locked in the lower foreground, [LOCK_NEGATIVE]. The camera pushes in with large amplitude at fast speed; background streaks into motion blur while [PRODUCT] stays sharp; [ATMOSPHERE]; the move converges on the end frame and holds sharp for the last second. [DURATION_SEC].
```

2. T2 Whip-occluder (dự phòng khi T1 morph nhãn/biển):
```text
Single unbroken take. The camera pushes toward [PRODUCT], midway whips right so [PROP_LIST, e.g. freezer glass edge / checkout sign] fills the frame with directional blur for half a second, then reveals the new location and settles sharp on [END_FRAME]. [LOCK_NEGATIVE].
```

3. T3 Speed-ramp 3 nhịp (muốn nhịp chậm–nhanh–chậm rõ):
```text
[Shot 1] Slow establish on [END_FRAME] for 1s. [Shot 2] At 00:01.000 rapid rush: [MOTION] at fast speed with motion blur. [Shot 3] At 00:06.500 settle sharp on [END_FRAME]. [LOCK_NEGATIVE].
```

## Quy trình chạy kèm (tiếng Việt — tóm tắt để test)

1. Trả lời kịch bản sơ lược trước, user duyệt mới chạy (quy tắc session 2026-09-29).
2. Test clip biến hình lớn nhất trước; text-to-video 5s test nhịp trước khi kẹp 2 đầu.
3. So kèo model cùng ref + cùng setting; mixed theo frame (MS giữ scene/màu, Grok giữ vật thể — việc cần chính xác bao bì/nguyên liệu chọn Grok, có đủ 3 ref + prompt chuẩn thì MS thắng).
4. Stop-loss 3 gen/clip; mỗi lần đổi đúng 1 biến. Không edit nối quá 1 vòng trên ảnh AI — rớt thì gen mới từ ref thật.
