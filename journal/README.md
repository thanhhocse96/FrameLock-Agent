# journal — nhật ký dev + agent

> Ghi theo thời gian: quyết định, pitfall, bài học, chi phí sau mỗi đợt production.
> Đọc khi: bắt đầu production mới, đổi model/nền tảng, hoặc onboarding dev mới.

## Quy ước

- Mỗi entry 1 file: `YYYY-MM-DD-<slug>.md` (tiếng Việt).
- Cấu trúc entry: Bối cảnh → Việc đã làm → Pitfall + cách fix → Bài học chốt → Chi phí (request/credit nếu nhớ).
- Không dump log dài — log ở `.local/work/<provider>/<slug>/run.log`, journal chỉ tóm tắt.
- Insight nào thành luật lâu dài → promote thêm vào `.context/PITFALLS.md` hoặc `docs/` (ghi rõ đã promote ở cuối entry).
- Phân biệt với `.context/` (memory agent vận hành theo phiên) và `docs/` (tài liệu tra cứu): journal là **dòng thời gian**, đọc từ mới tới cũ để hiểu vì sao repo thành ra thế này.

## Mục lục

| Ngày | Entry | Tóm tắt |
|------|-------|---------|
| 2026-11-02 | [sillago-background-outpaint.md](2026-11-02-sillago-background-outpaint.md) | Mở nền cá đục trên/dưới thành 3:4; không thấy props mới, chưa xác minh giữ nguyên pixel |
| 2026-11-02 | [iqf-conveyor-image-study.md](2026-11-02-iqf-conveyor-image-study.md) | Hai run ảnh IQF: sai hình học băng chuyền, prompt nguyên văn và artifact local, chưa đạt strict pass |
| 2026-10-12 | [total-product-image-study-retro.md](2026-10-12-total-product-image-study-retro.md) | Study ảnh demo TOTAL: user chấp nhận tạm ổn, lỗi tư thế tay còn tồn tại; đóng study, lưu kinh nghiệm |
| 2026-10-12 | [video-delta-analysis-retro.md](2026-10-12-video-delta-analysis-retro.md) | Ba thử nghiệm Husband F1→F2; lỗi count/contact/morph, spec user, chi phí và promote skill |
| 2026-09-28 | [ca-duc-kho-tieu-retro.md](2026-09-28-ca-duc-kho-tieu-retro.md) | Production cá đục kho tiêu: Soul→Grok→MS so kèo, sinh lùi từ neo, clip MiniMax, NSFW, morph |
| 2026-09-28 | [keyframe-splitting.md](2026-09-28-keyframe-splitting.md) | Chi tiết phương pháp tách cụm frame: 10 section (neo, K1×6 vòng, sống-chín, so kèo, morph, chuyển nền) + checklist tái dùng |
