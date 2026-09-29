# Module: work-apis

> Quy tắc chạy thử API theo provider. `work/` structure-only — mọi sản phẩm vào `.local/work/`.

## Layout

```
work/<provider>/README.md      ← setup, auth, workflow (commit)
work/<provider>/INDEX.md       ← index experiment, 1 dòng/lần chạy (commit)
work/<provider>/models/<model>.md + .params.example.json   ← doc model (commit)
work/<provider>/run_<model>.py ← script chạy, key từ env (commit, không chứa key)
.local/work/<provider>/<YYYY-MM-DD-slug>/
  input.md | params.json | output/ | result.md | run.log   (gitignored)
```

## Quy tắc

1. Provider mới → `work/<provider>/` + `README.md` + `INDEX.md`, hỏi user trước (ASK — tách/gộp thư mục).
2. Key/token chỉ từ env hoặc `.local/` — cấm vào `work/` (xem `PITFALLS.md` #9).
3. Mỗi lần chạy thêm 1 dòng `INDEX.md`: local path, ngày, template/digest nguồn, kết quả, promote?.
4. Output tốt → promote: copy prompt (EN) vào `research/*/raws/` với nguồn là experiment path → digest → mapping → template. Không trỏ digest trực tiếp vào `.local/`.
5. `params.json` tối thiểu: model+version, prompt_source, seed, size, duration_sec.
6. Ngôn ngữ: `README.md`/`INDEX.md`/`result.md` tiếng Việt; `input.md` prompt tiếng Anh.
