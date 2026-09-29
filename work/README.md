# work — khu vực chạy thử API (scripts + docs commit, sản phẩm ở .local)

> `work/` commit **scripts + docs + INDEX** (script `run_*.py` do skill `higgsfield-run` điều phối, không chứa key).
> Mọi thứ liên quan đến sản phẩm (prompt input đã chạy, params, media output, log, key) → `.local/work/` (gitignored), không commit.

```
work/                          ← commit (cấu trúc + docs)
  README.md                    ← file này — quy ước work/
  <provider>/                  ← vd higgsfield/
    README.md                  ← setup, auth, workflow riêng provider
    INDEX.md                   ← index experiment (SoT tra cứu)
.local/work/                   ← gitignored (sản phẩm thật)
  <provider>/<YYYY-MM-DD-slug>/
    input.md                   ← prompt EN đã gửi + link template/digest nguồn
    params.json                ← model, version, seed, size, duration, ...
    output/                    ← media trả về
    result.md                  ← đánh giá VI + có promote lên digest không
    run.log                    ← log gọi API
```

Quy tắc:

1. Thêm provider mới → tạo `work/<provider>/` với `README.md` + `INDEX.md`, hỏi user trước (ASK).
2. Mỗi lần chạy → 1 thư mục `.local/work/<provider>/<YYYY-MM-DD-slug>/`, thêm 1 dòng vào `work/<provider>/INDEX.md`.
3. API key/token **không bao giờ** vào `work/` — chỉ đọc từ env hoặc `.local/` (xem `PITFALLS.md` #9–#12).
4. Muốn đưa kết quả vào kho chính → promote theo pipeline: output tốt → copy prompt vào `research/*/raws/` (ghi nguồn là experiment) → digest → mapping → template.
5. Ngôn ngữ: `work/*/README.md` + `INDEX.md` tiếng Việt; prompt trong `input.md` tiếng Anh.
