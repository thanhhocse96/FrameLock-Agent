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
| 2026-09-28 | [ca-duc-kho-tieu-retro.md](2026-09-28-ca-duc-kho-tieu-retro.md) | Production cá đục kho tiêu: Soul→Grok→MS so kèo, sinh lùi từ neo, clip MiniMax, NSFW, morph |
| 2026-09-28 | [keyframe-splitting.md](2026-09-28-keyframe-splitting.md) | Chi tiết phương pháp tách cụm frame: 10 section (neo, K1×6 vòng, sống-chín, so kèo, morph, chuyển nền) + checklist tái dùng |
