# FORCE RULES — yêu cầu dán vào phiên mới (bài ESG mới → Journal of Finance: Insights and Perspectives)

> Dán nguyên khối dưới đây làm tin nhắn đầu tiên, hoặc chèn vào đầu CLAUDE.md của repo B-i-ESG2.
> Các quy tắc được rút ra từ bài stock toán, gồm cả những lỗi đã mắc và phải sửa ở bài đó.

```
=== FORCE RULES — BẮT BUỘC 100%, KHÔNG NGOẠI LỆ ===

A. CÁCH LÀM VIỆC
A1. CỨ LÀM, KHÔNG HỎI LẠI. Tôi đã uỷ quyền trước cho mọi bước. Không dừng ở bất kỳ checkpoint "user must confirm" nào của skill ARS / proofreading / stop-slop; không dùng AskUserQuestion. Chỗ nào cần chọn → tự chọn mặc định hợp lý nhất theo skill, ghi quyết định + lý do vào notes/AUDIT_LEDGER.md. Chỉ dừng khi (a) thiếu dữ liệu không thể suy ra, hoặc (b) bước tiếp theo vi phạm liêm chính — khi đó ghi ledger, làm hết phần còn lại, báo tôi 1 lần.
A2. SKILL: đọc toàn bộ HANDOFF_NEW_PAPER_ESG.md (repo trungcandygit/B-i-stock-to-n, nhánh main) trước tiên. academic-pipeline điều phối; deep-research (đọc bài gốc, chọn câu hỏi, phương pháp), academic-paper (viết, citation-check, revision), academic-paper-reviewer (full 5 ghế + re-review 3 cổng), proofreading + stop-slop (2 vòng ngôn ngữ, mỗi vòng qua cổng academic-paper). Mỗi skill load MỘT lần mỗi phiên, không gọi lại, nhưng tuân thủ 100% SKILL.md.
A3. VÒNG: 1 phản biện full → sửa → re-review (tối đa 2 vòng revision theo IRON RULE) → 2 vòng proofreading + stop-slop. Tự đi hết S0→S11, không chờ lệnh "làm tiếp".
A4. R: mọi phân tích, bảng, hình làm bằng R (project_R/run_all.R, cố định seed, outputs/). Mỗi con số trong bài phải truy được về 1 file CSV output. Chạy lại toàn bộ trước khi nộp: CSV phải byte-identical. Số lệch → sửa bài hoặc code, ghi ledger, KHÔNG im lặng.
A5. Xong: commit, push thẳng lên main, gửi tôi tóm tắt + lệnh git pull.

B. LIÊM CHÍNH (IRON RULE — "không hỏi lại" KHÔNG cho phép bỏ qua)
B1. Bài mới khác bài gốc ESG2 ở câu hỏi, phân tích, kết quả. Cấm paraphrase, cấm tái dùng đoạn văn / bảng / hình, cấm chia một kết quả thành hai bài. Công khai dùng chung dữ liệu: bản ẩn danh ghi "a companion study (details withheld for anonymous review)"; cover letter ghi rõ bài gốc và tình trạng.
B2. Trước khi nộp: kiểm tra trùng lặp bằng R (tỷ lệ 8-gram trùng theo từng mục; Intro/Lit/Results/Discussion ≈ 0%) + bảng đối chiếu từng bảng/hình/giả thuyết với bài gốc → notes/09_overlap_audit.md. Không đạt thì không nộp.
B3. Không bịa dữ liệu. Biến nào không có trong dữ liệu thật thì bỏ hẳn phân tích đó và ghi là hạn chế. (Bài trước: chuỗi VN70 không có → phải xoá toàn bộ kết quả VN70.)
B4. Không bịa trích dẫn: mọi tài liệu tham khảo phải có thật, kiểm tra tác giả / năm / tạp chí / tập / trang / DOI bằng WebSearch; không xác minh được thì bỏ. Không bịa số liệu về tạp chí (tỷ lệ nhận bài, IF): chỉ dẫn số có nguồn.
B5. Khai báo AI đúng công cụ đã dùng thật (Claude, và Gemini nếu có dùng).

C. TẠP CHÍ & CẤU TRÚC
C1. Tìm và đọc Author Guidelines thật của Journal of Finance: Insights and Perspectives (WebSearch/WebFetch; bị chặn thì dừng và nhờ tôi upload PDF — KHÔNG đoán). Lấy đúng: loại bài (Insights), giới hạn từ, số bảng/hình tối đa, abstract, keywords, JEL, định dạng tham chiếu, ẩn danh, highlights, internet appendix, phí APC.
C2. Cấu trúc đúng như tạp chí yêu cầu; mặc định: Title – Abstract – Introduction – Data/Methods – Results – Discussion/Conclusion. Tiêu đề mục đánh số nhất quán, roadmap cuối Introduction khớp đúng số và tên mục. Không tạo "pseudo-heading" (dòng in đậm có dấu hai chấm giữa đoạn).
C3. SỐ TỪ: tuân thủ tuyệt đối giới hạn của tạp chí. Đếm bằng script (toàn bài kể cả bảng, tài liệu tham khảo, trừ khi guideline nói khác) và ghi số từ vào ledger sau mỗi vòng. Abstract đúng giới hạn (đếm riêng). Bài Insights phải gọn: kết quả phụ → Internet Appendix.
C4. Keywords đúng số lượng yêu cầu, xếp chữ cái nếu tạp chí yêu cầu; có JEL codes.

D. BẢNG (lỗi bài trước: note quá dài, caption sai nội dung, bảng rời rạc)
D1. Mỗi bảng được NHẮC TRONG BÀI TRƯỚC KHI XUẤT HIỆN, và đoạn văn phải diễn giải bảng (không chỉ "xem Bảng 3").
D2. Caption: "Table n" in đậm + mô tả ngắn đúng nội dung thật của bảng (bài trước Bảng 6 ghi nhầm "(M30)" trong khi báo cáo 1D/H1/H4). Kiểm tra caption ↔ nội dung bảng bằng script sau mỗi lần sửa.
D3. NOTE DƯỚI BẢNG: TỐI ĐA 2–3 CÂU, kèm dòng "Source: …". Không giải thích phương pháp trong note — phương pháp nằm ở Methods.
D4. Bảng gọn: ít cột, bỏ cột không dùng đến trong phần thảo luận; số chữ số thập phân nhất quán trong cùng cột; dấu âm là "−"; ký hiệu ý nghĩa thống kê giải thích 1 lần trong note; có khoảng tin cậy hoặc sai số chuẩn cho mọi ước lượng suy luận.
D5. Mọi ô số điền tự động từ CSV output R bằng script (không gõ tay). Sau khi điền, so tự động mọi số trong bảng và trong văn với CSV.
D6. Làm tròn nhất quán: số trong văn phải khớp số đã làm tròn trong bảng (bài trước: văn ghi 0.052 nhưng bảng cho 0.977−0.924 = 0.053 → phải sửa).

E. HÌNH (lỗi bài trước: thiếu nhãn trục, font Greek hỏng)
E1. Mỗi hình được nhắc trước khi xuất hiện; caption "Fig. n" + mô tả; notes ≤ 2–3 câu, giải thích mọi kiểu nét / ký hiệu / vùng tô, có "Source".
E2. Đủ nhãn trục x và y (có đơn vị), legend không che dữ liệu, không tiêu đề bên trong hình (tiêu đề nằm ở caption).
E3. Đen trắng đọc được: phân biệt bằng kiểu nét + marker, không chỉ bằng màu; cùng một chuỗi dùng cùng ký hiệu ở mọi hình.
E4. Xuất bằng R (ggplot2): EPS có nhúng font (cairo_ps) + PNG 600 dpi; tên Fig1.eps, Fig2.eps…; ký tự Greek dùng plotmath/label_parsed. Mở PNG ra xem trực tiếp để kiểm tra trước khi chèn.
E5. Số hình/bảng trong bài chính không vượt giới hạn tạp chí; phần còn lại vào Internet Appendix.

F. VĂN BẢN
F1. Ít ký hiệu toán trong phần văn: dùng lời khi có thể; công thức hiển thị đánh số (1), (2)…; mỗi ký hiệu được định nghĩa ngay tại lần dùng đầu.
F2. Không phóng đại: không nói nhân quả khi thiết kế không cho phép; không khái quát ra ASEAN / thị trường khác từ dữ liệu 1 nước (chỉ nêu như giả thuyết); "không bác bỏ H0" ≠ "chứng minh không có tác động" — báo cáo power khi kết quả không có ý nghĩa.
F3. Báo cáo cả kết quả không có ý nghĩa thống kê và các hạn chế (một mục Limitations riêng).
F4. Discussion chỉ trích dẫn các tác giả đã được nhắc ở phần trước; không đưa tài liệu mới vào Discussion.
F5. Methods mô tả cái gì và làm thế nào — không lặp lại động cơ nghiên cứu ("To guarantee…", "To preserve…"). Không dùng "guarantee / prove / verify / ensure" khi không có chứng minh.
F6. Viết tắt: định nghĩa trong abstract (riêng) và lại ở lần dùng đầu trong thân bài; sau đó dùng nhất quán. (Bài trước thiếu định nghĩa: ASEAN, OLS, GARCH.)
F7. Văn phong: American English; stop-slop theo văn phong học thuật (we-voice, không "you", bỏ trạng từ đệm/phóng đại: genuinely, strictly, markedly, fundamentally, critical, robust khi không có số…); không em dash; "First/Second/Third" (không "Firstly"); dấu phẩy Oxford: chọn một kiểu và nhất quán toàn bài; không câu lặp ý ở hai đoạn liền nhau.
F8. Tham chiếu chéo đúng: "Section x.y", "Table n", "Eq. (n)" phải tồn tại. Chạy script kiểm tra sau mỗi lần đổi cấu trúc (bài trước: bỏ mục 1.1 nhưng vẫn còn "(Section 1.1)").
F9. Mọi tuyên bố định lượng trong abstract / introduction / conclusion phải trùng khớp với Results.

G. DOCX & HỒ SƠ NỘP
G1. Sửa docx bằng script lxml (giữ công thức OMML), markup subscript/superscript/italic xử lý đúng (bài trước lọt ký tự thô "P_{cap}"); validate docx sau mỗi lần build; render PDF (LibreOffice không hiện OMML — nhắc tôi mở Word kiểm tra công thức).
G2. Bản ẩn danh: không tên/email/đơn vị tác giả trong text; xoá docProps creator/lastModifiedBy; xoá word/people.xml (danh sách người sửa tracked changes); đoạn "Author contributions" CHỈ ở Title Page; không self-citation lộ danh tính. Script assert không còn tên tác giả trước khi đóng gói.
G3. Bộ hồ sơ submission/JFIP_submission/: 00_CHECKLIST (tiếng Việt, map file ↔ item type), 01_Title_Page, 02_Manuscript_Anonymized, 03_Figures (EPS+PNG), 04_Declaration_of_Competing_Interest, 05_Replication_Package (+.zip, README map bảng ↔ CSV, không kèm dữ liệu gốc nếu điều khoản nhà cung cấp cấm), 06_Cover_Letter (có đoạn công khai companion study, đúng scope tạp chí bằng chính từ ngữ của tạp chí), 07_Manuscript_with_Author_Details, 08_Highlights (chỉ nếu tạp chí yêu cầu).
G4. Tác giả (thứ tự): 1 Nguyen Thanh Binh (Dr., Ph.D.; Academy of Policy and Development), 2 Nguyen Van Trung* (corresponding; APD; 15233582@st.neu.edu.vn; +84 355 347 831), 3 Ha Hong Hanh (Assoc. Prof., Ph.D.; School of Accounting and Auditing, National Economics University), 4 Nguyen Bach Diep (Mr., M.Sc.; APD). Email/ORCID xem HANDOFF §5. Nếu bài gốc có nhóm tác giả khác → theo bài gốc, ghi ledger.
G5. Khi hướng dẫn nhập form nộp bài: họ (Nguyen / Ha) ở ô Family, tên ở Given, đệm ở Middle.

H. KIỂM TRA CUỐI (script, ghi kết quả vào ledger — tất cả phải PASS)
[ ] số từ toàn bài & abstract ≤ giới hạn   [ ] mọi bảng/hình được nhắc trước khi xuất hiện   [ ] mọi note ≤ 3 câu
[ ] caption khớp nội dung   [ ] mọi số trong văn/bảng = CSV R   [ ] chạy lại R: CSV byte-identical
[ ] mọi trích dẫn có trong References và ngược lại, đều đã xác minh   [ ] tham chiếu chéo tồn tại
[ ] viết tắt đã định nghĩa   [ ] không em dash   [ ] bản ẩn danh sạch (text + metadata + people.xml)
[ ] overlap audit với bài gốc PASS   [ ] docx validate PASS   [ ] đúng Author Guidelines từng mục
```
