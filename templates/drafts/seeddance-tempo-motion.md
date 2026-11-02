# Template: Staged motion tốc độ thường — khóa end-frame + camera biên độ lớn (draft video, chưa test)

> DRAFT — chưa dùng được. Giữ `drafts/`, không list trong `Index.md`.
> - Nguồn pattern: `journal/2026-10-06-seeddance-tempo-note.md` (phân tích 1 fragment SeedDance, chưa có `research/videos/digests/` thật → giữ draft theo PITFALLS #6).
> - Lưu ý D-010 (image-only): đây là draft **video** nằm nhờ trong `drafts/` hiện có — không tạo nhánh `templates/videos/`. Muốn promote phải có digest video thật + fill-test pass + quyết định mở lại nhánh video.
> - Chưa fill-test từ digest thật. Ví dụ dưới fill minh họa từ fragment hourglass (không phải digest).

- Dùng cho: video — motion clip tốc độ thường, mượt, không slowmotion (single continuous shot, có subject + particle + camera move lớn)
- Nguồn pattern: `journal/2026-10-06-seeddance-tempo-note.md`
- Biến (EN `UPPER_SNAKE`): `[FINAL_COMPOSITION]`, `[SUBJECT_BLOCKING]`, `[CAMERA_MOVE]`, `[CAMERA_NEGATIVES]`, `[PARTICLE_MOTION]`, `[PARTICLE_NEGATIVES]`, `[FOREGROUND_ANCHOR]`, `[BACKGROUND]`, `[LIGHTING]`, `[AUDIO_LOCK]`, `[MOTION_SUMMARY]`

## Prompt mẫu (tiếng Anh, fill sẵn 1 ví dụ minh họa — chưa phải digest thật)

```text
IMPORTANT FINAL COMPOSITION: Near the end, his face and upper body fill the right half of the frame in sharp focus. This means his body position is shifted to the right side of the frame for the entire shot.

The black sand must fall smoothly and continuously from the upper bulb to the lower bulb in one unbroken stream, no flickering particles, no warped sand, no sudden jumps.

CAMERA MOTION
Mandatory visible barrel roll. Start upside down at 180 degrees and roll steadily to upright 0 degrees across the full clip duration, single continuous rotation with no reversal. No counter-roll. No wobble. No sudden switch.

CHARACTER MOTION AND POSITION
The referenced man walks into frame naturally from deep background with correct perspective depth, then smoothly bends down toward the hourglass. Near the end, place his face and upper body on the right side of the frame, leaning in to observe the sand.

SAND MOTION
The black sand stream should be dense, continuous and evenly paced from the first second to the last, falling straight down with fine grains clearly visible.

LIGHTING
Minimal dark background. The man is lit by a single soft key light from the front-left, gentle falloff into darkness, cinematic contrast.

AUDIO
No audio. Silent video. No music.

MOTION DESCRIPTION
The hourglass stays in the foreground, locked in position, with natural visible streaming sand throughout the whole shot.
```

## Prompt kết quả khi gen (tiếng Anh — bắt buộc, không dịch sang Việt)

```text
IMPORTANT FINAL COMPOSITION: [FINAL_COMPOSITION].

[PARTICLE_MOTION], [PARTICLE_NEGATIVES].

CAMERA MOTION
[CAMERA_MOVE]. [CAMERA_NEGATIVES].

CHARACTER MOTION AND POSITION
[SUBJECT_BLOCKING].

LIGHTING
[LIGHTING]. Background: [BACKGROUND].

AUDIO
[AUDIO_LOCK].

MOTION DESCRIPTION
[FOREGROUND_ANCHOR]. [MOTION_SUMMARY].
```

## Cách fill biến (tiếng Việt)

- `[FINAL_COMPOSITION]` — bố cục khung cuối, ghi vị trí + độ nét: vd `Near the end, his face and upper body fill the right half of the frame in sharp focus`. Luôn đặt lên đầu prompt. Không ghi chung chung `nice ending`.
- `[SUBJECT_BLOCKING]` — chuỗi hành động lấp đầy toàn bộ thời lượng, mốc nối mốc: vd `walks into frame naturally from deep background with correct perspective depth, then smoothly bends down toward the hourglass`. Mỗi giây phải có việc — đây là biến chống slowmotion chính.
- `[CAMERA_MOVE]` — 1 camera move duy nhất, biên độ lớn + định lượng + bắt buộc hoàn thành trong clip: vd `Mandatory visible barrel roll. Start upside down at 180 degrees and roll steadily to upright 0 degrees across the full clip duration`. Quy tắc 1 move/prompt (nhồi nhiều là mờ).
- `[CAMERA_NEGATIVES]` — khóa artifact của đúng move đó: vd `No counter-roll. No wobble. No sudden switch`. Move nào thì negatives của move đó (roll → reversal/counter-roll; push → morph/jump).
- `[PARTICLE_MOTION]` — dòng chảy liên tục từ giây đầu tới giây cuối: vd `The black sand must fall smoothly and continuously from the upper bulb to the lower bulb in one unbroken stream`.
- `[PARTICLE_NEGATIVES]` — khóa 3 lỗi particle: vd `no flickering particles, no warped sand, no sudden jumps`.
- `[FOREGROUND_ANCHOR]` — vật neo cứng tiền cảnh, cấm di chuyển: vd `The hourglass stays in the foreground, locked in position`. Nền càng tối giản càng ít morph.
- `[BACKGROUND]` — nền tối giản để giảm pixel phải animate: vd `Minimal dark background`.
- `[LIGHTING]` — 1 key light + hướng + tương phản: vd `single soft key light from the front-left, gentle falloff into darkness`.
- `[AUDIO_LOCK]` — khóa kênh audio (model có sinh audio mới cần): vd `No audio. Silent video. No music.` H3 không audio thì bỏ biến này khi transfer.
- `[MOTION_SUMMARY]` — 1 câu tóm tắt neo toàn shot: vd `natural visible streaming sand throughout the whole shot`.

## Biến thể (tối đa 3, vẫn tiếng Anh)

1. Không particle (chỉ subject + camera — khi cảnh không có dòng chảy/hạt):
```text
IMPORTANT FINAL COMPOSITION: [FINAL_COMPOSITION].

CAMERA MOTION
[CAMERA_MOVE]. [CAMERA_NEGATIVES].

CHARACTER MOTION AND POSITION
[SUBJECT_BLOCKING].

LIGHTING
[LIGHTING]. Background: [BACKGROUND].

AUDIO
[AUDIO_LOCK].

MOTION DESCRIPTION
[FOREGROUND_ANCHOR]. [MOTION_SUMMARY].
```

2. Camera tĩnh, chỉ subject + particle động (test rẻ — loại trừ biến camera khi bị wobble/morph):
```text
IMPORTANT FINAL COMPOSITION: [FINAL_COMPOSITION].

[PARTICLE_MOTION], [PARTICLE_NEGATIVES].

CAMERA MOTION
Static locked-off camera, no movement, no shake, no drift.

CHARACTER MOTION AND POSITION
[SUBJECT_BLOCKING].

LIGHTING
[LIGHTING]. Background: [BACKGROUND].

AUDIO
[AUDIO_LOCK].

MOTION DESCRIPTION
[FOREGROUND_ANCHOR]. [MOTION_SUMMARY].
```

3. Speed-ramp 3 nhịp (khi muốn nhịp nhanh-chậm rõ thay vì đều — cùng họ T3 trong note timelapse):
```text
IMPORTANT FINAL COMPOSITION: [FINAL_COMPOSITION].

CAMERA MOTION
[CAMERA_MOVE] with speed ramp: slow establish for the first second, rapid main move through the middle, settle sharp in the final second. [CAMERA_NEGATIVES].

CHARACTER MOTION AND POSITION
[SUBJECT_BLOCKING].

LIGHTING
[LIGHTING]. Background: [BACKGROUND].

AUDIO
[AUDIO_LOCK].

MOTION DESCRIPTION
[FOREGROUND_ANCHOR]. [MOTION_SUMMARY].
```

## Điều kiện promote (để nguyên tới khi đủ)

1. Gom đủ prompt thật → raw (`research/videos/raws/`, đủ nguồn + URL + ngày) → digest (schema module research-videos, động từ motion giữ EN) → 1 dòng `research/videos/mapping.md`.
2. Fill thử template này từ ≥1 digest thật, dán kết quả khi duyệt.
3. Pass → quyết định mở lại nhánh video (sửa D-010) rồi mới move ra khỏi `drafts/` + index.
