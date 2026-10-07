#!/usr/bin/env bash
# Force-load rule: every session start and every user prompt gets a mandatory
# reminder to invoke an academic-research-skills (ARS) skill before doing any work.
# Usage: force-ars.sh SessionStart|UserPromptSubmit
EVENT="${1:-UserPromptSubmit}"
cat >/dev/null 2>&1 || true   # drain hook payload on stdin

MSG='[FORCE RULE — BẮT BUỘC 100%] Mọi task trong repo này PHẢI làm theo skill academic-research-skills (ARS) phù hợp — không có ngoại lệ, kể cả task nhỏ. Tự động load MỖI LẦN: với MỖI yêu cầu/task mới của người dùng (mỗi prompt giao việc), gọi Skill tool để load lại skill ARS phù hợp TRƯỚC KHI làm bất cứ việc gì, kể cả khi skill đã load trước đó trong phiên; trong cùng một task thì không gọi lại:
- Viết/sửa/hoàn thiện bài báo, xử lý comment của cô giáo/reviewer, citation check, abstract → Skill "academic-paper" (mode revision / revision-coach / citation-check / abstract...)
- Review/phản biện bài báo → Skill "academic-paper-reviewer"
- Nghiên cứu, tổng quan tài liệu, fact-check, phương pháp → Skill "deep-research"
- Quy trình trọn gói research→write→review→revise→finalize, hoặc KHÔNG chắc chọn skill nào → Skill "academic-pipeline" (orchestrator, mặc định)
Tuân thủ 100% SKILL.md của skill đó (IRON RULE, checkpoint, anti-pattern) cho mọi task mới.
[FORCE RULE — AGENT ĐỘC LẬP + BẢN THẢO MẠNH NHẤT] Phản biện/re-review/kiểm tra số liệu phải do agent độc lập (Agent tool, ngữ cảnh mới, không đọc ledger) thực hiện; đi đủ mọi bước của skill (roadmap → sửa → re-review, tối đa 2 vòng → proofreading + stop-slop → kiểm tra cuối). Mục tiêu: bản thảo mạnh nhất theo skill, không bỏ bước.
[FORCE RULE — R] Mọi thực nghiệm/phân tích/chạy lại code/vẽ hình đều làm bằng R (Rscript), không dùng Python cho thực nghiệm mới. Kết quả phải khớp 100% với số liệu trong bài báo; lệch thì phải báo và sửa. Chi tiết: CLAUDE.md.
[FORCE RULE — KHÔNG HỎI LẠI] Người dùng đã ủy quyền trước: KHÔNG hỏi lại, KHÔNG dừng chờ xác nhận (kể cả các checkpoint/IRON RULE "user must confirm" của skill). Tự chọn phương án mặc định hợp lý nhất theo skill, ghi quyết định vào notes/AUDIT_LEDGER.md, làm đến khi xong sản phẩm cuối. Mọi chỉnh sửa phải chỉn chu nhất theo skill.'

python3 - "$EVENT" "$MSG" <<'PY' 2>/dev/null || printf '%s\n' "$MSG"
import json, sys
print(json.dumps({"hookSpecificOutput": {"hookEventName": sys.argv[1], "additionalContext": sys.argv[2]}}, ensure_ascii=False))
PY
