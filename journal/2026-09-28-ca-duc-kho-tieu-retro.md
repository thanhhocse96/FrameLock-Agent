# 2026-09-28 — Retro production Cá đục kho tiêu SK

> Entry đầu tiên: từ scaffold repo tới chuỗi clip MiniMax. Đọc kèm `workflows/higgsfield/INDEX.md` (chi tiết từng request; trước 2026-09-29 nằm ở `work/higgsfield/`, đã gộp theo commit b0c2db5).

## Bối cảnh

Video quảng cáo túi cá đục kho tiêu: lốc nước mắm → vào nồi đất → bật bếp từ (vòng năng lượng) → sôi → chị bưng nồi + túi. Keyframes khóa K1a→K7, clip MiniMax H3 image-to-video kẹp 2 đầu.

## Việc đã làm (đường đi model)

1. **Soul 2** sinh keyframes text-only → trật bố cục K7 (thiếu top-down/fisheye), cá bị nấu chín do nhiễm ref.
2. **Grok Imagine 2.0** (`image_urls` ≤10) + ref → trúng K7, thành neo cả chuỗi.
3. **Marketing Studio Image** vào so kèo → thắng mảng tĩnh/bố cục (K1, K2), chốt mixed: MS cho đầu chuỗi, Grok cho cuối.
4. **MiniMax H3 image-to-video** chạy 7 clip (1a, 1b, 1bc, 1cd, 2v2, 3, 4); clip 1 bản đầu morph hỏng → tách motion + thêm K1b/K1c/K1d.

## Pitfall + cách fix

| # | Pitfall | Fix | Đã promote |
|---|---------|-----|------------|
| 1 | `urllib` gửi UA `Python-urllib` → Cloudflare 403 error 1010 | Header `User-Agent: curl/8.0` trong mọi script | script + journal này |
| 2 | Key export ở shell tương tác, phiên agent không thấy (`${#HF_KEY}`=0) | Key vào `.local/work/higgsfield/.env` (gitignored), agent nạp qua `WSLENV` mỗi lệnh | `.local/ENVIRONMENT.md` |
| 3 | File Windows editor chưa flush → WSL đọc 0 byte | Đọc key từ phía Windows truyền qua `WSLENV`, không đọc file cross-mount | journal này |
| 4 | Hàng đợi `queued` treo (Soul v2) | Chờ + tăng `--poll-timeout`; hết credit cũng gây treo → check balance trước | journal này |
| 5 | Ref cá kho chín (K7) khiến frame đầu chuỗi bị "nấu chín" | Ref phải cùng trạng thái sống/chín với frame cần gen (cá sống → ref `ca-duc-lam-sach.jpg`) | journal này |
| 6 | Prompt có `slams down`/`dense burst` → cờ `nsfw` | Viết mềm (`pours gently`, `fine mist`) | `docs/nsfw-filter-words.md` + PITFALLS #13 |
| 7 | Morph biến hình giữa clip (chai đứng→nghiêng, dĩa→nồi) | Tách motion tịnh tiến (bay lên → rót → xoáy); chỗ nào morph thì giấu trong dòng chảy đặc/bọt; neo dòng liên tục giữa 2 frame | journal này |
| 8 | Chuỗi trôi (nồi/bếp đổi hình) | Sinh lùi từ neo cuối (K7→K1), frame sau ref frame trước + neo gốc | journal này |
| 9 | Chữ túi AI vẽ lem | Không bắt AI vẽ chữ — overlay túi thật ở khâu dựng | journal này |
| 10 | Ảnh `.jpg` ruột PNG | Khai `content-type` theo ruột file, không theo đuôi | `upload_asset.py` (do người gọi chỉ định) |

## Bài học chốt (luật cho production sau)

1. **Neo cuối trước, sinh lùi sau.** Frame cuối (packshot) là neo cứng nhất vì chứa toàn bộ prop đã duyệt.
2. **Ref phải cùng trạng thái.** Sống ref sống, chín ref chín; lẫn 1 ref sai là nhiễm cả frame.
3. **Motion tịnh tiến, không morph.** Mỗi clip 1 động tác; biến hình thì giấu trong dòng/bọt/hơi hoặc cắt ở khâu dựng.
4. **Test clip khó nhất trước** (biến hình lớn nhất) — đạt mới chạy cả chuỗi.
5. **Từ vựng kiểm duyệt là tài sản đa nền tảng** — ghi `blocked/suspected/safe` theo từng nền tảng, không mang kết luận qua platform khác.
6. **Structure-only giữ repo sạch:** `work/` chỉ docs + script, sản phẩm + key ở `.local/` (gitignored).

## Chi phí (ước tính)

- Keyframes: ~20 request ảnh (Soul batch 4 + Grok/MS đơn). Clip: 8 request video 2K (7 clip 5s + 1 clip 8s ≈ $0.13/s).
- Đắt nhất không phải tiền mà là request thử-sai morph — luật số 3 sinh ra từ đó.
