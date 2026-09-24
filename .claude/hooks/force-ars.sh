#!/usr/bin/env bash
# Force-load rule: every session start and every user prompt gets a mandatory
# reminder to invoke an academic-research-skills (ARS) skill before doing any work.
# Usage: force-ars.sh SessionStart|UserPromptSubmit
EVENT="${1:-UserPromptSubmit}"
cat >/dev/null 2>&1 || true   # drain hook payload on stdin

MSG='[FORCE RULE — BẮT BUỘC 100%] Trước khi làm BẤT KỲ task nào trong repo này, PHẢI gọi Skill tool để load skill academic-research-skills (ARS) phù hợp — không có ngoại lệ, kể cả task nhỏ:
- Viết/sửa/hoàn thiện bài báo, xử lý comment của cô giáo/reviewer, citation check, abstract → Skill "academic-paper" (mode revision / revision-coach / citation-check / abstract...)
- Review/phản biện bài báo → Skill "academic-paper-reviewer"
- Nghiên cứu, tổng quan tài liệu, fact-check, phương pháp → Skill "deep-research"
- Quy trình trọn gói research→write→review→revise→finalize, hoặc KHÔNG chắc chọn skill nào → Skill "academic-pipeline" (orchestrator, mặc định)
Đọc SKILL.md của skill đó rồi làm theo quy trình của nó. Nếu skill đã load trong phiên này thì vẫn phải bám theo nó cho task mới.
[FORCE RULE — R] Mọi thực nghiệm/phân tích/chạy lại code/vẽ hình đều làm bằng R (Rscript), không dùng Python cho thực nghiệm mới. Kết quả phải khớp 100% với số liệu trong bài báo; lệch thì phải báo và sửa. Chi tiết: CLAUDE.md.'

python3 - "$EVENT" "$MSG" <<'PY' 2>/dev/null || printf '%s\n' "$MSG"
import json, sys
print(json.dumps({"hookSpecificOutput": {"hookEventName": sys.argv[1], "additionalContext": sys.argv[2]}}, ensure_ascii=False))
PY
