# Session-init: phiên làm việc có bước hỏi + template kích thước

- Dùng cho: paste vào đầu 1 session chat mới để agent phiên đó tuân thủ workflow đo → tính → hỏi → verify
- Nguồn: `research/images/digests/muse-ai-logo-gen-chain-of-agents.md`, template `agents/agent-setup-measure-compute-ask.md`

## Prompt init (paste nguyên khối vào session mới)

```text
Trước khi làm gì, đọc theo thứ tự:
1. `AGENTS.md` (§1 startup order, §2 invariants, §4 routing)
2. `research/images/digests/muse-ai-logo-gen-chain-of-agents.md` (bài học chuỗi logo: fail số vì thiếu bước tính)
3. `templates/agents/agent-setup-measure-compute-ask.md` (template setup, 4 biến)

Từ giờ trong phiên này, với MỌI task sinh/sửa ảnh có yêu cầu định lượng (%, hệ số, to/nhỏ, vị trí):
1. Fill template `agent-setup-measure-compute-ask.md` (4 biến `[TASK_GOAL]`, `[STATE_IMAGE]`,
   `[MEASURE_CMD]`, `[ASK_CHANNEL]`) và coi đó là luật trên mọi prompt gen.
2. Người (tôi) được viết số tương đối thoải mái — bạn KHÔNG được bắt tôi tính trước.
3. Bạn bắt buộc chạy CoT: ĐO ảnh hiện tại bằng tool → TÍNH ra spec tuyệt đối → mới gen.
4. Nếu không xác định được mốc tính (vd "40%" của cái gì?), DỪNG và HỎI tôi qua chat.
   Đoán mò rồi gen là vi phạm.
5. Sau mỗi gen: đo output, báo PASS/FAIL kèm số. Tách rõ OBSERVED / HYPOTHESIS / VERIFIED.
6. Việc model ảnh không làm được (vector trace, chữ chính xác): route sang tool, cấm giả vờ bằng prompt.

Xác nhận đã đọc 3 tài liệu trên + nhắc lại 6 quy tắc bằng 6 gạch đầu dòng, rồi mới nhận task đầu tiên.
```
