# Genjutsu Motion Transfer — playbook control (không đốt gen)

> Mục tiêu: mọi lỗi chặn được ở tiền kỳ $0, gen trả tiền chỉ để chốt.
> Giá: $0.318/s (480p) · $0.681/s (720p) · $1.632/s (1080p), làm tròn lên từng giây. Clip 10s 720p ≈ $6.8/gen.

## 1. Audit ảnh ref (miễn phí, quyết định 70% mặt có morph không)

- [ ] 2–3 ảnh cùng người, khác góc (chính diện + 3/4 + nghiêng), biểu cảm trung tính
- [ ] Ánh sáng ref giống ánh sáng clip nguồn (ngày/đêm, ấm/lạnh)
- [ ] Mặt ref rõ, không kính râm/khẩu trang/bóng đổ nửa mặt
- [ ] Không dùng 1 ref duy nhất cho clip >5s
- [ ] Prompt neo mặt viết sẵn: tuổi, tóc, áo, đặc điểm nhận dạng (1 dòng EN)

## 2. Audit video nguồn (ffmpeg local, miễn phí)

- [ ] Cắt đoạn ≤5s, chỉ giữ đoạn mặt nhìn rõ ≥80% thời lượng
- [ ] Bỏ đoạn quay đầu gắt, che mặt, mặt <10% khung hình
- [ ] Motion quá nhanh → giảm kỳ vọng hoặc cắt ngắn hơn (model giữ motion tốt nhưng mặt trả giá)
- [ ] Kiểm tra: `ffprobe` độ phân giải/duration trước khi upload (tránh up nhầm file nặng)

## 3. Thang test (rẻ → đắt, dừng khi đạt)

1. **Draft motion 480p, 2–3s** (~$1): chỉ xem motion/camera có đúng không, KHÔNG chấm mặt
2. **Test mặt 720p, 2–3s** (~$1.4–2): đoạn mặt khó nhất, chấm morph
3. **Final 720p full đoạn** (đã trừ 2 bước trên): chỉ chạy khi 1+2 đạt

## 4. Triage khi morph (không chạy lại mù)

| Triệu chứng | Nguyên nhân likely | Sửa $0 trước |
|-------------|-------------------|--------------|
| Mặt biến dạng ngay giây đầu | Ref khác xa frame đầu | Đổi ref giống góc/ánh sáng frame đầu |
| Mặt đẹp đầu clip, trôi dần | Clip dài + drift | Cắt ngắn, neo prompt mặt |
| Mặt nát khi quay đầu | Che khuất/không bám được | Cắt bỏ đoạn đó hoặc che bằng cắt cảnh ở dựng |
| Mặt bệt/mất chi tiết | Resolution thấp | Lên 720p (đừng chấm mặt ở 480p) |
| Đổi ref 3 lần vẫn morph | Model limit với ca này | Chấp nhận + vòng edit-frame-hỏng/ráp (không gen tiếp) |

## 5. Quy tắc dừng (stop-loss)

- Tối đa **3 gen trả tiền/ca**: 1 draft + 1 test + 1 final. Quá 3 mà chưa đạt → dừng, đổi phương án (cắt cảnh, edit frame, đổi model) thay vì gen tiếp.
- Mỗi gen ghi vào `workflows/higgsfield/INDEX.md` kèm cost ước tính để thấy tiền chảy đi đâu.
