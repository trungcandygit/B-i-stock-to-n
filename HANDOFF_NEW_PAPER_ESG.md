# HANDOFF — Viết một bài MỚI THẬT SỰ từ bộ dữ liệu của bài ESG2

Tài liệu này dành cho một phiên Claude Code mới làm việc trên repo **`trungcandygit/B-i-ESG2`**.
Phiên mới đọc toàn bộ file này trước khi làm bất cứ việc gì, rồi làm theo từ đầu đến cuối.
Nguồn mẫu (skill, hook, quy trình đã chạy thành công) nằm ở repo **`trungcandygit/B-i-stock-to-n`**.

---

## 0. Mục tiêu và ranh giới liêm chính (IRON RULE — không được vi phạm)

**Mục tiêu:** từ **cùng bộ dữ liệu** của bài ESG2 gốc, viết một bài báo **mới thật sự** để gửi tạp chí
*Journal of Finance: Insights and Perspectives* (AFA, Wiley, open access). Bài gốc ESG2 vẫn được tác giả gửi tạp chí khác.

**Được phép:** dùng lại dữ liệu (cùng mẫu, cùng nguồn), với điều kiện bài mới có đủ 3 điều sau:
1. **Câu hỏi nghiên cứu khác** (không phải cùng câu hỏi được diễn đạt lại).
2. **Phân tích khác**: biến phụ thuộc, thiết kế nhận diện và phương pháp khác.
3. **Kết quả khác**: không có bảng hay hình nào trùng, không đăng lại cùng một hệ số.

**Cấm tuyệt đối** (đăng trùng lặp, salami slicing, text recycling; theo COPE, Wiley và Springer):
- Diễn đạt lại (paraphrase) bài gốc để "khác 80%" rồi nộp như bài mới.
- Dùng lại nguyên văn đoạn văn, bảng hoặc hình của bài gốc.
- Chia cùng một kết quả thành hai bài.
- Giấu việc hai bài dùng chung dữ liệu.

**Bắt buộc công khai:**
- Trong bài mới, mục Data: ghi rõ dữ liệu cũng được dùng trong một nghiên cứu khác (companion study) với câu hỏi khác.
  - Bản ẩn danh (blinded): ghi *"a companion study (details withheld for anonymous review)"*.
  - Bản có tên tác giả: ghi đầy đủ tên bài gốc và tình trạng (under review / working paper).
- Trong cover letter: nói rõ với biên tập viên về bài song hành, tình trạng của nó, và vì sao hai bài không trùng.

Nếu không tìm được câu hỏi nào thật sự khác mà dữ liệu hiện có trả lời được, **dừng lại, ghi vào ledger và báo người dùng**. Không cố viết bằng mọi giá.

---

## 1. Thiết lập repo B-i-ESG2 (làm đầu tiên, trước mọi phân tích)

Repo có thể đang trống hoặc mới chỉ có bài gốc. Sao chép bộ công cụ từ `B-i-stock-to-n`:

```bash
# trong phiên mới: clone repo mẫu (chỉ để lấy công cụ, không sửa gì bên đó)
git clone --depth 1 https://github.com/trungcandygit/B-i-stock-to-n /tmp/template
cd <thư mục repo B-i-ESG2>
mkdir -p vendor .claude/skills .claude/hooks
cp -R /tmp/template/vendor/academic-research-skills vendor/
cp -R /tmp/template/vendor/proofreading vendor/
cp -R /tmp/template/vendor/stop-slop vendor/
cp /tmp/template/.claude/settings.json .claude/
cp /tmp/template/.claude/hooks/force-ars.sh .claude/hooks/
for s in academic-paper academic-paper-reviewer academic-pipeline deep-research; do
  ln -sfn ../../vendor/academic-research-skills/$s .claude/skills/$s; done
ln -sfn ../../vendor/proofreading .claude/skills/proofreading
ln -sfn ../../vendor/stop-slop .claude/skills/stop-slop
```

