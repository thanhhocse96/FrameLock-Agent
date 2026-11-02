# Retro — chuỗi stock bếp IQF grouper (Flux 1K, 2026-10-06)

> 12 runs `black-forest-labs/flux-3-image` 1K (~$0.288): 10 đạt (pack vợ 25 ×4, pack chồng ×4 trừ gốc cũ, bếp K2/A1/A2/A3/P1), 2 rớt (T1 serve ×2 — nhân đôi vợ).
> Log runs: `workflows/openrouter/INDEX.md`. Refs: `.local/work/openrouter/ref-*-768.jpg` + `Ref/` (screenshot YouTube, chỉ nội bộ).

## 1. Lỗi prompt (chữ)

| # | Lỗi | Biểu hiện | Fix đã chứng minh |
|---|-----|-----------|-------------------|
| P1 | Tuổi bằng chữ | `early 30s` → mặt ~50; `mid 30s` → mặt ~40 | Ghi số + phủ định già: `25-year-old ... smooth clear skin with no wrinkles` |
| P2 | Tả trạng thái thay vì motion | `have formed and expanded` → ảnh/video đứng hình | Hiện tại tiếp diễn + động từ mềm: `are expanding gently` |
| P3 | Thiếu khóa số người với 2 face ref | T1 nhân đôi vợ, take2 thêm `exactly one woman, no twins` vẫn dính | Khung 2 mặt + 2 face ref = vùng nguy hiểm; fix thật: bỏ ref mặt người thứ 2, tả chay bằng chữ |
| P4 | Thiếu khóa dụng cụ | Xẻng đỏ lơ lửng trên chảo không tay cầm (K2 bản đầu) | `every utensil is either held by a hand or out of frame, no floating utensils`; shot không trở → xẻng ra khỏi khung |
| P5 | Nhét ngôn ngữ video vào prompt ảnh | `single unbroken take, holds static` trong T2I | Bỏ khi gen ảnh; chỉ dùng khi kẹp clip |
| P6 | Claim sai vật lý | `tinh thể nhỏ hơn giọt nước` (nước nở ~9% khi đông) | `similar size, evenly distributed, membranes stay intact` |
| P7 | Ref screenshot mang logo | `no logo` giảm nhưng A3 vẫn dính 2 chấm tròn mờ góc | Crop 5% mép khi dựng, hoặc regen bỏ ref screenshot |

## 2. Lỗi bố cục (hình)

| # | Lỗi | Biểu hiện | Fix đã chứng minh |
|---|-----|-----------|-------------------|
| C1 | Tranh truyền thần | Chồng đứng nhìn thẳng vào máy trong bếp, cứng | Thân nghiêng candid qua bếp + tay là chủ thể + mặt nhòe/crop mép (A1) |
| C2 | Không design trục siết | Các shot nhảy cỡ cảnh lung tung | Khóa trục trước: A1 rộng (người+chảo) → A2 tight (chảo lấp khung) → A3 về góc K2 (thấy người) |
| C3 | Khung đối xứng + 2 face ref | T1 vợ hai bên giống hệt | Tránh đối xứng khi có 2 face ref; hoặc 1 người + 1 tả chay |
| C4 | Cặp so sánh khác scale | GPT-IQF vs GPT-Frozen khác độ phóng đại/mật độ | Cùng lưới + cùng scale, chỉ khác kích hốc đá |
| C5 | Hốc trắng đọc nhầm | Hốc đá trong tiêu bản dễ đọc thành mỡ/khuyết | Không để ảnh lab đứng một mình — nhãn mũi tên hậu kỳ |

## 3. Lỗi bối cảnh (context)

| # | Lỗi | Biểu hiện | Fix |
|---|-----|-----------|-----|
| B1 | Gam lab cho quảng cáo đồ ăn | Hồng H&E lạnh, không thèm ăn | Hero = đồ ăn thật ấm; lab chỉ cutaway 3-5s có voiceover |
| B2 | Wardrobe ref lệch pack | Screenshot YouTuber áo caro | Ref người/vật phải khớp pack đã khóa (thun xám, chảo đen, xẻng đỏ, bếp gas) |
| B3 | Loại bếp không khóa từ đầu | May mắn cả chuỗi đều bếp gas | Khóa `[KITCHEN]` trong template (gas/từ, tối/sáng) |
| B4 | Kỹ thuật chạy | (a) PowerShell ghi JSON BOM → `json.load` rớt; (b) ref base64 2MB treo request >300s | (a) Ghi no-BOM + đã patch 2 script `utf-8-sig`; (b) ref nén 768px JPEG ~85KB |

## 4. Quy tắc rút ra (đã đúc thành template)

`templates/images/kitchen-stock-continuity-16x9.md` — nguồn production 5 runs bếp đạt + 2 pack. Chờ merge: đề xuất thêm B4/P4/P3 vào `.context/PITFALLS.md` (user duyệt mới sửa, theo invariant governance).
