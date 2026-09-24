# Tài liệu mô tả dữ liệu & Kế hoạch nghiên cứu
## Tương quan chéo đa thang thời gian (DCCA/MF-DCCA) giữa VNINDEX, VN30, VN100 và hàm ý cho danh mục đầu tư

---

## 1. Tổng quan bộ dữ liệu

Hai file dữ liệu được tạo từ việc gộp (merge) các chỉ số chứng khoán Việt Nam (VNINDEX, VN30, VN100) và tỷ giá USD/VND, ở 4 khung thời gian khác nhau (30 phút, 1 giờ, 4 giờ, 1 ngày), phục vụ phân tích tương quan chéo theo nhiều thang thời gian.

| File | Mô tả |
|---|---|
| `vn_indices_merged_raw.csv` | Bản **gốc**, còn giữ nguyên các ô trống (`NaN`) ở cột `USDVND` |
| `vn_indices_merged_filled.csv` | Bản **đã lấp khoảng trống** (forward-fill) ở cột `USDVND` |

Cả hai file có cùng cấu trúc cột và số dòng: **43,842 dòng** (gộp cả 4 khung thời gian).

---

## 2. Nguồn dữ liệu gốc

Dữ liệu được tổng hợp từ các file CSV xuất từ TradingView (sàn HOSE), gồm các mã: `VNINDEX`, `VN30`, `VN100` ở 4 khung thời gian, và `USDVND` (chỉ có bản ngày).

| Timeframe | File nguồn dùng (VN30 / VN100 / VNINDEX) | Lý do chọn |
|---|---|---|
| 1D | `HOSE_DLY_VN301D.csv` / `HOSE_DLY_VN1001D.csv` / `HOSE_DLY_VNINDEX1D.csv` | Bản mới nhất, có cột Volume thật, dữ liệu tới 12/2025 |
| M30 | `HOSE_DLY_VN3030.csv` / `HOSE_DLY_VN10030.csv` / `HOSE_DLY_VNINDEX30.csv` | Tương tự, tới 12/2025 |
| H1 | `HOSEVN30H1.csv` / `HOSEVN100H1.csv` / `HOSEVNINDEXH1.csv` | Không có bản mới hơn, chỉ tới 12/2024 |
| H4 | `HOSEVN30H4.csv` / `HOSEVN100H4.csv` / `HOSEVNINDEXH4.csv` | Không có bản mới hơn, chỉ tới 12/2024 |
| USDVND | `USDVND1D.csv` | Chỉ có dữ liệu ngày, dữ liệu tới 12/2024 |

**File bị loại (không dùng):** các bản trùng lặp cũ hơn không có hậu tố `_DLY_` cho khung 1D và M30 (VD: `HOSEVN301D.csv`, `HOSEVN30M30.csv`...) — vì đã bị thay thế bởi bản `_DLY_` mới hơn, đầy đủ hơn (có Volume thật thay vì cột `Plot` toàn `NaN`).

---

## 3. Mô tả từng cột

| Cột | Kiểu dữ liệu | Ý nghĩa |
|---|---|---|
| `timeframe` | text | Khung thời gian của dòng dữ liệu: `1D` (ngày), `M30` (30 phút), `H1` (1 giờ), `H4` (4 giờ). Dùng để lọc dữ liệu theo từng thang thời gian khi phân tích. |
| `time` | integer (Unix timestamp) | Thời điểm nến (candle), tính bằng số giây kể từ 01/01/1970 UTC. |
| `datetime` | text | Thời điểm đọc được của `time`. Với `timeframe = 1D`: chỉ hiện `YYYY-MM-DD` (vì bản chất là dữ liệu theo ngày, phần giờ chỉ là artifact kỹ thuật khi convert timestamp — không mang ý nghĩa). Với `M30/H1/H4`: hiện đầy đủ `YYYY-MM-DD HH:MM:SS`. |
| `VN30` | float | Giá đóng cửa (close) của chỉ số VN30 tại thời điểm `time`. |
| `VN100` | float | Giá đóng cửa (close) của chỉ số VN100 tại thời điểm `time`. |
| `VNINDEX` | float | Giá đóng cửa (close) của chỉ số VNINDEX tại thời điểm `time`. |
| `USDVND` | float | Giá đóng cửa (close) của tỷ giá USD/VND tại **ngày** tương ứng (không phải theo giờ, vì USDVND gốc chỉ có dữ liệu ngày). Dùng làm **biến kiểm soát phụ**, không phải biến chính trong phân tích DCCA giữa 3 chỉ số. |