Sau đó viết **`CLAUDE.md`** ở gốc repo B-i-ESG2. Lấy nội dung từ `/tmp/template/CLAUDE.md` và chỉnh các đường dẫn (mục 2, 3) cho repo này. Giữ nguyên các FORCE RULE:
- **§1 ARS:** mọi task đều theo skill ARS. Tự load skill **một lần mỗi phiên**, không gọi lại (người dùng đã phàn nàn khi skill bị gọi lại nhiều lần).
  Bảng chọn skill: academic-paper / academic-paper-reviewer / deep-research / academic-pipeline (mặc định).
- **Vòng ngôn ngữ:** sau tối đa 2 vòng revision của ARS, chạy 2 vòng `proofreading` + `stop-slop`. Mỗi vòng phải qua cổng kiểm tra của `academic-paper`.
- **§1b Không hỏi lại:** người dùng đã uỷ quyền trước. Không dừng ở các checkpoint "user must confirm"; tự chọn mặc định hợp lý nhất theo skill, ghi quyết định và lý do vào `notes/AUDIT_LEDGER.md`. Không dùng AskUserQuestion. Chỉ dừng khi thật sự bị chặn.
- **§2 R:** mọi thực nghiệm, bảng, hình mới đều làm bằng **R** (`Rscript`), đặt trong `project_R/`, có `run_all.R`, cố định seed, output ghi vào `project_R/outputs/`. **Khớp 100%**: mọi con số trong bài phải truy được về một file output R. Code Python cũ (nếu có) chỉ để tham chiếu.
- **§3 Bài báo:** ghi đường dẫn bài gốc, bài mới, bộ hồ sơ nộp và ledger.
- **Thêm FORCE RULE riêng cho repo này:** *"Bài mới phải khác bài gốc ở câu hỏi, phân tích và kết quả; không tái sử dụng văn bản, bảng, hình; công khai việc dùng chung dữ liệu"* (xem §0).

Kiểm tra hook: `.claude/settings.json` có `SessionStart` và `UserPromptSubmit` gọi `bash "$CLAUDE_PROJECT_DIR/.claude/hooks/force-ars.sh"`. Không được xoá hay tắt hook.
Commit: *"Bootstrap: vendor ARS + proofreading + stop-slop skills, force hooks, CLAUDE.md"*.

---

## 2. Quy trình tổng thể (skill `academic-pipeline` điều phối)

Load `academic-pipeline` ở task đầu tiên. Các skill khác được load **một lần** khi đến giai đoạn của chúng.

| Giai đoạn | Skill | Sản phẩm (ghi trong repo) |
|---|---|---|
| S0 Đọc bài gốc | deep-research (paper review) | `notes/00_original_paper_map.md`: câu hỏi nghiên cứu, giả thuyết, biến, mẫu, phương pháp, mọi bảng và hình, kết luận chính → **bản đồ vùng cấm trùng** |
| S1 Chọn câu hỏi mới | deep-research (lit-review + Socratic, tự trả lời theo mặc định) | `notes/01_candidate_RQs.md`: 3 câu hỏi ứng viên, chấm điểm theo độ mới / khả thi với dữ liệu / độ phù hợp JF:IP / khoảng cách với bài gốc → chọn 1 câu, ghi lý do vào ledger |
| S2 Thiết kế phương pháp | deep-research (methodology) | `notes/02_analysis_plan.md`: giả thuyết, biến, chiến lược nhận diện, kiểm định robustness, ngưỡng ý nghĩa, viết TRƯỚC khi chạy kết quả (pre-analysis plan) |
| S3 Thực nghiệm bằng R | — (FORCE RULE R) | `project_R/run_all.R`, `R/*.R`, `outputs/*.csv` và hình (EPS + PNG 600 dpi), cố định seed |
| S4 Viết bài | academic-paper (full) | bản thảo docx theo cấu trúc tạp chí |
| S5 Kiểm tra liêm chính + trích dẫn | academic-paper (citation-check) | mọi tài liệu tham khảo đều có thật, có DOI và đã kiểm tra; không bịa |
| S6 Phản biện | academic-paper-reviewer (**full**, 5 ghế, sprint contract `reviewer/reviewer_full/v2`, provenance) | `notes/review_full/*` |
| S7 Sửa bài (tối đa 2 vòng) + phản biện lại | academic-paper (revision) + reviewer (re-review 3 cổng) | response to reviewers, `08_rereview*.md` |
| S8 Hai vòng ngôn ngữ | proofreading + stop-slop, cổng academic-paper | `notes/proofreading/round*_report.md` |
| S9 Kiểm tra trùng lặp với bài gốc | — | `notes/09_overlap_audit.md` (xem §4) |
| S10 Bộ hồ sơ nộp | academic-paper (format) | `submission/JFIP_submission/` (xem §5) |
| S11 Ledger, commit, push | — | commit, rồi **push thẳng lên `main`** (người dùng muốn như vậy) |

