# Note — template SeedDance "barrel-roll + hourglass" cho motion tốc độ thường (chờ gom thêm prompt)

- Ngày: 2026-10-06
- Trạng thái: phân tích sơ bộ từ 1 fragment do user cung cấp (bản thiếu, có `...`); **chưa làm raw/digest/mapping** — đợi user tổng hợp thêm prompt rồi làm chuyên sâu.
- Thiếu để đủ điều kiện vào pipeline: nguồn (kênh/influencer nào), URL prompt gốc, ngày thu thập, model SeedDance cụ thể (PITFALLS #1 — chưa có thì digest sẽ mồ côi).

## Fragment gốc (user cung cấp 2026-10-06, giữ nguyên)

```
IMPORTANT FINAL COMPOSITION:Near the end, his face ...
frame. This means his body position is shifted to the right side ...


The black sand must fall smoothly and continuously ...
flickering particles, no warped sand, no sudden jumps.


CAMERA MOTION
Mandatory visible barrel roll. Start upside down at 180 degre...
reversal. No counter-roll. No wobble. No sudden switch ...


CHARACTER MOTION AND POSITION
The referenced man walks into frame naturally from deep ...
perspective depth, then smoothly bends down ...
...
Near the end, place his face and upper ...


SAND MOTION
The black sand stream should be ...


LIGHTING
Minimal dark background. The man ...


AUDIO
No audio. Silent video. No music.


MOTION DESCRIPTION
The hourglass stays in the foreground ...
hourglass with natural visible st...
```

## Phân tích sơ bộ — vì sao nó ra tốc độ thường, mượt, không slowmotion

### 1. Lấp đầy toàn bộ thời lượng bằng staged blocking (giả thuyết chính)

Prompt chia motion thành các mốc chiếm hết clip: đi vào từ sâu (deep background + perspective depth) → cúi xuống → mặt/upper body vào vị trí chốt gần cuối. Model không còn "thời gian rảnh" để drift chậm — mỗi giây đều có việc phải làm. Đối lập với prompt yếu kiểu `smooth glide` (đúng bệnh clip cart cũ của repo: `smooth forward glide, steady cam` → model hiểu là trôi chậm — xem `journal/2026-09-29-cart-video-timelapse-note.md`).

### 2. Camera move biên độ lớn, định lượng, bắt buộc hoàn thành trong clip

`Mandatory visible barrel roll. Start upside down at 180 degre...` — xoay 180°→0° là quãng đường dài, buộc model tiêu hao time-budget vào motion thật thay vì nội suy chậm. Kèm negatives khóa đúng artifact của roll: `no reversal, no counter-roll, no wobble, no sudden switch`. Cùng họ với công thức T1 hyperlapse của repo (`large amplitude at fast speed`).

### 3. Khóa end-frame bằng FINAL COMPOSITION

Ép bố cục cuối (mặt + upper body, body lệch phải) = neo thời gian cuối clip. Tương đương triết lý "kẹp 2 đầu" của repo: có đích đến rõ thì nội suy ít lang thang. Đặt section này lên ĐẦU prompt (`IMPORTANT ... Near the end`) — có thể là trick thứ tự ưu tiên.

### 4. Foreground anchor + nền tối giản

`The hourglass stays in the foreground` + `Minimal dark background` = ít pixel phải animate → ít morph/warp → mượt. Cùng nguyên lý "foreground neo cứng + background streak" trong note timelapse (paper hyperlapse: stabilize + skip frame).

### 5. Negatives nhắm đúng artifact slow-mo/morph

`no flickering particles, no warped sand, no sudden jumps` — khóa 3 lỗi điển hình khi model kéo dài motion: nhấp nháy, biến dạng, nhảy cóc. SAND MOTION riêng một section vì cát là particle system dễ flicker nhất.

### 6. Khóa kênh không dùng

`AUDIO: No audio. Silent video. No music.` — tắt hẳn 1 kênh để model không phân bổ capacity lung tung (SeedDance có sinh audio; H3 của mình không audio nên điểm này không transfer).

### 7. Cấu trúc section ALL-CAPS = khung template sẵn

7 section (FINAL COMPOSITION / SAND / CAMERA / CHARACTER / LIGHTING / AUDIO / MOTION DESCRIPTION) — mỗi section 1 mối quan tâm, dễ chuyển thành biến `UPPER_SNAKE` (`[CAMERA_MOVE]`, `[SUBJECT_BLOCKING]`, `[NEGATIVES]`) khi forge template sau này (D-003).

## Câu hỏi mở (trả lời khi làm chuyên sâu)

1. Toàn văn prompt là gì (phần `...` bị cắt)? Đặc biệt câu barrel roll đầy đủ + MOTION DESCRIPTION.
2. Model SeedDance bản nào, clip dài bao nhiêu giây, single-shot hay có cut?
3. Có dùng start/end frame không, hay text-to-video thuần? (quyết định transfer được sang H3 kẹp 2 đầu hay không)
4. Tốc độ "bình thường" có đo được không (so với slow-mo cũ của mình observer-blind hay có metric)?
5. Các prompt sắp gom có cùng họ section này không, hay mỗi người một kiểu?

## Việc tiếp theo (khi user gom đủ)

1. Mỗi prompt → `research/videos/raws/<slug>.md` (đủ nguồn + URL + ngày, invariant raw bất biến).
2. Mỗi raw → digest theo schema `.context/modules/research-videos.md` (trọng tâm: động từ motion giữ EN, mục Cấu trúc thời gian).
3. Mỗi digest → 1 dòng `research/videos/mapping.md`.
4. So pattern lặp (staged blocking? quantified camera? end-composition lock?) → forge template từ `templates/drafts/` → merge khi fill-test được từ ≥1 digest thật.
5. Test transfer rẻ→đắt trên H3/MiniMax: text-to-video 5s trước, kẹp 2 đầu sau (stop-loss 3 gen).
