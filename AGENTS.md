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
7. `.context/modules/<module>.md` — chỉ module liên quan task (`research-images`, `research-videos`, `templates`, `work-apis`)

Không load mặc định: `research/**/raws/*` (raw prompt text dài), `research/**/digests/*` (chỉ load entry được `mapping.md` trỏ tới), `workflows/*/INDEX.md` (chỉ load dòng experiment liên quan task), `.local/work/**` (sản phẩm local, không load), `docs/` human (chỉ khi task docs).

## §2 Invariants

| # | Invariant |
|---|-----------|
| 1 | **raw = text prompt, không phải media** — `research/*/raws/` chỉ chứa `.md`/`.txt` copy nguyên văn prompt của influencer; không lưu ảnh/video binary. Media mẫu (nếu cần) → `.local/` (gitignored) |
| 2 | **Raw bất biến** — file trong `raws/` sau khi ghi không sửa nội dung; sửa lỗi copy → tạo file mới `*_v2.md`, ghi chú trong digest |
| 3 | **Mọi claim trong digest phải truy về raw** — digest không bịa kỹ thuật/chủ đề/từ vựng; mỗi nhận định ghi `Nguồn: ../raws/<file>#<đoạn>` |
| 4 | **Mapping là index duy nhất** — không tìm digest bằng glob mò; `research/images/mapping.md` và `research/videos/mapping.md` là source of truth để tra cứu |
| 5 | **Chat ≠ storage** — insight durable ghi vào `digests/`, `mapping.md`, `templates/`, `.context/modules/`; chat chỉ điều phối |
| 6 | **Template dùng được mới merge** — template trong `templates/` phải có `Index.md` trỏ tới + ví dụ fill từ 1 digest thật; template chưa test → giữ `drafts/` |
| 7 | **Governance-only-when-mentioned** — không sửa `AGENTS.md`/`.context/` nếu phiên không yêu cầu rõ |
| 8 | **Ngôn ngữ** — phân tích tiếng Việt, prompt tiếng Anh: digest + mapping + hướng dẫn fill + `Index.md` viết tiếng Việt; quote prompt gốc giữ tiếng Anh; **prompt mẫu trong template và mọi prompt kết quả khi được yêu cầu gen đều xuất tiếng Anh** (biến template đặt tên EN `UPPER_SNAKE` như `[SUBJECT]`) |
| 9 | **Bản quyền + nguồn** — mỗi raw ghi `Nguồn influencer/kênh + URL + ngày thu thập`; không re-post nguyên khối ra ngoài repo |
| 10 | **workflows/ là nơi duy nhất cho chạy thử API, sản phẩm ở .local** — `workflows/<platform>/` commit `README.md` + `INDEX.md` + script chạy (`*.py`, key từ env, không chứa key) + `models/` (doc + params mẫu), chạy trên WSL; skill `higgsfield-run` điều phối. Mọi input đã chạy/output/log/key vào `.local/work/<provider>/<slug>/` (gitignored). Cấm API key trong `workflows/`, `research/`, `templates/` |

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
- [ ] Experiment API mới đã thêm 1 dòng `workflows/<platform>/INDEX.md` (không commit media/key)?
- [ ] Ngôn ngữ đúng (phân tích VI, prompt mẫu + prompt gen EN, biến `UPPER_SNAKE`)?
- [ ] File `.context/` mới đúng subdir (không dump root)?