Mỗi giai đoạn: ghi một mục vào `notes/AUDIT_LEDGER.md` (Iter n, các quyết định D-x và lý do).

### Gợi ý hướng câu hỏi (S1 phải tự kiểm chứng với dữ liệu thật)

Chọn theo biến mà bộ dữ liệu thực sự có, và **khác hẳn** câu hỏi của bài gốc. Ví dụ nếu bài gốc là "ESG và hiệu quả doanh nghiệp":
- ESG và **rủi ro giảm giá / tail risk** trong các cú sốc (COVID-2020, khủng hoảng trái phiếu 2022) → event study hoặc DiD theo cú sốc ngoại sinh.
- ESG và **thanh khoản cổ phiếu hoặc sở hữu nước ngoài** (dòng vốn, room ngoại).
- **Phản ứng giá khi công bố hoặc thay đổi điểm ESG** (event study, abnormal return).
- ESG và **chi phí vốn / định giá** (implied cost of capital), nếu dữ liệu có đủ biến.

Tiêu chí của JF:IP: bài dạng *Insights*, tức **một phát hiện thực nghiệm rõ ràng và chặt chẽ**, có chiến lược nhận diện (sự kiện ngoại sinh, DiD, IV, discontinuity), không chỉ là hồi quy tương quan.

---

## 3. Quy tắc viết (rút kinh nghiệm từ bài stock toán — người dùng đã yêu cầu tất cả những điều này)

- **Cấu trúc theo tạp chí:** lấy từ *Author Guidelines* của JF:IP. Phiên mới phải tìm và đọc hướng dẫn thật (WebSearch; nếu bị chặn thì nhờ người dùng upload PDF). Không được đoán giới hạn số từ, định dạng tham chiếu hay chính sách ẩn danh.
- Viết ra số liệu cụ thể thay vì tính từ mơ hồ; có khoảng tin cậy hoặc sai số chuẩn cho mọi kết quả suy luận; báo cáo cả kết quả không có ý nghĩa thống kê.
- **Bảng và hình:** mỗi bảng, hình được nhắc trong bài **trước khi xuất hiện**. Note dưới bảng **tối đa 2–3 câu**; có dòng "Source". Bảng gọn. Hình có nhãn trục đầy đủ, phân biệt các đường bằng kiểu nét và ký hiệu (in đen trắng vẫn đọc được), xuất EPS có nhúng font.
- **Ít ký hiệu toán trong phần văn;** công thức hiển thị được đánh số.
- **Discussion:** chỉ trích dẫn các tác giả đã được nhắc ở phần trước. Ở bài stock toán người dùng cấm thêm tài liệu mới; với bài mới có thể thêm tài liệu nhưng **phải có thật và đã kiểm tra**.
- **Không phóng đại:** không suy ra quan hệ nhân quả khi thiết kế không cho phép; không khái quát ra cả ASEAN từ dữ liệu một nước (chỉ nêu như giả thuyết).
- **Văn phong học thuật** (quyết định D14 của bài trước): áp dụng stop-slop trong khuôn khổ văn phong học thuật. Dùng "we" khi có chủ thể; không dùng "you"; bỏ trạng từ đệm và từ phóng đại; giữ trạng từ kỹ thuật. Không dùng em dash.
- **Viết tắt:** định nghĩa riêng trong abstract và định nghĩa lại ở lần dùng đầu trong thân bài.
- **Mục khai báo trước References:** Ethical standards, Data availability, Code availability, Funding, Conflict of interest, Declaration of generative AI use. Ghi **đúng các công cụ AI thật sự đã dùng** (Claude và cả Gemini nếu có dùng).

