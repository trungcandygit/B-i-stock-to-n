# CLAUDE.md — Quy tắc bắt buộc cho repo này

## 1. FORCE RULE — Luôn load skill academic-research-skills (ARS)

**Bắt buộc 100%, không ngoại lệ.** Mọi task (kể cả task nhỏ, câu hỏi, sửa 1 dòng) phải làm theo skill ARS phù hợp.
**Tự động load:** ở task đầu tiên của phiên — hoặc khi cần một skill ARS chưa load trong phiên — gọi `Skill` tool
để load; skill đã load còn hiệu lực cả phiên, không gọi lại, chỉ tiếp tục tuân thủ 100% SKILL.md của nó.

| Loại task | Skill phải gọi |
|---|---|
| Viết / sửa / hoàn thiện bài báo, xử lý comment & chỉnh sửa của cô giáo / reviewer, abstract, citation check, format | `academic-paper` (mode `revision`, `revision-coach`, `citation-check`, `abstract`, ...) |
| Phản biện / review bài báo, đánh giá trước khi nộp | `academic-paper-reviewer` |
| Nghiên cứu, tổng quan tài liệu, fact-check, thiết kế phương pháp | `deep-research` |
| Quy trình trọn gói research → write → review → revise → finalize, **hoặc không chắc chọn skill nào** | `academic-pipeline` (mặc định) |

- Skill được vendor tại `vendor/academic-research-skills/` (upstream:
  https://github.com/imbad0202/academic-research-skills, commit ghi trong `.upstream-commit`) và
  link vào `.claude/skills/`.
- Hook `.claude/settings.json` (`SessionStart` + `UserPromptSubmit`) tự nhắc lại quy tắc này ở mỗi
  phiên và mỗi prompt. Không được xoá/tắt hook.
- Không hỏi lại người dùng những thứ skill đã có quy trình mặc định — cứ chạy theo skill.
- Skill nội bộ `Python for Algorithmic Trading/NCKH/Bài stock toán/skill gộp/` (quy tắc biên tập,
  checklist 120 điểm, playbook từng section) dùng **bổ sung** khi sửa bài báo.

## 1b. FORCE RULE — Không hỏi lại

- Người dùng đã ủy quyền trước: **không hỏi lại, không dừng chờ xác nhận** — kể cả các checkpoint
  "user must confirm" / IRON RULE xác nhận cấu hình của skill ARS. Tự chọn mặc định hợp lý nhất theo
  skill, ghi lại quyết định + lý do vào `notes/AUDIT_LEDGER.md`, và làm tới khi ra sản phẩm cuối.
- Không dùng AskUserQuestion. Chỉ dừng khi thật sự bị chặn (thiếu dữ liệu không thể suy ra) — khi đó
  ghi rõ vào ledger và vẫn hoàn thành mọi phần còn lại.
- Mọi chỉnh sửa phải chỉn chu nhất theo skill (quy trình, checklist, IRON RULE về trích dẫn thật).

## 2. FORCE RULE — Thực nghiệm bằng R

- Mọi thực nghiệm, phân tích, chạy lại code, vẽ hình, bảng số liệu mới đều làm bằng **R** (`Rscript`).
  Code Python cũ trong `project/` chỉ để tham chiếu / đối chiếu, không viết thực nghiệm mới bằng Python.
- Code R đặt tại `Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/`, có một script
  chạy toàn bộ (`run_all.R`), cố định seed, ghi output ra `project_R/outputs/`.
- **Khớp 100% với bài báo:** mọi con số, bảng, hình trong bài phải truy được về output R. Nếu số chạy
  lại lệch với bài, phải ghi rõ chỗ lệch và sửa bài (hoặc code) cho nhất quán — không được im lặng.

## 3. Bài báo

- Bản đang làm việc: `Python for Algorithmic Trading/NCKH/Bài stock toán/submission/*.docx`
  (có comment và tracked changes của cô giáo — phải xử lý hết, từng cái một).
- Nhật ký chỉnh sửa: `notes/AUDIT_LEDGER.md` — ghi lại mỗi vòng sửa.
