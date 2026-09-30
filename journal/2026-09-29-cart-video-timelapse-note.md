# Note — cart video tua nhanh qua các địa điểm (chưa làm)

- Ngày: 2026-09-29
- 3 cụm mốc đã chốt/chờ: `v1-dim` (đông lạnh) → `v4-checkout` (quầy Co.op) → `v5-trunk` (bãi xe cốp mở)
- 2 clip đã chạy (smooth glide, chưa đúng ý): `clipA-v1-v4-retry` (5.4MB), `clipB-v4-v5` (5.2MB)
- Quy tắc session (user chốt 2026-09-29): yêu cầu mới → **trả lời kịch bản sơ lược trước, user duyệt mới chạy** (đã ghi vào `workflows/higgsfield/README.md` bước 0).

## Yêu cầu user (note lại, chưa làm)

- Phong cách video: **tua nhanh (timelapse / fast-forward)**, đi qua các địa điểm khác nhau.
- Hiện tại clip chỉ là glide mượt chậm — sai nhịp, sai năng lượng.
- Cần nghiên cứu thêm cách viết prompt timelapse cho MiniMax H3 image-to-video kẹp 2 đầu.

## Kết quả research chuyên sâu (2026-09-29)

Nguồn chính: MiniMax H3 Prompt Guide chính thức (minimaxh3.co/prompt-guide, cập nhật 08/2026) + HuggingFace `VIDEO_PROMPT_WRITING_GUIDE` + case Kling O1 timelapse + Runway/Adobe/Artlist/Morphic + paper hyperlapse (Microsoft Research) + playbook `genjutsu-control.md` của repo.

### 1. Cấu trúc prompt đúng cho H3 kẹp 2 đầu (FL2VA)

- Script repo chỉ gửi 1 chuỗi `prompt`, nhưng nên viết theo ngữ pháp chính thức: dòng neo ảnh trước, rồi timeline `[Shot 1]` (không timestamp) + `[Shot N] At MM:SS.mmm` cho các nhịp sau. FL2VA hợp nhất với **single continuous shot** — đúng POV đẩy xe của mình.
- Từ vựng camera chuẩn (dùng nguyên cụm): `Push In / Pull Out / Truck / Pedestal / Pan / Tilt / Arc / Tracking / POV` + biên độ (`with small/large amplitude`) + tốc độ (`at slow/fast speed`). Clip cũ ghi `smooth forward glide, steady cam` là từ vựng yếu — model hiểu là trôi chậm.
- Quy tắc Adobe/Runway: **1 subject motion + 1 camera move + 1 atmosphere** mỗi prompt; nhồi nhiều là mờ. Khóa kênh không muốn động bằng câu phủ định nêu tên (vd `the cart holds steady, only the background rushes`).

### 2. Mâu thuẫn cốt lõi: kẹp 2 đầu × tua nhanh × khác địa điểm

- FL2VA mặc định nội suy mượt giữa 2 frame. Ép `fast` mà không cho "cầu nối" thì model nhảy cóc/morph nhãn (đúng lỗi sợ mất chữ `CÁ MÚ`, biển hiệu).
- 3 cách nối đã được chứng minh (Morphic + Artlist + Kling):
  a. **Hyperlapse push + motion-blur bridge (khuyên dùng):** xe khóa cứng tiền cảnh dưới, nền chảy streak, hội tụ về end frame, 1s cuối giữ nét.
  b. **Whip-pan qua vật che (occluder):** push → quật ngang blur ở giữa (mép tủ đông / biển hồng / nắp cốp lấp đầy khung ~0.5s) → lộ địa điểm mới → settle.
  c. **Speed-ramp 3 nhịp:** chậm 1s dựng hình → nhanh 3s lướt → chậm 1s đáp (ghi timestamp rõ).
- Case Kling O1 chứng minh cụm `Create a magical timelapse transition... melts rapidly... lighting shifts... camera pushes in slowly` chạy được trong prompt kẹp 2 frame — thay nội dung bằng hành trình của mình là dùng được.
- Paper hyperlapse: bản chất là stabilize + skip frame; tương đương AI là **foreground neo cứng + background streak**. Xe + gói hàng là neo, cấm morph chữ.

### 3. Công thức prompt đề xuất (giữ 3 frame mốc, clip 8-10s thay vì 5s)

- 5s quá ngắn cho tua nhanh qua địa điểm (dựng hình + lướt + đáp không kịp) → đề xuất **8-10s** (H3 hỗ trợ 5-15s, $0.13/s → clip 10s ≈ $1.30).
- T1 Hyperlapse push (dùng cho cả 2 clip): `First-person POV hyperlapse, single unbroken take, no cut, no dissolve. The blue-handle cart with frozen fish packs stays locked in the lower foreground, labels hold readable, no text morphing. The camera pushes in with large amplitude at fast speed; background aisles/lights streak into motion blur while the cart stays sharp; lighting shifts [cool freezer → warm checkout / indoor → daylight parking]; the move converges on the end frame and holds sharp for the last second.`
- T2 Whip-occluder (dự phòng khi T1 morph): thêm `midway the camera whips right, [freezer glass edge / pink checkout sign / trunk lid] fills the frame with directional blur for half a second, then reveals the new location`.
- T3 Speed-ramp (nếu muốn nhịp rõ): `[Shot 1] slow establish 1s → [Shot 2] At 00:01.000 rapid rush → [Shot 3] At 00:06.500 settle sharp`.

### 4. Kế hoạch test rẻ → đắt (theo playbook genjutsu, stop-loss 3 gen/clip)

1. Text-to-video 5s test từ khóa tua nhanh (không ref, ~$0.65) — chỉ chấm nhịp/blur.
2. Clip A-timelapse 8s công thức T1 — chấm morph nhãn + đáp end frame.
3. Clip B-timelapse 8s công thức T1 — tương tự.
4. Rớt mới đổi sang T2/T3, mỗi lần đổi 1 biến duy nhất.
5. H3 không audio — SFX whoosh + nhạc tua nhanh làm ở dựng.

### 5. Rủi ro đã biết trước

- Chữ `CÁ MÚ`/biển `QUẦY TÍNH TIỀN` dễ chảy khi rush → mitigation: `labels hold readable` + biển nền để mờ có chủ ý + 1s cuối nét.
- End-frame exactness vs motion blur là trade-off — nếu T1 vẫn nhảy cóc, cân nhắc reference-to-video (đắt hơn) thay vì kẹp cứng 2 đầu.
