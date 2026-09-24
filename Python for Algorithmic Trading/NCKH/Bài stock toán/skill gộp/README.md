# Master Academic Paper Writing, Proofreading & Peer Review Skill (Skill Gộp)

**Kho Tổng Hợp Đỉnh Cao Về Viết, Soát Lỗi, Phản Biện & Giải Trình Bài Báo Học Thuật Đẳng Cấp Quốc Tế (Top Field / Top 5 Journals)**

---

## 📖 Giới Thiệu & Nguồn Gốc

Thư mục **`skill gộp`** là kết quả tích hợp toàn diện, sâu sắc và loại bỏ hoàn toàn trùng lặp từ toàn bộ hệ sinh thái các kỹ năng học thuật hàng đầu thế giới:
1. **`paper-writing-skill` & `paper-writing` (SNL Lab / UC Santa Barbara & Arpit Gupta)**: Quy trình viết bài 5 giai đoạn, 14 nguyên tắc biên tập, cổng cơ học (Mechanical Gate), cổng ngữ nghĩa (Semantic Gate), nén câu chữ (Compression Patterns), tổng hợp Figure 1 và TikZ.
2. **`econ-writing-skill` (`econ-write` - Lu Han & OpenEcon)**: Đúc kết từ hơn 50 cẩm nang của các giáo sư kinh tế học lừng danh (John Cochrane, Jesse Shapiro, Claudia Goldin, Marc Bellemare, Deirdre McCloskey).
3. **`econ-paper-review-skill` (`econ-review` - Lu Han)**: Chuẩn mực phản biện khắt khe của trọng tài Top-5 kinh tế (AER, QJE, JFE, Econometrica), tái thiết lập luận điểm, kiểm định nội sinh và sổ cái phát hiện lỗi (Findings Ledger).
4. **`proofreading` (Jakob Thumm - TU Munich)**: Bộ kiểm tra soát lỗi học thuật toàn diện với hơn 100 tiêu chí: ký hiệu toán học, cấu trúc bài, độ vững thống kê, bảng LaTeX `booktabs`, chữ viết tắt.
5. **`humanizer_academic` (Wikipedia Academic Slop Guide)**: Khử sạch triệt để các dấu vết văn phong do AI sinh ra (*delve, testament, pivotal, beacon, tapestry, multifaceted...*), cấm gạch ngang em-dash (`---`), tái cấu trúc nhịp điệu câu phong phú.
6. **`econ-management-paper-polish` (linkingoscar)**: Nguyên tắc Evidence-First, kiểm định tính liêm chính của trích dẫn (chống ảo giác / hallucination), chuẩn hóa văn phong kinh tế & quản lý.
7. **`open-phrasebank` (Manchester Academic Phrasebank)**: Ngân hàng mẫu câu học thuật kinh điển được phân loại chi tiết theo từng chức năng giao tiếp khoa học.
8. **`ChatReviewer` & `ChatResponse` (nishiwen1214)**: Quy trình phản biện độc lập và cấu trúc ma trận giải trình phản biện (Rebuttal / Author Response) từng điểm kèm mã diff văn bản.
9. **`Auto-Empirical-Research-Skills` & `econ-paper-workflow` (Stanford REAP & CoPaper)**: Bộ tiêu chuẩn ước lượng kinh tế lượng, suy diễn nhân quả (DiD, IV, RDD, SCM) và ma trận kiểm định độ vững (Oster bounds, placebo tests).

### ❌ Các phần ĐÃ ĐƯỢC LOẠI BỎ theo yêu cầu:
- **Loại bỏ hoàn toàn kỹ năng làm Slide (`econ-slides-skill`)**: Toàn bộ trọng tâm và năng lượng được dồn 100% vào việc hoàn thiện bản thảo bài báo (manuscript) đạt chuẩn đăng ký tại các tạp chí Scopus/SSCI Q1 và Top Field.
- **Loại bỏ trùng lặp (Deduplication)**: Hợp nhất các danh sách từ cấm, tích hợp các checklist rời rạc thành 1 bảng kiểm duy nhất 120 tiêu chuẩn, thống nhất các nguyên tắc viết của Cochrane và Arpit Gupta thành một triết lý biên tập mạch lạc.

---

## 📂 Cấu Trúc Thư Mục Chuẩn Hóa

