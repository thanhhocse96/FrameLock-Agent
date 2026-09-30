# TENSIONS_ACTIVE — quyết định đã chốt đang hiệu lực

> Entry đã resolve từ `TENSIONS_OPEN.md`. Mỗi entry: ID, quyết định, ngày.

| ID | Ngày | Quyết định |
|----|------|------------|
| D-001 | 2026-09-28 | **raw = text prompt, không phải media.** `raws/` chỉ `.md`/`.txt`; media mẫu → `.local/` (gitignored). User chốt 2026-09-28. |
| D-002 | 2026-09-28 | **Phong cách context-mapping làm chủ đạo:** `.context/` + `AGENTS.md` startup order + mapping là index duy nhất (không glob mò digest). |
| D-003 | 2026-09-28 | **Ngôn ngữ:** phân tích tiếng Việt, prompt tiếng Anh. Digest/mapping/hướng dẫn fill/`Index.md` tiếng Việt; quote prompt gốc giữ tiếng Anh. **Prompt mẫu trong template và mọi prompt kết quả khi được yêu cầu gen đều xuất tiếng Anh** (biến EN `UPPER_SNAKE`). User chốt 2026-09-28. |
| D-004 | 2026-09-28 | **T-001 → B: đổi `researchs/` thành `research/`.** Đã rename thư mục + cập nhật mọi link (`AGENTS.md`, `README.md`, `.context/`, `docs/`). User chốt 2026-09-28. |
| D-005 | 2026-09-28 | **T-002 → B: mở rộng schema digest thêm tone/shot/composition.** Digest ảnh: kỹ thuật + tone + shot + composition + chủ đề + từ vựng; digest video thêm cấu trúc thời gian; mapping thêm cột tone/shot/composition. User chốt 2026-09-28. |
| D-006 | 2026-09-28 | **work/ structure-only cho API (provider đầu: higgsfield).** `work/` chỉ commit `README.md` + `INDEX.md`; mọi input/output/log/key vào `.local/work/<provider>/<slug>/` (gitignored). Promote output tốt → `research/*/raws/` → digest → mapping → template. User chốt 2026-09-28. |
| D-007 | 2026-09-28 | **Script là đường chính trong OpenCode, MCP là đường phụ.** Script (`run_minimax_h3.py` + `HF_KEY`) tái lập được, khớp pipeline promote; MCP Higgsfield (`opencode.json` project-scope → `https://mcp.higgsfield.ai/mcp`, OAuth tài khoản) dùng khi cần `create_character`/history. User chốt 2026-09-28. |
| D-008 | 2026-09-29 | **Nhận `workflows/higgsfield/` làm nơi duy nhất cho chạy thử API.** Phiên ITSKVN gộp `work/higgsfield/` → `workflows/` (commit b0c2db5); phiên này đối chiếu: INDEX + scripts + models nguyên vẹn, chuyển nốt `genjutsu-control.md`, sửa link cũ, `.local/work/` giữ nguyên. User chốt 2026-09-29. |
| D-009 | 2026-09-30 | **Agent được mở pull request, mỗi PR một mối quan tâm + giải thích riêng.** Không gộp governance/template/workflows/docs chung một PR; mỗi PR ghi làm gì, vì sao, đã kiểm tra gì. User chốt 2026-09-30. |
