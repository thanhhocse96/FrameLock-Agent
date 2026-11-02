# AGENTS.md — AI-GAN

> Startup order, invariants, routing. Chi tiết human → `docs/README.md`. Working memory → `.context/`.

## §0 Milestone

**M1 Bootstrap context system** — xem `.context/MILESTONES.md` cho acceptance criteria.

## §1 Startup order

Mỗi phiên mới, đọc theo thứ tự:

1. `.context/README.md` — luật phân loại working memory
2. `.context/GLOBAL.md` — mục tiêu dự án, module index, invariants tóm tắt
3. `.context/MILESTONES.md` — milestone hiện tại + checklist
4. `.context/TENSIONS_OPEN.md` — tension/conflict chưa resolve
5. `.context/TENSIONS_ACTIVE.md` — quyết định đã chốt đang hiệu lực
6. `.context/PITFALLS.md` — bẫy đã biết (prompt copy, mapping lệch, curios)
7. `.context/modules/<module>.md` — chỉ module liên quan task (`research-images`, `templates`)

Không load mặc định: `research/**/raws/*` (raw prompt text dài), `research/**/digests/*` (chỉ load entry được `mapping.md` trỏ tới), `.local/**` (sản phẩm local, không load), `docs/` human (chỉ khi task docs).

## §2 Invariants

| # | Invariant |
|---|-----------|
| 1 | **raw = text prompt, không phải media** — `research/images/raws/` chỉ chứa `.md`/`.txt` copy nguyên văn prompt của influencer; không lưu ảnh binary. Media mẫu (nếu cần) → `.local/` (gitignored) |
| 2 | **Raw bất biến** — file trong `raws/` sau khi ghi không sửa nội dung; sửa lỗi copy → tạo file mới `*_v2.md`, ghi chú trong digest |
| 3 | **Mọi claim trong digest phải truy về raw** — digest không bịa kỹ thuật/chủ đề/từ vựng; mỗi nhận định ghi `Nguồn: ../raws/<file>#<đoạn>` |
| 4 | **Mapping là index duy nhất** — không tìm digest bằng glob mò; `research/images/mapping.md` là source of truth để tra cứu |
| 5 | **Chat ≠ storage** — insight durable ghi vào `digests/`, `mapping.md`, `templates/`, `.context/modules/`; chuỗi video first/last-frame ghi case + từng run vào `research/videos/` theo §7; chat chỉ điều phối |
| 6 | **Template dùng được mới merge** — template trong `templates/` phải có `Index.md` trỏ tới + ví dụ fill từ 1 digest thật; template chưa test → giữ `drafts/` |
| 7 | **Governance-only-when-mentioned** — không sửa `AGENTS.md`/`.context/` nếu phiên không yêu cầu rõ |
| 8 | **Ngôn ngữ** — phân tích tiếng Việt, prompt tiếng Anh: digest + mapping + hướng dẫn fill + `Index.md` viết tiếng Việt; quote prompt gốc giữ tiếng Anh; **prompt mẫu trong template và mọi prompt kết quả khi được yêu cầu gen đều xuất tiếng Anh** (biến template đặt tên EN `UPPER_SNAKE` như `[SUBJECT]`) |
| 9 | **Bản quyền + nguồn** — mỗi raw ghi `Nguồn influencer/kênh + URL + ngày thu thập`; không re-post nguyên khối ra ngoài repo |
| 10 | **Ảnh + research video first/last-frame** — D-010 là quyết định compact lịch sử; user mở lại research video ngày 2026-10-12 và giới hạn ở chuỗi sinh có cả frame đầu và frame cuối (§7). Không tự mở rộng sang mode video khác, API hoặc platform mới; thay đổi phạm vi cần ASK |
| 11 | **Agent được mở pull request, mỗi PR một mối quan tâm + giải thích riêng** — xem `§6 Quy tắc pull request` |

## §3 Tension format

- **OPEN** → `.context/TENSIONS_OPEN.md` — conflict chưa resolve
- **ACTIVE** → `.context/TENSIONS_ACTIVE.md` — đã resolve, đang hiệu lực
- Mỗi entry: `ID`, mô tả ngắn, options, quyết định (nếu ACTIVE), ngày.

## §4 Routing

| Mode | Khi nào |
|------|---------|
| **CODE_NOW** | Task trong milestone hiện tại, đã có spec — làm ngay (thêm raw/digest/mapping/template theo đúng schema) |
| **ASK** | Đổi schema digest/mapping/template, đổi invariant, tách/gộp thư mục — hỏi user trước |
| **EXPLAIN** | User hỏi workflow, cách reverse-engineer — trích digest/mapping, không suy diễn thêm |

## §5 Self-check (trước khi ghi file)