```
skill gộp/
├── SKILL.md                                  # File cấu hình & điều khiển trung tâm (Agent Router)
├── README.md                                 # Tài liệu hướng dẫn sử dụng chi tiết này
├── rules/                                    # CÁC QUY TẮC BẤT DI BẤT DỊCH
│   ├── 01_master_editorial_philosophy.md     # 14 nguyên tắc biên tập, văn phong tam giác ngược, punchline trước
│   ├── 02_mechanical_and_anti_ai_gate.md    # Cổng kiểm tra từ cấm AI, cấm em-dash, regex audit
│   ├── 03_semantic_and_logic_gate.md        # Cổng ngữ nghĩa: định nghĩa trước khi dùng, chống ảo giác
│   ├── 04_econometric_and_empirical_standards.md # Chuẩn mực kinh tế lượng: DiD, IV, RDD, Panel FE, Oster bounds
│   ├── 05_latex_tables_and_math_notation.md # Chuẩn bảng booktabs, ký hiệu toán học vector/matrix, dấu câu phương trình
│   └── 06_figure_synthesis_and_visuals.md  # Nguyên tắc Figure 1 trang đầu, chú thích tự giải thích, mẫu TikZ
├── section_playbooks/                        # CẨM NANG VIẾT TỪNG PHẦN CỦA BÀI BÁO
│   ├── 01_title_and_abstract.md             # Tiêu đề & Tóm tắt (100–150 từ, viết sau cùng, không trích dẫn)
│   ├── 02_introduction.md                   # 5 bước chuyển dịch tu từ (Hook, Problem, Gap, Solution, Contributions)
│   ├── 03_literature_review_and_gaps.md     # Tổng quan y văn theo chủ đề, đối chiếu chiều kích, nêu bật khoảng trống
│   ├── 04_theoretical_model.md              # Khung lý thuyết: trực giác kinh tế trước, điều kiện bậc nhất, giả thuyết
│   ├── 05_empirical_design_and_id.md        # Dữ liệu, quy trình lọc mẫu, phương trình hồi quy, nhận diện ngoại sinh
│   ├── 06_results_and_mechanisms.md         # Bảng kết quả chuẩn, diễn giải ý nghĩa kinh tế, đua ngựa cơ chế
│   ├── 07_robustness_and_threats.md         # Ma trận kiểm định độ vững, kiểm định giả (placebo), giới hạn Oster
│   └── 08_conclusion_and_implications.md    # Kết luận 4 đoạn: đúc kết, hàm ý chính sách, giới hạn trung thực
├── peer_review_and_rebuttal/                 # PHẢN BIỆN & GIẢI TRÌNH PHẢN BIỆN
│   ├── referee_review_protocol.md           # Quy trình đóng vai phản biện Top-5, lập sổ cái phát hiện lỗi
│   └── author_response_rebuttal_guide.md    # Ma trận giải trình từng điểm, trích dẫn văn bản sửa đổi, nghệ thuật ngoại giao
├── reference_phrasebanks/                    # NGÂN HÀNG MẪU CÂU HỌC THUẬT
│   ├── master_academic_phrasebank.md        # Tuyển chọn mẫu câu tinh hoa nhất theo từng chức năng tu từ
│   └── manchester_phrasebank_raw.md         # Toàn văn cơ sở dữ liệu mẫu câu Manchester Phrasebank
├── checklists/                              # BẢNG KIỂM TRA CHẤT LƯỢNG
│   └── master_120_point_proofreading_checklist.md # 120 tiêu chí kiểm duyệt toàn diện trước khi nộp bài
├── protocols/                               # QUY TRÌNH NÂNG CAO
│   ├── red_team_adversarial_protocol.md     # Quy trình kiểm định đối kháng Red-Team tìm lỗ hổng trước reviewer
│   └── iterative_loop_mode.md               # Vòng lặp hội tụ tự động từng phần (Draft -> Mech -> Sem -> Converged)
└── figure_templates/                        # MẪU THIẾT KẾ ĐỒ HỌA & TIKZ
    ├── figure_spec_template.md
    ├── prompt_templates.md
    ├── tikz_skeletons.md
    └── venue_styles.md
```

---

## 🎯 6 Chế Độ Hoạt Động Của Skill (Operational Modes)

Khi làm việc với AI Agent (Antigravity, Claude Code, Cursor, Codex), bạn có thể kích hoạt các chế độ chuyên biệt:

### 1. Viết Mới Từng Phần (`/draft [tên phần]`)
- **Ví dụ**: *"Dùng skill gộp để viết phần Introduction cho bài nghiên cứu về Regime-switching DCCA trên thị trường chứng khoán Việt Nam."*
- **Quy trình**: Agent tải `section_playbooks/02_introduction.md`, áp dụng 5 bước tu từ kinh điển, đưa kết quả chính lên ngay đoạn 1 và 2, kiểm soát văn phong tam giác ngược.

