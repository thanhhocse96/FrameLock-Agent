# 2026-09-29 — Nhật ký gen master sơ chế: vì sao fail 5 round mới chốt

Chuỗi: MS v1 → MS v2 → MS v3 → MS v4 → MS v5 → Grok v1 → Grok v2 → Grok v3 (chốt) → final +tuyết → Soul v2 fill-test (rớt).

## 1. Edit nối trên ảnh AI gây drift cộng dồn (v3, v4)

- v3/v4 edit từ output v2 (ảnh AI, không phải ảnh thật). Mỗi vòng model quên dần ràng buộc gốc:
  v3 mất khay xốp, v4 cá trôi thành cá lạ + rớt khay xốp.
- Bài học: **gen mới từ đầu với ref thật** (v5) thay vì edit nối quá 1 vòng. Quy tắc: 1 edit nối không đạt → bỏ, gen mới.

## 2. Prompt thiếu phủ định vật liệu (v1–v4)

- Chỉ ghi `PP plastic tray` / `plastic tray` → model mặc định khay nhựa trong.
- Chốt ở v5 nhờ ghi `opaque white foam, NOT transparent plastic` + `SLIGHTLY BIGGER`.
- Bài học vào template: mọi vật liệu từng sai phải có cặp khẳng định + phủ định.

## 3. Ref cá thật nhưng model vẫn bịa (v4)

- v4 có ref `ca-duc-lam-sach.jpg` mà cá vẫn lạ → ref 1 mình không đủ khi ref chính (v2-AI) đã drift.
- Bài học: ref giữ vật thể chỉ hiệu lực khi ref giữ bố cục còn sạch. Cả 3 ref thật (v5) mới khóa được.

## 4. Túi càng lộ nhiều càng bịa chữ (Grok v3)

- Túi to hơn khay + lộ tem → model vẽ thêm huy hiệu tuyết + chữ Việt ngọng (không có trong ref).
- Chấp nhận vì chữ nhỏ; lần sau: hoặc lộ 1 phần tem, hoặc dí `blank label, no text except SK logo`.

## 5. Model khác không ref thua xa (Soul v2 fill-test)

- Cùng prompt template, Soul v2 text-only: cá còn đầu, túi đỏ/vàng sai, props thừa (đậu lăng, hũ lạ), không tuyết, fisheye yếu.
- Kết luận: **Grok + 3 ref thật > MS + ref > Soul text-only**. Template `SK_SALES_HERO_9x16` bắt buộc kèm ref (đã ghi trong file template).
- MS vs Grok: MS giữ scene/màu tốt nhưng nghe vật thể kém (khay, cá); Grok ngược lại — việc cần độ chính xác vật thể (bao bì, nguyên liệu) thì chọn Grok.

## 6. Bổ sung: MS + đủ 3 ref + prompt template thắng Grok (fill-test MS)

- Cùng prompt + cùng 3 ref như Grok v3, MS cho ra bản sạch nhất: fisheye mạnh, khay xốp,
  cá không đầu 2 hàng + tuyết, logo SK rõ mà KHÔNG bịa thêm chữ tem (Grok v3 bịa huy hiệu + chữ ngọng).
- Kết luận cập nhật: **MS + 3 ref + prompt chuẩn > Grok + 3 ref > MS thiếu ref.**
  Giả thuyết: MS giữ ref trung thành hơn khi prompt đã khóa chặt vật liệu (cặp khẳng định + phủ định);
  Grok sáng tạo hơn nên hay "vẽ tiếp" phần ref không có (chữ tem, đầu cá).