**Lưu ý về `VN30`, `VN100`, `VNINDEX`:** ba cột này đã được **inner-join theo `time`**, nghĩa là chỉ giữ lại các mốc thời gian mà **cả 3 chỉ số đều có dữ liệu đồng thời** → không có ô trống ở 3 cột này, dữ liệu đã đồng bộ sẵn, dùng ngay được cho tính log-return và DCCA.

---

## 4. Khác biệt giữa 2 file

| Khía cạnh | `vn_indices_merged_raw.csv` | `vn_indices_merged_filled.csv` |
|---|---|---|
| Cột `USDVND` | Giữ nguyên `NaN` ở những dòng thiếu (do USDVND gốc chỉ có theo ngày, và chỉ tới 12/2024) | Đã forward-fill: lấy giá `USDVND` gần nhất trước đó để lấp vào |
| Số dòng thiếu `USDVND` | 11,161 / 43,842 | 0 / 43,842 |
| Khi nào dùng | Khi cần biết chính xác đâu là dữ liệu thật, đâu là thiếu (VD: kiểm tra chất lượng dữ liệu, loại bỏ hoàn toàn phần thiếu bằng `dropna`) | Khi cần một chuỗi `USDVND` liên tục để đưa vào mô hình (VD: hồi quy, biến kiểm soát) mà không muốn code phải tự xử lý `NaN` |

**Cảnh báo quan trọng:** vì `USDVND` gốc chỉ có dữ liệu tới **08/12/2024**, nên trong file `filled`, toàn bộ giai đoạn **năm 2025 mang giá trị lặp lại của phiên cuối cùng (08/12/2024)**, **không phải tỷ giá thật**. Nếu phân tích có liên quan đến biến động USDVND trong 2025, cần dùng file `raw` và loại các dòng `NaN` tương ứng, hoặc bổ sung dữ liệu USDVND 2025 từ nguồn khác.

---

## 5. Phạm vi dữ liệu theo từng khung thời gian

| Timeframe | Số dòng | Từ | Đến |
|---|---|---|---|
| `1D` | 2,964 | 27/01/2014 | 12/12/2025 |
| `M30` | 21,943 | 03/01/2017 | 12/12/2025 |
| `H1` | 13,524 | 27/01/2014 | 09/12/2024 |
| `H4` | 5,411 | 27/01/2014 | 09/12/2024 |

**Lưu ý khi thiết kế nghiên cứu:** `H1` và `H4` **thiếu toàn bộ năm 2025**, trong khi `1D` và `M30` có đủ tới cuối 2025. Nếu muốn phân tích xuyên suốt đến 2025, nên ưu tiên trục chính là **1D + M30**; `H1`/`H4` chỉ nên dùng cho giai đoạn 2014–2024 hoặc như phân tích bổ sung về "thang thời gian trung gian".

---

## 6. Ý tưởng nghiên cứu: Tương quan chéo đa thang thời gian (DCCA/MF-DCCA) và hàm ý cho danh mục đầu tư

### 6.1. Câu hỏi nghiên cứu

Các nhà đầu tư xây dựng danh mục thường giả định tương quan giữa các tài sản (hoặc giữa các chỉ số đại diện nhóm tài sản) là **một con số cố định**, ước lượng từ dữ liệu lịch sử (thường là dữ liệu ngày). Nhưng trên thực tế:

- Tương quan **thay đổi theo thang thời gian quan sát** (30 phút vs. ngày vs. tuần).
- Tương quan **thay đổi theo "chế độ" biến động** của thị trường (giai đoạn bình ổn vs. giai đoạn biến động mạnh/khủng hoảng).