### 2. Khử Văn Phong AI & Nâng Cấp Câu Chữ (`/polish [file hoặc đoạn văn]`)
- **Ví dụ**: *"Khử toàn bộ mùi AI và gọt giũa đoạn văn này theo chuẩn mechanical gate của skill gộp."*
- **Quy trình**: Quét sạch các từ cấm (*delve, testament, pivotal, beacon...*), xóa 100% gạch ngang em-dash (`---`), hạ tỷ lệ câu bị động xuống dưới 15%, tái phân bổ nhịp điệu câu linh hoạt.

### 3. Soát Lỗi Toàn Diện 120 Tiêu Chí (`/proofread [file.tex]`)
- **Ví dụ**: *"Soát lỗi toàn bộ file `main.tex` theo checklist 120 tiêu chuẩn của skill gộp."*
- **Quy trình**: Kiểm tra chuẩn bảng `booktabs` (cấm tuyệt đối đường kẻ dọc), dấu câu phương trình, ký hiệu toán vector/matrix, quy tắc mở rộng viết tắt, khoảng trắng không ngắt (`~cite{...}`).

### 4. Đóng Vai Trọng Tài Top-5 Đánh Giá Bài Báo (`/review [bản thảo]`)
- **Ví dụ**: *"Hãy đóng vai phản biện của Journal of Financial Economics (JFE) để audit chiến lược nhận diện của bài báo này."*
- **Quy trình**: Tái thiết lập các tuyên bố khoa học, soi xét giả định ngoại sinh, kiểm tra hiện tượng Bad Controls, phân loại lỗ hổng thành Fatal Flaws (Tử huyệt) / Major Concerns / Minor Fixes.

### 5. Viết Thư Giải Trình Phản Biện (`/rebuttal [comments]`)
- **Ví dụ**: *"Dùng ma trận giải trình của skill gộp để viết phản hồi từng điểm cho nhận xét phản biện sau."*
- **Quy trình**: Lập bảng ma trận: Lời cảm ơn chân thành ➔ Câu trả lời trực diện kèm bằng chứng định lượng ➔ Trích đoạn văn bản chỉnh sửa chính xác kèm số trang/dòng.

### 6. Kiểm Định Đối Kháng Red-Team (`/redteam [đoạn văn/phần]`)
- **Ví dụ**: *"Chạy Red-Team kiểm tra xem lập luận trong phần Cơ chế (Mechanisms) này có bị tấn công không."*
- **Quy trình**: Đóng vai một chuyên gia đối kháng siêu hoài nghi, tìm ra các giả định ngầm chưa được chứng minh, các biến ngoại sinh bị nghi ngờ, và nguy cơ kết quả bị vô nghĩa về mặt kinh tế (economic insignificance).

---

## ⚡ Kiểm Tra Nhanh Bằng Dòng Lệnh (Grep Audit)

Bạn có thể chạy trực tiếp bộ lệnh sau trong terminal để kiểm tra bài báo LaTeX của mình:

```bash
# Di chuyển vào thư mục bài viết
cd "/path/to/your/paper"

# 1. Kiểm tra dấu gạch ngang em-dash (Cấm tuyệt đối)
grep -rnE "(---|—| – )" *.tex sections/*.tex

# 2. Kiểm tra từ ngữ sáo rỗng AI
grep -rinE "\b(delve|testament|underscores|underpins|pivotal|beacon|tapestry|paramount|multifaceted|nuanced|shed light on|foster|vibrant|realm|interplay|meticulous|relentless|burgeoning|revolutionize|game-changer|quintessential|symbiotic|bespoke|utilize)\b" *.tex sections/*.tex

# 3. Kiểm tra mở đầu câu rườm rà (Throat-clearing)
grep -rnE "^(Moreover|Furthermore|Additionally|Notably|Importantly|Crucially|Indeed|It is worth noting that|It should be noted that)\b" *.tex sections/*.tex
```

---

## 🌟 Cam Kết Chất Lượng

Bản thảo được tinh chỉnh qua **`skill gộp`** đảm bảo:
- Văn phong khách quan, đanh thép, chắc chắn, giàu dữ kiện (Evidence-Forward).
- Đưa kết quả và đóng góp lên hàng đầu ngay từ những câu đầu tiên.
- Sạch 100% các lỗi văn phong AI slop mà các hội đồng và reviewer quốc tế thường gắn cờ.
- Chuẩn hóa toán học và bảng biểu LaTeX theo đúng chuẩn mực của các nhà xuất bản hàng đầu thế giới (Elsevier, Springer, Wiley, Oxford University Press, Chicago University Press).
