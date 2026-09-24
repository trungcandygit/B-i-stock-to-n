# Phản hồi góp ý của cô (bản ngày 24/9) — bản thảo nộp Asia-Pacific Financial Markets

File nộp: `submission/final_APFM/Co_movement_manuscript_APFM_final.docx` (kèm `Title_Page.docx` và thư mục `figures/`).

## A. Ba comment của cô

| # | Comment của cô | Đã xử lý | Vị trí trong bản mới |
|---|---|---|---|
| 1 | “Institutional Context of HOSE” không nên nằm trong Data and Methodology; nên đưa vào phần mô tả Current Situation | Đã chuyển toàn bộ phần này ra khỏi Methods thành mục **1.1 Current Situation and Institutional Background of the HOSE** (thuộc Introduction). Cấu trúc bài theo đúng chuẩn tạp chí: 1 Introduction – 2 Methods – 3 Results – 4 Discussion and Conclusion. Các quy định pháp lý được viết lại cho chính xác (±7%, T+2, ATO/ATC, cấm bán khống, ký quỹ ban đầu ≥ 50%, Thông tư 68/2024 chỉ bỏ yêu cầu ký quỹ trước cho NĐT tổ chức nước ngoài). | §1.1 |
| 2 | “Thiếu nguồn tham khảo của bảng” (gắn ở Hình 1) | Mọi bảng và hình đều có dòng **Source: Authors’ calculations based on HOSE index data (TradingView)**. Mỗi bảng/hình đều được dẫn trong văn bản trước khi xuất hiện; phần Notes rút gọn còn 2–3 câu. | Hình 1–3, Bảng 1–7 |
| 3 | Mục 6 đặt tên chưa phù hợp; cần là Conclusion and Future Research | Đổi thành **4 Discussion and Conclusion** (khớp cấu trúc Introduction/Methods/Results/Discussion của tạp chí), gồm 4.1 Implications for ASEAN Capital Markets và **4.2 Limitations and Future Research** (mới, nêu rõ hướng nghiên cứu tiếp). | §4 |

## B. Các chỗ cô sửa trực tiếp (tracked changes)

Đã chấp nhận toàn bộ 56 chỗ chèn và 38 chỗ xóa của cô, giữ nguyên văn phong cô sửa (ví dụ “Utilizing…”, “illustrates…”, “Furthermore…”, “Consequently…”, “These research findings highlight the imperative…”, các câu chuyển sang bị động ở phần Data/Methods). Đã sửa các lỗi kỹ thuật phát sinh khi chèn: dấu cách thừa trong Abstract, thiếu dấu chấm (“equitiesThis”, “return paths Consequently”), dấu “..” kép, và câu “T is evaluated…”.

## C. Những thay đổi quan trọng khác (em phải báo cô)

1. **Chạy lại toàn bộ thực nghiệm bằng R** (`project_R/run_all.R`); mọi con số trong bài lấy từ output R. R tái lập chính xác các giá trị DCCA của pipeline Python cũ.
2. **Bỏ toàn bộ kết quả VN70 (VNMIDCAP)**: dữ liệu, code và file Excel của hình đều không có chuỗi VN70, nên các con số VN70 trong bản cũ không có nguồn. Theo nguyên tắc liêm chính (không được bịa dữ liệu), em đã bỏ các con số này, giữ P_cap làm proxy mid-cap, và đưa việc đối chiếu với VN70 vào mục hạn chế/hướng nghiên cứu.
3. **Kết luận Forbes–Rigobon thay đổi**: bản cũ ghi Panel A (khủng hoảng theo giai đoạn) có ρ_low = 0.629 và t = 7.71. Chạy lại đúng theo định nghĩa (539 ngày khủng hoảng, 1.000 ngày bình thường) thì ρ_low = 0.844, tương quan sau điều chỉnh ρ* = 0.803 và t = −2.28, tức **không có đột biến cấu trúc**. Panel B khớp với bản cũ (t = 0.97, p = 0.165). Vì vậy bài được viết lại theo hướng “interdependence, not contagion”: tương quan tăng trong khủng hoảng là do biến động tăng. Hàm ý quản trị rủi ro vẫn giữ nguyên.
4. **Các con số khác được cập nhật theo R**: Bảng 1 (skewness/kurtosis cũ sai), Bảng 3 (ngưỡng tin cậy từ 1.002 lần mô phỏng Monte Carlo thật), Bảng 7 (chiều tác động của trọng số bị ngược trong bản cũ), độ rộng phổ đa phân dạng, và sai số danh mục (+15,63% theo chế độ rolling, +2,44% theo giai đoạn).
5. **Tiêu chí chọn giai đoạn khủng hoảng**: năm 2018 chỉ giảm 26,2%, không đạt ngưỡng 30% như bản cũ ghi. Tiêu chí được sửa thành: giảm hơn 25% và ít nhất 45% số ngày nằm trong nhóm biến động cao, đều tính từ dữ liệu.
6. **Tài liệu tham khảo**: đã kiểm tra từng tài liệu. Bỏ 4 tài liệu không xác minh được (Goh & Wong 2020, Vo 2017, Nguyen & Nguyen 2021, Lee & Azali 2012). Sửa sai thông tin của Epps (1979) (đúng là JASA 74(366), 291–298), Karim & Ning (2013) và Lean & Teng (2013). Không thêm tác giả mới. Trích dẫn theo kiểu Springer, ví dụ (Hong and Stein 1999).
7. **Chuẩn tạp chí APFM**: Abstract 198 từ; 6 keywords theo thứ tự ABC; JEL; heading thập phân tối đa 3 cấp; chú thích hình dạng “**Fig. 1** …”; hình dùng font sans-serif, có file EPS riêng; bản thảo ẩn danh; trang tiêu đề riêng (tên tác giả, CRediT, Funding) — **cô/nhóm cần điền phần bôi vàng trong `Title_Page.docx`**. Tổng độ dài khoảng 8.080 từ (< 8.500).
8. Giảm ký hiệu toán trong văn xuôi, giữ lại các phương trình hiển thị.
