# 2026-09-28 — Phương pháp tách cụm keyframe (chi tiết)

> Deep-dive của retro cùng ngày. Mỗi cụm frame là 1 section nhỏ: ý tưởng → pitfall → cách giải quyết → kết quả.

## 1. Ý tưởng gốc: neo cuối + sinh lùi

Thay vì sinh xuôi K1→K7 (frame sau trôi khỏi frame trước), chốt **frame cuối K7 trước** (packshot chứa đủ prop đã duyệt: nồi, chị, túi) rồi sinh lùi K6→K1, frame nào cũng ref vào frame sau nó (+ neo gốc K7 cho vật chủ chốt). Chuỗi giữ được vì mỗi bước chỉ lùi 1 trạng thái.

## 2. Cụm K7 — neo (3 lần thử)

- **Thử 1 (Soul text-only):** trật bố cục (thiếu top-down/fisheye). Nguyên nhân: prompt thiếu tả camera + model mù ref. Fix: viết lại prompt khóa camera — vẫn trật.
- **Thử 2 (Soul + prompt fisheye):** vẫn không bám ảnh ref. Kết luận: text-only không anchor được vào ảnh có sẵn.
- **Thử 3 (Grok + 2 refs composite/túi):** trúng. Bài học: **neo phải nhìn được ref** — model không nhận ảnh ref thì đừng giao việc giữ bố cục.
- Quyết định thêm: túi overlay hậu kỳ thay vì bắt AI vẽ (chữ lem), K7 Grok giữ túi ở cỡ vừa.

## 3. Cụm K1 tĩnh — 6 vòng lặp (v1→v6)

| Vòng | Lỗi | Fix |
|------|-----|-----|
| v1 | Chai lùn, khay nhựa cứng | Prompt `TALL`, khay `styrofoam polystyrene` + tỉ lệ `cao gấp đôi hũ` |
| v2–v3 | Cá còn đầu/mắt + bị nấu chín | Phát hiện nhiễm ref K7 (cá kho chín) → **bỏ ref K7**, thay ref `ca-duc-lam-sach.jpg` + khóa `RAW, uncooked, nothing cooked` |
| v4 | Chai lại lùn | Neo dáng chai vào K2 + tỉ lệ số học thay vì tính từ mơ hồ |
| v5→v6 | Hũ đậy nắp (video khó cuốn gia vị) | Mở nắp hũ — quyết định tiền-video: prop tĩnh phải ở trạng thái "sẵn sàng bay" |
| Bài học cụm | **Ref phải cùng trạng thái sống/chín** với frame cần gen; tả tỉ lệ bằng số, không bằng tính từ |

## 4. Cụm K2/K3 — cá sống xuyên suốt

- Phát hiện: K2/K3 đời đầu cá chín (nhiễm K7 như K1). Fix hàng loạt: ref cá sống + prompt `still raw`.
- Logic sống-chín chốt: K1→K4 cá sống, K5 bật bếp mới chín, K6 sôi, K7 dọn. **Trạng thái là 1 trục phải design**, không để model tự quyết.

## 5. Cụm K5 — vòng năng lượng (so kèo 2 model)

- Grok vs Marketing Studio cùng prompt + ref → MS thắng mảng tĩnh/bố cục. Cách so công bằng: cùng ref, cùng `2k`/`16:9`, 1 frame/mẫu.
- Kết quả mixed: MS cho đầu chuỗi (K1, K2), Grok cho cuối (K7) — **không trung thành 1 model**, frame nào lấy con mạnh nhất.

## 6. Cụm K6 — lỗi găng tay (MS)

- MS tự thêm găng tay bếp. Xử lý: bỏ qua có ghi nhận (không đốt request sửa lỗi nhỏ ở frame trung gian — frame trung gian chỉ sống 5s trong clip, lỗi nhỏ chìm trong motion).
- Luật: **lỗi frame trung gian < lỗi frame neo** — frame neo (K1, K7) sửa tới cùng, frame giữa chấp nhận 90%.

## 7. Cụm chuyển nền K3→K4 (tối→sáng)

- Vấn đề: K1–K3 nền đen, K4+ bếp sáng. 2 plan: (a) edit nền 3 frame, (b) beat chuyển ở khâu dựng.
- Chốt: **sweep theo hướng dòng rót + bloom từ vầng sáng K4** (12–15 frame, miễn phí ở CapCut). Lý do: có neo vật lý (vầng sáng), không tốn request, giữ chất cinematic nền đen của cảnh lốc.

## 8. Cụm clip 1 — tách motion (bài học đắt nhất)

- **Bản đầu (K1→K2 một clip):** morph hỏng — chai đứng thành chai nghiêng, đồ nằm thành đồ bay, méo hình giữa clip.
- **Sửa:** tách 1 động tác/clip — 1a bay lên + nắp bật, 1b rót + lốc, 1bc hũ hiện trong bọt, 1cd dĩa morph nồi (neo dòng chảy liên tục).
- Luật: **model giỏi motion tịnh tiến, dở morph biến hình**. Chỗ nào bắt buộc morph thì giấu trong dòng đặc/bọt/hơi, hoặc cắt ở khâu dựng.
- Phụ: prompt dính `slams`/`burst` → cờ nsfw → luật viết mềm + sổ `docs/nsfw-filter-words.md`.

## 9. Cụm clip 2v2 — giấu cá trong dòng

- Lỗi: lốc thành chảo, cá đổi hình (nhìn giả). Fix: dòng sốt **đặc đục**, cá chìm hẳn, chỉ lộ khi đã nằm yên trong nồi. Cùng họ với luật giấu-morph mục 8.

## 10. Checklist tái dùng production sau

1. Chốt frame cuối trước, sinh lùi, ref chuỗi + neo gốc.
2. Ref cùng trạng thái sống/chín; tả tỉ lệ bằng số.
3. 1 clip = 1 động tác; morph thì giấu hoặc cắt.
4. Test clip biến hình lớn nhất trước.
5. So kèo model cùng ref + cùng setting; mixed theo frame, không theo hãng.
6. Frame neo sửa tới cùng; frame giữa chấp nhận 90%.
7. Prompt motion viết mềm, tra sổ NSFW trước khi gen.
