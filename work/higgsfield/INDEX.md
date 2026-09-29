# INDEX — experiment Higgsfield (source of truth)

> Chỉ index metadata. Media + input đã chạy nằm ở `.local/work/higgsfield/<slug>/` (gitignored), không commit.

| Experiment (local path) | Ngày | Model | Template/digest nguồn | Kết quả | Promote? |
|---|---|---|---|---|---|
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k2` | 2026-09-28 | soul-v2 (seed 60928, batch 4) | Kịch bản cá đục shot-1 K2 | completed 4 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k3` | 2026-09-28 | soul-v2 (seed 60928, batch 4) | Kịch bản cá đục shot-2 K3 | completed 4 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k5` | 2026-09-28 | soul-v2 (seed 60928, batch 4) | Kịch bản cá đục shot-3 K5 | completed 4 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k6` | 2026-09-28 | soul-v2 (seed 60928, batch 4) | Kịch bản cá đục shot-3 K6 | completed 4 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k7` | 2026-09-28 | soul-v2 (seed 60928, batch 4) | Kịch bản cá đục shot-4 K7 | completed 4 ảnh, user chê sai bố cục (thiếu top-down/fisheye) | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k7b` | 2026-09-28 | soul-v2 (seed 60928, batch 4) | Kịch bản cá đục shot-4 K7 retry (khóa top-down + fisheye) | completed 4 ảnh, user chê không tham khảo ảnh SP | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k7c` | 2026-09-28 | soul-v2 (seed 60928, batch 4) | Kịch bản cá đục shot-4 K7 bg-plate (nền trống, túi overlay hậu kỳ) | completed 4 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k7-grok` | 2026-09-28 | grok-imagine-2.0 (2k, 16:9, 2 refs) | Kịch bản cá đục shot-4 K7 (ref composite + túi thật) | completed 1 ảnh, user chốt neo K7 | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k6-back-test` | 2026-09-28 | grok-imagine-2.0 (1k, low, ref K7 CDN) | Sinh lùi K6 từ neo K7 (test rẻ) | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k6-back-ms` | 2026-09-28 | marketing-studio/image (2k, high, ref K7 CDN) | Sinh lùi K6 từ neo K7 (so kèo Grok, cùng prompt) | completed 1 ảnh, lỗi găng tay bếp — bỏ qua theo user | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k5-grok` | 2026-09-28 | grok-imagine-2.0 (2k, medium, ref K6-Grok) | K5 vòng năng lượng (so kèo, cùng prompt + ref) | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k5-ms` | 2026-09-28 | marketing-studio/image (2k, high, ref K6-Grok) | K5 vòng năng lượng (so kèo, cùng prompt + ref) | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k4-grok` | 2026-09-28 | grok-imagine-2.0 (2k, medium, ref K5-Grok) | K4 nồi đầy, tắt vòng (so kèo, ref chuỗi riêng) | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k4-ms` | 2026-09-28 | marketing-studio/image (2k, high, ref K5-MS) | K4 nồi đầy, tắt vòng (so kèo, ref chuỗi riêng) | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k3-grok` | 2026-09-28 | grok-imagine-2.0 (2k, medium, ref K4-Grok + K7 cá) | K3 rót vào nồi, cá neo K7 | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k3-ms` | 2026-09-28 | marketing-studio/image (2k, high, ref K4-MS + K7 cá) | K3 rót vào nồi, cá neo K7 | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k2-grok` | 2026-09-28 | grok-imagine-2.0 (2k, medium, ref K3-Grok + K7 cá) | K2 lốc hoàn chỉnh, cá neo K7 | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k2-ms` | 2026-09-28 | marketing-studio/image (2k, high, ref K3-MS + K7 cá) | K2 lốc hoàn chỉnh, cá neo K7 | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k1-grok` | 2026-09-28 | grok-imagine-2.0 (2k, medium, ref K2-Grok + K7 cá) | K1 chai bắt đầu đổ, cá neo K7 | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k1-ms` | 2026-09-28 | marketing-studio/image (2k, high, ref K2-MS + K7 cá) | K1 chai bắt đầu đổ, cá neo K7 | completed 1 ảnh, user đổi ý: K1 tĩnh | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k1-ms-static` | 2026-09-28 | marketing-studio/image (2k, high, ref K2-MS + K7 cá) | K1 tĩnh trước giờ G (chai đứng, hũ gia vị, khay nhựa trắng) | completed 1 ảnh, user sửa: chai cao + khay xốp | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k1-ms-static-v2` | 2026-09-28 | marketing-studio/image (2k, high, ref K2-MS + K7 cá) | K1 tĩnh v2 (chai cao, khay mút xốp polystyrene) | completed 1 ảnh, user sửa: cá sơ chế + túi dưới khay | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k1-ms-static-v3` | 2026-09-28 | marketing-studio/image (2k, high, 3 refs) | K1 tĩnh v3 (cá bỏ đầu+mắt, túi thật dưới khay xốp) | completed 1 ảnh, lỗi: cá còn đầu+mắt và bị nấu chín (nhiễm ref K7) | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k1-ms-static-v4` | 2026-09-28 | marketing-studio/image (2k, high, 3 refs) | K1 tĩnh v4 (cá sống làm sạch ref ca-duc-lam-sach, bỏ ref K7 chín) | completed 1 ảnh, lỗi: chai lùn không khớp K2 | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k1-ms-static-v5` | 2026-09-28 | marketing-studio/image (2k, high, 3 refs) | K1 tĩnh v5 (chai cao gấp đôi hũ, khớp dáng K2) | completed 1 ảnh, user chốt + sửa tiếp: mở nắp hũ | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k1-ms-static-v6` | 2026-09-28 | marketing-studio/image (2k, high, 3 refs) | K1 tĩnh v6 (mở nắp hũ gia vị) | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k2-ms-rawfix` | 2026-09-28 | marketing-studio/image (2k, high, ref K1v6 + cá sống) | K2 fix cá sống (bỏ ref K7 chín) | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k3-ms-rawfix` | 2026-09-28 | marketing-studio/image (2k, high, ref K2-rawfix + cá sống) | K3 fix cá sống vào nồi trống (chín từ K5 bật bếp) | completed 1 ảnh, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-clip1` | 2026-09-28 | minimax/h3/image-to-video (2K, 5s, K1→K2) | Clip 1 test (khó nhất: tĩnh → lốc xoáy) | completed, user chê morph — sửa kịch bản bay lên + nắp bật | — |
| `.local/work/higgsfield/2026-09-28-keyframes-ca-duc/k1b-ms` | 2026-09-28 | marketing-studio/image (2k, high, ref K1v6 + cá sống) | K1b trung gian (chai bay cao, nắp bật, nguyên liệu lơ lửng nhỏ) | completed 1 ảnh, user chốt K1b.jpg | — |
| `.local/work/higgsfield/2026-09-28-clip1a` | 2026-09-28 | minimax/h3/image-to-video (2K, 5s, K1a→K1b) | Clip 1a (bay lên + nắp bật) | completed, video đã tải, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-clip1b` | 2026-09-28 | minimax/h3/image-to-video (2K, 5s, K1b→K2) | Clip 1b (rót + lốc hoàn chỉnh) | completed, video đã tải, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-clip2` | 2026-09-28 | minimax/h3/image-to-video (2K, 5s, K3→K4) | Clip 2 (rót vào nồi) | completed, lỗi: lốc thành chảo, cá đổi hình giả | — |
| `.local/work/higgsfield/2026-09-28-clip2v2` | 2026-09-28 | minimax/h3/image-to-video (2K, 5s, K3→K4) | Clip 2 v2 (giấu cá trong dòng sốt đặc) | completed, video đã tải, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-clip3` | 2026-09-28 | minimax/h3/image-to-video (2K, 5s, K5→K6) | Clip 3 (vòng năng lượng → sôi) | completed, video đã tải, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-clip4` | 2026-09-28 | minimax/h3/image-to-video (2K, 8s, K6→K7) | Clip 4 (pull-back lộ chị + túi) | completed, video đã tải, chờ user duyệt | — |
| `.local/work/higgsfield/2026-09-28-clip1cd` | 2026-09-28 | minimax/h3/image-to-video (2K, 5s, K1c→K1d) | Clip 1cd (dĩa morph nồi, neo dòng chảy + arc top-down) | completed, video đã tải, chờ user duyệt | — |

Cột Promote?: `không` / `research/videos/raws/<file>` (khi output tốt và đã copy prompt vào kho).
