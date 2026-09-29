---
name: make-digest
description: Analyze a raw prompt into a research digest with technique tone shot composition keywords and append one mapping row. Use when writing a digest, phan tich prompt, or updating mapping.md.
---

# Make Digest

Phân tích raw thành digest + 1 dòng mapping. Mọi claim phải truy về raw.

## Quy tắc

- Digest: `research/images/digests/<slug>.md` hoặc `research/videos/digests/<slug>.md`, viết tiếng Việt; quote prompt gốc giữ tiếng Anh.
- Mỗi nhận định kèm `Nguồn: ../raws/<file>#<đoạn>`. Không bịa model/kỹ thuật nếu raw không nói.
- Mapping là index duy nhất: mỗi digest = 1 dòng trong `research/images/mapping.md` (hoặc videos). Không tìm digest bằng glob mò.
- Schema digest ảnh: kỹ thuật, tone, shot, composition, chủ đề, từ vựng, công thức, ghi chú bản quyền. Digest video thêm cấu trúc thời gian.
- Mapping 1 dòng: `| digest | model | kỹ thuật | tone | shot | composition | chủ đề | từ vựng |`. Từ khóa kỹ thuật/model kebab-case tiếng Anh, chủ đề tiếng Việt.

## Các bước

1. Đọc raw (`../raws/<slug>.md`). Nếu chưa có raw, dừng và gọi skill `add-raw` trước.
2. Ghi digest theo schema `.context/modules/research-images.md` (ảnh) hoặc `research-videos.md` (video).
3. Thêm ngay 1 dòng vào `mapping.md` tương ứng (self-check AGENTS.md §5).
4. Báo đường dẫn digest + dòng mapping đã thêm.