- [ ] Đúng pipeline (raw → digest → mapping → template)?
- [ ] Raw có nguồn + URL + ngày?
- [ ] Digest có link ngược về raw + từ khóa kỹ thuật/chủ đề/model?
- [ ] Mapping đã thêm 1 dòng index cho digest mới?
- [ ] Template mới đã được `templates/Index.md` trỏ tới?
- [ ] Ngôn ngữ đúng (phân tích VI, prompt mẫu + prompt gen EN, biến `UPPER_SNAKE`)?
- [ ] File `.context/` mới đúng subdir (không dump root)?
- [ ] Nếu là chuỗi video first/last-frame: đã lưu brief, cặp frame, từng run, prompt/settings, chi phí, bằng chứng, feedback và tổng kết trong research; index có trỏ tới case?

## §6 Quy tắc pull request

1. Agent được mở pull request.
2. Mỗi PR một mối quan tâm (governance, template, workflows, docs… không gộp chung).
3. Mỗi PR có giải thích riêng: làm gì, vì sao, đã kiểm tra gì (self-check `§5`, không lộ key/media).
4. Không push/PR khi user nói "không có pr" trong phiên đó.

## §7 Chuỗi video first/last-frame — research để hình thành workflow Business

### Điều kiện áp dụng

Chỉ tự áp dụng skill `video-delta-analysis` và nghĩa vụ ghi research này khi chuỗi/đoạn video sinh dùng **cả frame đầu và frame cuối làm conditioning**. Hai ảnh chỉ làm reference, text-to-video hoặc first-frame-only không tự kích hoạt quy trình. Một chuỗi nhiều đoạn cần ghi rõ cặp đầu/cuối của từng đoạn áp dụng. Phân tích spec hoặc gọi skill không tự cấp quyền paid generation.

### Ghi mỗi lần thực hiện

- Tạo một hồ sơ case cho cả chuỗi; nối tiếp lịch sử từng run, không tạo case mới chỉ vì đổi prompt hoặc tăng duration.
- Brief gồm mục đích Business nếu có, spec, điều phải giữ, thứ tự/cặp frame, mức cho phép morph/time-lapse/cut và tiêu chí acceptance. Chưa biết mục đích Business thì ghi chưa rõ, không tự bịa KPI.
- Mỗi run lưu prompt EN đầy đủ, model/provider/mode, settings thực, biến đổi so với baseline, job ID nếu có, trạng thái, phí thực hoặc chưa rõ, bằng chứng quan sát và lỗi có timestamp. Ghi cả fail, blocked/cancelled và lý do dừng; không giả định request fail là miễn phí.
- Tách quan sát, giả thuyết, kết quả kiểm tra và feedback user. Endpoint đúng/API completed không chứng minh progression đúng; user chấp nhận sáng tạo và strict pass có thể khác nhau.
- Cuối chuỗi lưu điều đã học, phạm vi kết luận model, hướng chưa thử và việc dừng. Giới hạn cấu hình đã thử không tự thành kết luận về mọi model.

### Cấu trúc và promote

- Một index video là điểm tra cứu case; phương pháp chung tách khỏi dữ liệu thử. Tra index trước, không glob mò.
- Mỗi case gom brief/spec, lịch sử run và tổng kết tại một nơi; journal chỉ tóm tắt/trỏ tới case, tránh sao chép toàn bộ hồ sơ. Media/frame/log/request base64/key ở `.local/` (gitignored), không vào research.
- Tên case/run ổn định, kebab-case; liên kết từ case tới artifact local phải rõ và không giả định checkout khác có media.
- Không thêm thư mục/file ad-hoc nếu chưa có vai trò trong layout được duyệt. Tách/gộp/chuyển cấu trúc hiện hữu cần chốt layout với user trước theo §4.
- Kinh nghiệm từ case là nguồn để hình thành workflow Business: chỉ promote phần có bằng chứng phù hợp với mục đích, phạm vi và acceptance đã chốt; ghi nguồn case, giới hạn và tiêu chí kiểm chứng. Phương án chưa thử giữ trạng thái đề xuất; prompt video fail không được gọi là template đạt.
- Layout dưới đây được user duyệt ngày 2026-10-12 **cho case mới**. Hồ sơ cũ và artifact local cũ giữ nguyên vị trí/nội dung; index chung trỏ tới chúng, không di chuyển hoặc sao chép lại lịch sử.

```text
research/videos/
  INDEX.md                       # điểm tra cứu chung cho case mới và legacy
  methods/                       # phương pháp chung mới, không chứa run cụ thể
  cases/<case-slug>/
    case.md                      # brief, mục tiêu Business, chuỗi frame, tổng kết
    runs/<run-id>.md              # prompt/settings/kết quả của từng run

.local/video-runs/<case-slug>/<run-id>/
  ...                            # media, frame, log, request đầy đủ; gitignored
```

Không tạo thư mục/file rỗng chỉ để đủ cây; tạo khi có dữ liệu tương ứng. `<case-slug>` ổn định cho cả chuỗi; `<run-id>` có thứ tự như `001-baseline`, `002-morph`. `case.md` liên kết từng run; `INDEX.md` liên kết case và ghi trạng thái/nguồn workflow. Method hiện hữu dưới `delta-analysis/` tiếp tục được tham chiếu tại chỗ; method mới mới dùng `methods/`. Index cũ được giữ làm hồ sơ lịch sử, không là nơi ghi case mới.
