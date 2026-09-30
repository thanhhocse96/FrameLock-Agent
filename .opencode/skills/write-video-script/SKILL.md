---
name: write-video-script
description: Write a commercial video script (keyframes + clips) from the 7 journal-proven methods, present a brief script for user approval before running, and test cheap-to-expensive. Use when viet kich ban video, script video quang cao, timelapse, or planning a new production.
metadata:
  version: "1.0.0"
  updated: "2026-09-30"
---

# Write Video Script

Viết kịch bản video thương mại theo 7 cách đã chứng minh trong `journal/`. Kịch bản trước, chạy sau.

## Khi nào dùng

- Yêu cầu mới về video (quảng cáo sản phẩm, timelapse, chuỗi clip) → viết kịch bản sơ lược, user duyệt mới chạy (quy tắc session 2026-09-29, xem `journal/2026-09-29-cart-video-timelapse-note.md`).
- Có draft sẵn: `templates/drafts/video-script-commercial-9x16.md` — fill biến theo đó.

## 7 bước (mỗi bước 1 cách trong journal)

1. **Neo-cuối–sinh-lùi** (`journal/2026-09-28-keyframe-splitting.md` §1): chốt frame cuối (packshot đủ prop) trước, sinh lùi từng frame, frame nào cũng ref frame sau + neo gốc. Design trục trạng thái (sống→chín) cho cả chuỗi.
2. **Khóa kỹ thuật trong prompt** (splitting §2–3 + `journal/2026-09-29-master-soche-fail-log.md` §2): khóa camera (`fisheye`, `top-down`), tỉ lệ bằng số, vật liệu ghi cặp khẳng–phủ (`opaque white foam, NOT transparent plastic`).
3. **Viết mềm motion** (retro pitfall 6): `pours gently`, `fine mist`; tra `docs/nsfw-filter-words.md` trước khi gen.
4. **Một clip một động tác** (splitting §8–9): tách motion tịnh tiến; morph bắt buộc thì giấu trong dòng đặc/bọt/hơi hoặc cắt ở dựng.
5. **Ngữ pháp H3 kẹp 2 đầu** (cart note §1): dòng neo ảnh + `[Shot N] At MM:SS.mmm`; 1 subject motion + 1 camera move + 1 atmosphere; khóa kênh đứng yên bằng phủ định nêu tên.
6. **Chọn cách nối timelapse** (cart note §2–3): T1 hyperlapse-push (mặc định) → T2 whip-occluder → T3 speed-ramp; clip qua địa điểm 8–10s, không 5s.
7. **So kèo + stop-loss** (retro §5 + cart note §4): cùng ref + cùng setting, mixed theo frame; test clip khó nhất trước; stop-loss 3 gen/clip, mỗi lần đổi 1 biến; không edit nối quá 1 vòng trên ảnh AI.

## Trình tự phiên làm việc

1. Đọc yêu cầu → trả lời **kịch bản sơ lược** (mốc frame, clip, công thức T1/T2/T3, ước tính request + chi phí từ `journal/analytics-models-db.csv`).
2. User duyệt → giao `higgsfield-run` chạy (prompt EN từ draft đã fill, key từ env, sản phẩm vào `.local/work/`).
3. Rớt/clip đạt → ghi fail-log vào `journal/`; insight thành luật → promote sang `.context/PITFALLS.md` hoặc `docs/`.
4. Output tốt → promote theo pipeline: `research/*/raws/` → `make-digest` → mapping → `make-template` merge draft thành template chính.