---

## 4. Kiểm tra trùng lặp với bài gốc (S9, bắt buộc trước khi nộp)

1. **Trùng văn bản:** viết script R (gói `stringdist` hoặc so khớp n-gram tự viết) tính tỷ lệ 8-gram trùng giữa bài mới và bài gốc, theo từng mục.
   - Mục tiêu: Introduction, Literature, Results, Discussion **gần 0%**.
   - Mô tả dữ liệu có thể giống một phần về nội dung nhưng **phải viết lại hoàn toàn** và trích dẫn companion study.
   - Ghi kết quả vào `notes/09_overlap_audit.md`.
2. **Trùng nội dung:** lập bảng đối chiếu từng bảng, hình, giả thuyết của bài mới với bài gốc (từ `00_original_paper_map.md`). Không được có cặp nào trùng.
3. **Mẫu:** nếu dùng cùng mẫu, ghi rõ; nếu lọc mẫu khác, nêu lý do.
4. Nếu bất kỳ mục nào không đạt → quay lại S4/S7 để sửa. Không nộp bài khi chưa đạt.

---

## 5. Bộ hồ sơ nộp (S10) — theo mẫu `B-i-stock-to-n/…/submission/APFM_submission/`

Script mẫu dựng bộ hồ sơ: `B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/`, gồm:
- `build_submission.py` (dựng bộ hồ sơ);
- `lib_docx.py` (sửa docx bằng lxml, giữ nguyên công thức OMML);
- `pack.sh` (đóng gói docx, file `[Content_Types].xml` phải nằm đầu);
- `checks.py` (kiểm tra tự động).

Thư mục `submission/JFIP_submission/` (chỉnh theo đúng yêu cầu của JF:IP):
```
00_CHECKLIST_NopBai.md        01_Title_Page.docx              02_Manuscript_Anonymized.docx
03_Figures/ (Fig1.eps…)        04_Declaration_of_Competing_Interest.docx
05_Replication_Package/ + .zip (code R + outputs + README đối chiếu bảng ↔ file output)
06_Cover_Letter.docx (có đoạn công khai companion study)   07_Manuscript_with_Author_Details.docx
08_Highlights.docx (chỉ khi tạp chí yêu cầu)
```

**Tác giả:** mặc định dùng cùng nhóm tác giả như bài trước, với thứ tự và thông tin như sau:

| Thứ tự | Tác giả | Học hàm, học vị / chức vụ | Đơn vị | Email | ORCID |
|---|---|---|---|---|---|
| 1 | Nguyen Thanh Binh | Dr., Ph.D., trưởng khoa Kinh tế | Academy of Policy and Development | nguyenthanhbinhapd@apd.edu.vn | 0009-0007-0042-2835 |
| 2 | **Nguyen Van Trung** (tác giả liên hệ) | — | Academy of Policy and Development | 15233582@st.neu.edu.vn; Tel +84 355 347 831 | 0009-0008-3307-6569 |
| 3 | Ha Hong Hanh | Assoc. Prof., Ph.D. | School of Accounting and Auditing, National Economics University | hanhhh@neu.edu.vn | 0000-0003-3581-6571 |
| 4 | Nguyen Bach Diep | Mr., M.Sc. | Academy of Policy and Development | diepnb@apd.edu.vn | 0009-0003-0967-7528 |

Nếu bài gốc ESG2 có nhóm tác giả khác, **dùng nhóm tác giả của bài gốc** và ghi quyết định vào ledger.

**Ẩn danh (bắt buộc kiểm tra bằng script):**
- Xoá `dc:creator` và `cp:lastModifiedBy` trong `docProps/core.xml`.
- Xoá `word/people.xml` (danh sách người sửa tracked changes; ở bài trước file này có tên cô Hạnh), cùng relationship và content type của nó.
- Assert: không còn tên, email hay domain đơn vị của tác giả trong bản ẩn danh.
- Đoạn "Author contributions" chỉ nằm ở Title Page. Người dùng từng tự thêm đoạn này vào bản ẩn danh, nên phải kiểm tra lại.

