# Note — transition qua cỡ cảnh khác nhau trong clip gen (2026-10-06)

> Vấn đề: first và last frame khác cỡ cảnh (vd medium 1.5 → tight Frame-2). Kẹp + camera static = clip rời rạc (đã chứng minh ở `2026-10-06-kling-f15-f2-3s`). Đây là bài toán TRANSITION, thảo luận trước khi sinh.
> Liên quan: `templates/drafts/video-script-commercial-9x16.md` (T1/T2/T3), `journal/2026-09-29-cart-video-timelapse-note.md` (kẹp 2 đầu × chuyển cảnh).

## Nguyên tắc

- Cùng cỡ cảnh + 1 động tác nhỏ → kẹp 2 đầu static được (vd 1.5→1.5-variation).
- Khác cỡ cảnh → prompt BẮT BUỘC có camera movement nối 2 scale + duration dài hơn (5-8s, không phải 3s). Static + khác scale = fail chắc.

## 3 cách đã có trong repo (chọn trước khi sinh)

### T1. Push-in hội tụ (khuyên dùng cho 1.5→2)
- Camera `pushes in with large amplitude` từ medium về tight, converge đúng end frame, 1s cuối giữ nét.
- Action (xẻng luồn) xảy ra GIỮA đường push, không phải lúc đầu.
- Duration 5-8s (3s không kịp vừa push vừa action). Prompt phải có câu neo đích: `the move converges on the end frame and holds sharp for the last second`.
- Áp cho: A1→A2, mọi cặp medium→tight.

### T2. Whip/zoom-blur qua điểm che
- Push → giữa đường whip nhanh (blur 0.5s, vật che = mép chảo/thớt) → lộ scale mới → settle.
- Dùng khi T1 morph (mặt/xẻng méo giữa đường). Đánh đổi: mất 0.5s nội dung.

### T3. Cắt ở dựng (không nối trong AI)
- 2 clip 1-frame rời + hard cut/match cut ở CapCut. A1 rộng → cắt → A2 tight chính là punch-in tự nhiên.
- Dùng khi: khác scale + khác góc + thêm/bớt vật cùng lúc (vượt khả năng nội suy). Đây là phương án đang dùng cho cả chuỗi bếp.

## Ma trận chọn (dán vào brief trước khi sinh)

| first → last | Cùng scale? | Thêm/bớt vật? | Cách | Duration |
|---|---|---|---|---|
| 1.5 → 2 (A2) | Không (medium→tight) | Có (xẻng) | T1 push-in 5-8s, hoặc T3 cắt | 5-8s / 3+3s |
| A1 → A1-var | Có | Không | Kẹp static 3s | 3s |
| A2 → A3 | Không (tight→K2-angle) | Không | T1 push-out hoặc T3 cắt | 5-8s / 3+3s |
| K2 → P1 | Không (góc + bố cục) | Có (đĩa/thớt) | T3 cắt (không kẹp) | 3+3s |

## Quy tắc viết prompt kẹp khác scale (checklist)

1. Có camera move nêu tên + biên độ (`pushes in with large amplitude at slow speed`).
2. Có câu neo đích (`converges on the end frame... holds sharp for the last second`).
3. Action đặt GIỮA timeline, không dồn đầu clip.
4. Duration 5-8s. 3s chỉ cho cùng-scale.
5. Stop-loss 3 gen, mỗi lần đổi 1 biến (đầu tiên luôn là thêm/bớt camera move).
6. Vật ra/vào BẰNG MÉP KHUNG — ghi rõ mép nào (user 2026-10-06, xem dưới).
7. Hành động không quan trọng thì ĐẨY RA NGOÀI KHUNG, không cho vào clip (user dạy 2026-10-06: cất xẻng không cần show — tay mang xẻng ra mép là xong, khỏi tốn motion, khỏi morph).

## Kết quả test nối 2→3 (fail toàn diện, chốt 2026-10-06)

- Kling O3 6s static + timestamp T3 → fade (pull rồi nhảy cảnh).
- Seedance 2.0 6s FPV 1-take (bỏ nhãn Shot, cấm fade, constant velocity, blocking mép trên) → VẪN FADE.
- Kết luận: multi-change clamp (đổi scale + đổi tay/vật) fail trên mọi model đã thử, bất kể văn phong. Kẹp AI chỉ dùng cho 1 thay đổi (cùng scale + 1 motion, hoặc camera-only). Mọi cặp multi-change → T3 cắt ở dựng, không đốt thêm request test.

## Nguyên lý ra/vào bằng mép khung (user phát hiện 2026-10-06)

- Mọi vật biến mất/xuất hiện phải đi qua mép khung theo camera move (tay cầm xẻng trôi ra mép khi push-in, tay rắc vào từ mép trên khi pull-back) — KHÔNG cho vật tự tan/biến giữa khung (morph, model dở nhất).
- Model làm được vì đây chỉ là camera move + vật tĩnh/động tịnh tiến, không đổi topology.
- Giới hạn: mép khung không giải quyết được (a) vật biến hình trong khung (cá sống→vàng — giấu bằng "time passes" trong lúc push), (b) đổi góc nhìn (3→4 low-front sang side — mép không xoay được góc, cần arc hoặc cắt), (c) vật phải xuất hiện giữa khung (tránh bằng staging: đặt sẵn ngoài khung rồi reveal).