Nếu điều này đúng, thì việc **đa dạng hóa danh mục** dựa trên tương quan ước lượng từ dữ liệu ngày có thể **đánh giá sai mức độ rủi ro thực sự** — đặc biệt trong giai đoạn thị trường biến động mạnh, khi nhà đầu tư cần đa dạng hóa nhất thì tương quan giữa các tài sản lại có xu hướng tăng vọt (hiện tượng "correlation breakdown" / "diworsification").

**Mục tiêu nghiên cứu:** (1) Chứng minh chặt chẽ về mặt toán học công cụ đo tương quan chéo theo thang thời gian (DCCA), và (2) Kiểm định thực nghiệm trên VNINDEX, VN30, VN100 xem tương quan giữa các "danh mục ngầm định" này (mỗi chỉ số đại diện một rổ cổ phiếu) có thực sự thay đổi theo thang thời gian và theo chế độ biến động hay không — từ đó rút ra hàm ý cho việc xây dựng danh mục đầu tư đa tài sản/đa nhóm cổ phiếu tại Việt Nam.

### 6.2. Khung lý thuyết: DCCA (Detrended Cross-Correlation Analysis)

Nguồn gốc: Podobnik & Stanley (2008), mở rộng đa fractal (MF-DCCA) bởi Zhou (2008).

**Bước 1 — Chuỗi tích lũy (profile):**

Với hai chuỗi log-return $\{x_i\}, \{y_i\}$ (VD: log-return của VN30 và VNINDEX), xây dựng:

$$X_k = \sum_{i=1}^{k}(x_i - \bar x), \qquad Y_k = \sum_{i=1}^{k}(y_i - \bar y)$$

**Bước 2 — Loại xu hướng cục bộ (detrending):**

Chia $X_k, Y_k$ thành các đoạn độ dài $s$ (thang thời gian cần xét), khớp đa thức bậc $m$ trên từng đoạn, lấy phần dư $\tilde X_k, \tilde Y_k$.

**Bước 3 — Hàm hiệp phương sai theo thang $s$:**

$$F_{xy}^2(s) = \frac{1}{N-s}\sum_{k=1}^{N-s}\tilde X_k \, \tilde Y_k$$

**Bước 4 — Hệ số tương quan chéo DCCA:**

$$\rho_{DCCA}(s) = \frac{F_{xy}^2(s)}{F_{xx}(s)\, F_{yy}(s)}$$

trong đó $F_{xx}(s), F_{yy}(s)$ là hàm biến động detrended (DFA) của từng chuỗi riêng lẻ.

**Mệnh đề cần chứng minh (phần lý thuyết của đề tài):**

1. **Tính bị chặn:** $-1 \le \rho_{DCCA}(s) \le 1$ với mọi $s$ — chứng minh bằng bất đẳng thức Cauchy–Schwarz áp dụng lên các đoạn đã detrend.
2. **Phân phối kiểm định:** dưới giả thuyết $H_0$ (hai chuỗi độc lập), $\rho_{DCCA}(s)$ có phân phối xấp xỉ chuẩn với số bậc tự do hiệu chỉnh $n(s) = N/s - 2$ (Podobnik et al., 2011) → cho phép xây dựng kiểm định thống kê chính thức, không chỉ mô tả định tính.
3. **(Mở rộng, nếu có thời gian) MF-DCCA:** tổng quát hóa hàm $F_{xy}(s)$ theo bậc $q$ để tách riêng tương quan trong giai đoạn biến động lớn ($q>0$) và biến động nhỏ ($q<0$), dựa trên lý thuyết đa fractal (Kantelhardt et al., 2002).

### 6.3. Thiết kế thực nghiệm

**Dữ liệu sử dụng:** log-return của `VN30`, `VN100`, `VNINDEX` từ file `vn_indices_merged_filled.csv` (hoặc `raw` nếu không cần USDVND), lọc theo từng `timeframe`.

**Các bước thực hiện:**