---

## 6. Hướng dẫn nộp bài trên hệ thống (để trả lời người dùng khi họ hỏi)

- **Tên tác giả trong form:** họ ở ô Family, ví dụ Given `Trung`, Middle `Van`, Family `Nguyen`. Người dùng đã nhập đảo nhiều lần.
- **Keywords:** 4–6 keyword theo thứ tự chữ cái (nếu tạp chí yêu cầu), phân cách bằng dấu chấm phẩy khi nhập vào form.
- **Hình:** EPS có nhúng font; PNG chỉ để dự phòng.
- **Replication package:** upload dạng Supplementary Material. Nếu không có loại file phù hợp, ghi chú ở ô Comments.
- **Luồng nộp bài:** Build PDF → View → kiểm tra (ẩn danh, hình, công thức) → Approve. Trạng thái "Incomplete" nghĩa là còn thiếu mục hoặc có file lỗi.
- **Không được bịa số liệu về tạp chí** (tỷ lệ nhận bài, Impact Factor…). Chỉ dẫn số có nguồn; nếu không có thì nói thẳng là không có.

---

## 7. Lưu ý kỹ thuật về môi trường (đã gặp ở phiên trước)

- **Mạng:**
  - Bị chặn: crossref, doi.org, CRAN, link.springer.com.
  - Kiểm tra tài liệu tham khảo bằng WebSearch.
  - Cài gói R qua `apt install r-cran-<gói>`, không dùng `install.packages`.
- **Docx:**
  - Sửa bằng lxml, giữ nguyên công thức OMML; `lxml` cài bằng pip.
  - Kiểm tra bằng `validate.py --original <file gốc>` của skill docx.
  - Render PDF bằng `HOME=/tmp/lohome soffice --headless --convert-to pdf`. LibreOffice không hiển thị công thức OMML; đó là do phần mềm, không phải file lỗi, nhưng phải nhắc người dùng mở bằng Word để kiểm tra.
- **Hình R:**
  - Dùng ggplot2 với `cairo_ps` để xuất EPS; nhãn Greek dùng plotmath hoặc `label_parsed`.
  - Kiểm tra nhãn trục và legend bằng cách xem ảnh PNG.
- **Git:**
  - Push lên nhánh làm việc được chỉ định, và **push thẳng lên `main`** khi xong (người dùng yêu cầu).
  - Commit message cuối có dòng attribution theo system reminder.
  - Không ghi tên model vào commit hay vào bài.
- **Tái lập:**
  - Chạy lại `run_all.R` với seed cố định, `cmp` với lần chạy trước; mọi CSV phải giống hệt.
  - Mọi con số trong bài phải so với file CSV. Nếu lệch, sửa bài hoặc sửa code và ghi vào ledger, không được im lặng.

---

## 8. Tiêu chí hoàn thành (Definition of Done)

- [ ] `CLAUDE.md`, hook và skill đã có trong B-i-ESG2; commit bootstrap.
- [ ] `00_original_paper_map.md` và `01_candidate_RQs.md` có kết luận: câu hỏi mới khác bài gốc.
- [ ] Pipeline R chạy từ đầu đến cuối và tái lập được; mọi số trong bài truy được về output.
- [ ] Đã phản biện full 5 ghế, sửa tối đa 2 vòng, phản biện lại; 2 vòng proofreading + stop-slop.
- [ ] `09_overlap_audit.md` đạt: văn bản gần 0% trùng ở các mục chính, không trùng bảng hay hình.
- [ ] Companion study được công khai trong bài (dạng ẩn danh) và trong cover letter.
- [ ] Tài liệu tham khảo có thật, đã kiểm tra; tuân thủ đúng Author Guidelines của JF:IP.
- [ ] Bộ hồ sơ `submission/JFIP_submission/` đủ file, bản ẩn danh sạch, docx hợp lệ.
- [ ] Ledger đầy đủ; đã push lên `main`; gửi người dùng tóm tắt và lệnh `git pull`.
