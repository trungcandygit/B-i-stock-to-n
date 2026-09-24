# Checklist nộp bài — Asia-Pacific Financial Markets (Springer)

**Bài:** Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam
**Tác giả (theo thứ tự):**
1. Nguyen Thanh Binh^a
2. Nguyen Van Trung^a,* (tác giả liên hệ)
3. Ha Hong Hanh^b
4. Nguyen Bach Diep^a

a: Academy of Policy and Development · b: National Economics University
**Hình thức bình duyệt:** double-blind, nên bản thảo nộp phải ẩn danh; thông tin tác giả chỉ nằm trong Title Page.
**Nộp tại:** springer.com/journal/10690 → "Submit manuscript" (Editorial Manager).

## 1. File trong thư mục này và loại file khi upload

| File | Upload với loại (Item type) | Bắt buộc? |
|---|---|---|
| `01_Title_Page.docx` | Title Page | Có: tên, đơn vị, email/điện thoại tác giả liên hệ, JEL, keywords, acknowledgements, COI, funding, CRediT, data/code availability |
| `02_Manuscript_Anonymized.docx` | Manuscript (blinded) | Có: không có tên tác giả (đã xoá cả metadata người sửa và danh sách người sửa tracked changes) |
| `03_Figures/Fig1.eps`, `Fig2.eps`, `Fig3.eps` | Figure (mỗi hình một file) | Có: file vector EPS; kèm PNG 600 dpi để dự phòng |
| `04_Declaration_of_Competing_Interest.docx` | Declaration / Conflict of interest | Tuỳ hệ thống: nếu không có mục riêng thì bỏ qua, vì nội dung đã có trong Title Page và cuối bản thảo |
| `05_Replication_Package.zip` | Electronic Supplementary Material, caption: *"Online Resource 1: R code and outputs that reproduce all tables and figures"* | Nên nộp: bài viết đã nhắc đến "Online Resource 1" |
| `06_Cover_Letter.docx` | Cover Letter | Nên nộp |
| `07_Manuscript_with_Author_Details.docx` | Không upload khi nộp lần đầu; chỉ dùng khi tạp chí yêu cầu bản có tên (sau khi được chấp nhận) | Không |
| `08_Highlights.docx` | APFM không yêu cầu highlights; chỉ dán vào nếu hệ thống có ô tương ứng | Không |

Thư mục `05_Replication_Package/` là bản giải nén của file zip, giữ lại để xem nhanh.

## 2. Kiểm tra theo hướng dẫn tác giả của APFM (đã đạt)

- [x] Abstract dài 150–250 từ (hiện 222 từ), không có viết tắt chưa định nghĩa.
- [x] 4–6 keywords, xếp theo thứ tự chữ cái (6 keywords); có mã JEL (C58, G11, G12).
- [x] Cấu trúc: Introduction / Methods / Results / Discussion (4.1–4.4).
- [x] Trích dẫn tên–năm; danh mục tài liệu có 23 mục, mục nào cũng được trích trong bài; có DOI.
- [x] Mọi bảng và hình được nhắc trong bài trước khi xuất hiện; note bảng tối đa 3 câu; có dòng "Source".
- [x] Trước danh mục tài liệu có các mục: Ethical standards, Data availability, Code availability, Funding, Conflict of interest, Declaration of generative AI use.
- [x] Double-blind: bản thảo và metadata không còn tên tác giả, không có câu tự trích dẫn để lộ danh tính.
- [x] Toàn bài dưới 8.500 từ (7.604 từ, tính cả bảng và tài liệu tham khảo).
- [x] Mọi con số trong bài đều truy được về output R (`05_Replication_Package/outputs`); chạy lại cho ra CSV giống hệt.

## 3. Việc tác giả cần tự làm trước khi bấm Submit

- [ ] Mở `02_Manuscript_Anonymized.docx` bằng Microsoft Word, kiểm tra 17 công thức (Word equation) hiển thị đúng. LibreOffice không hiển thị được loại công thức này.
- [ ] Cả 4 tác giả đọc và đồng ý bản cuối, kiểm tra lại thông tin trong Title Page (email, ORCID, CRediT).
- [ ] Kiểm tra số fax nếu hệ thống bắt buộc (hướng dẫn của APFM có nhắc fax; hiện chỉ có điện thoại).
- [ ] Khi hệ thống hỏi "funding": chọn "No funding".
- [ ] Đề xuất / loại trừ reviewer (tuỳ chọn), nhập trực tiếp trên hệ thống.
- [ ] Sau khi nộp, lưu file PDF mà hệ thống tạo ra (PDF build) và kiểm tra lại một lượt.
