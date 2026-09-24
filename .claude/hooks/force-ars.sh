#!/usr/bin/env bash
# Force-load rule: every session start and every user prompt gets a mandatory
# reminder to invoke an academic-research-skills (ARS) skill before doing any work.
# Usage: force-ars.sh SessionStart|UserPromptSubmit
EVENT="${1:-UserPromptSubmit}"
cat >/dev/null 2>&1 || true   # drain hook payload on stdin

MSG='[FORCE RULE — BẮT BUỘC 100%] Mọi task trong repo này PHẢI làm theo skill academic-research-skills (ARS) phù hợp — không có ngoại lệ, kể cả task nhỏ. Tự động load: ở task ĐẦU TIÊN của phiên (hoặc khi task cần một skill ARS chưa load trong phiên), gọi Skill tool để load skill đó; skill đã load thì vẫn còn hiệu lực cả phiên — KHÔNG gọi lại, chỉ tiếp tục tuân thủ 100% quy trình của nó:
- Viết/sửa/hoàn thiện bài báo, xử lý comment của cô giáo/reviewer, citation check, abstract → Skill "academic-paper" (mode revision / revision-coach / citation-check / abstract...)
- Review/phản biện bài báo → Skill "academic-paper-reviewer"
- Nghiên cứu, tổng quan tài liệu, fact-check, phương pháp → Skill "deep-research"
- Quy trình trọn gói research→write→review→revise→finalize, hoặc KHÔNG chắc chọn skill nào → Skill "academic-pipeline" (orchestrator, mặc định)
Tuân thủ 100% SKILL.md của skill đó (IRON RULE, checkpoint, anti-pattern) cho mọi task mới.
[FORCE RULE — R] Mọi thực nghiệm/phân tích/chạy lại code/vẽ hình đều làm bằng R (Rscript), không dùng Python cho thực nghiệm mới. Kết quả phải khớp 100% với số liệu trong bài báo; lệch thì phải báo và sửa. Chi tiết: CLAUDE.md.
[FORCE RULE — KHÔNG HỎI LẠI] Người dùng đã ủy quyền trước: KHÔNG hỏi lại, KHÔNG dừng chờ xác nhận (kể cả các checkpoint/IRON RULE "user must confirm" của skill). Tự chọn phương án mặc định hợp lý nhất theo skill, ghi quyết định vào notes/AUDIT_LEDGER.md, làm đến khi xong sản phẩm cuối. Mọi chỉnh sửa phải chỉn chu nhất theo skill.'

python3 - "$EVENT" "$MSG" <<'PY' 2>/dev/null || printf '%s\n' "$MSG"
import json, sys
print(json.dumps({"hookSpecificOutput": {"hookEventName": sys.argv[1], "additionalContext": sys.argv[2]}}, ensure_ascii=False))
PY