1. **Tiền xử lý:** tính log-return $r_t = \ln(P_t/P_{t-1})$ cho từng chỉ số, ở từng khung thời gian.
2. **Tính $\rho_{DCCA}(s)$** giữa các cặp chỉ số:
   - VN30 – VNINDEX (nhóm vốn hóa lớn vs. toàn thị trường)
   - VN30 – VN100 (nhóm vốn hóa lớn vs. vốn hóa vừa)
   - VN100 – VNINDEX
   
   với $s$ chạy từ vài mốc nhỏ (VD: vài giờ) đến vài tuần/tháng — sử dụng dữ liệu `M30` làm trục chính (đủ tới 2025, đủ dày để quét nhiều $s$).
3. **Vẽ đường cong Epps/DCCA:** trục hoành = $\log(s)$, trục tung = $\rho_{DCCA}(s)$ → kỳ vọng thấy tương quan tăng dần và bão hòa khi $s$ tăng.
4. **Kiểm định thống kê:** áp dụng phân phối tiệm cận (mục 6.2, mệnh đề 2) để kiểm tra khác biệt giữa $\rho_{DCCA}(s\text{ nhỏ})$ và $\rho_{DCCA}(s\text{ lớn})$ có ý nghĩa thống kê không.
5. **Phân tích theo chế độ biến động (MF-DCCA):** tách các giai đoạn biến động mạnh (VD: các đợt giảm sâu của VNINDEX trong 2018, 2020, 2022, 2025) và giai đoạn ổn định, so sánh $\rho_{DCCA}(s)$ giữa hai chế độ.
6. **Liên hệ danh mục đầu tư:**
   - Xây dựng danh mục giả định gồm 2 "tài sản" (VD: tỷ trọng VN30 và phần bù VNINDEX-VN30 đại diện nhóm vốn hóa vừa/nhỏ), tính phương sai danh mục theo công thức Markowitz **sử dụng $\rho_{DCCA}(s)$ thay vì $\rho$ Pearson cố định**:
   
   $$\sigma_p^2(s) = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\sigma_1\sigma_2\,\rho_{DCCA}(s)$$
   
   - So sánh $\sigma_p^2(s)$ ở các thang thời gian khác nhau và ở các chế độ biến động khác nhau → cho thấy mức độ rủi ro danh mục bị **đánh giá thấp** thế nào nếu chỉ dùng tương quan từ dữ liệu ngày trong giai đoạn thị trường ổn định.
7. **So sánh quốc tế:** đối chiếu độ mạnh của hiện tượng với các nghiên cứu DCCA đã công bố ở thị trường phát triển (Mỹ, châu Âu) — điểm đóng góp mới vì DCCA áp dụng cho thị trường VN còn ít nghiên cứu.

### 6.4. Cấu trúc đề tài đề xuất

1. **Chương 1** — Đặt vấn đề, câu hỏi nghiên cứu, đóng góp
2. **Chương 2** — Tổng quan lý thuyết (DCCA, MF-DCCA, các nghiên cứu liên quan trong và ngoài nước)
3. **Chương 3** — Chứng minh toán học (mục 6.2), phương pháp ước lượng, kiểm định thống kê
4. **Chương 4** — Dữ liệu, mô tả thống kê, kết quả thực nghiệm ($\rho_{DCCA}(s)$ theo thang thời gian và chế độ biến động)
5. **Chương 5** — Hàm ý cho xây dựng danh mục đầu tư tại Việt Nam, so sánh quốc tế, hạn chế và hướng mở rộng

---

## 7. Tài liệu tham khảo gốc (khung lý thuyết)

- Podobnik, B., & Stanley, H. E. (2008). *Detrended cross-correlation analysis: a new method for analyzing two nonstationary time series*. Physical Review Letters.
- Zhou, W.-X. (2008). *Multifractal detrended cross-correlation analysis for two nonstationary signals*. Physical Review E.
- Podobnik, B., Jiang, Z.-Q., Zhou, W.-X., & Stanley, H. E. (2011). *Statistical tests for power-law cross-correlated processes*. Physical Review E.
- Kantelhardt, J. W. et al. (2002). *Multifractal detrended fluctuation analysis of nonstationary time series*. Physica A.
