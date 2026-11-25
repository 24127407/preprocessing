# Đồ án Tiền xử lý Dữ liệu (Data Preprocessing)

Chào mừng đến với cuốn **Jupyter Book** tổng hợp toàn bộ quá trình phân tích thống kê khám phá (EDA), thiết kế pipeline tiền xử lý định lượng và đánh giá tác động cho Đồ án Tiền xử lý Dữ liệu.

- **Sinh viên thực hiện:** Mã Đức Khải
- **MSSV:** 24127407
- **Repository:** [TheBrilliantCoder/24127407](https://github.com/TheBrilliantCoder/24127407)

---

## 1. Mục tiêu đồ án

Đồ án áp dụng có hệ thống các kỹ thuật tiền xử lý dữ liệu kết hợp với kiểm định thống kê, đo lường định lượng và thiết kế pipeline chống rò rỉ dữ liệu (*anti-leakage*) trên hai dạng dữ liệu:

1. **Phần (a) – Dữ liệu dạng bảng (*Adult Census Income*):** Kiểm định phân phối, tương quan đa biến, cơ chế khuyết thiếu (MCAR/MAR/MNAR), so sánh 5 chiến lược điền khuyết, 4 phương pháp phát hiện ngoại lai, 4 kỹ thuật chuẩn hóa, mã hóa biến phân loại nâng cao, lựa chọn/giảm chiều đặc trưng 3 tầng và `[Nâng cao]` xử lý mất cân bằng lớp (SMOTE, ADASYN, Random Under-sampling).
2. **Phần (b) – Dữ liệu văn bản (*IMDB Movie Reviews*):** Text EDA (phân phối độ dài + Mann-Whitney U, Word Cloud, TTR, định luật Zipf), pipeline làm sạch 5 bước, so sánh 4 chiến lược Tokenization (Word, Sentence, Character, Subword BPE), phân tích Stop words (MI + Naive Bayes), so sánh Stemming vs Lemmatization (Collision Rate + 5-fold CV), vector hóa (BoW, TF-IDF, Word2Vec) và `[Nâng cao]` biểu diễn ngữ nghĩa bằng Sentence Transformer (`all-MiniLM-L6-v2`).

---

## 2. Kiến trúc tổng thể & Nguyên tắc triển khai

- **Chuẩn trình bày 3 phần cho mọi kỹ thuật:**
  1. Lý thuyết & công thức toán học (Markdown + LaTeX).
  2. Mã nguồn Python sạch, có chú thích, gán các giá trị số (p-value, RMSE, F1, Silhouette...) vào biến rõ ràng để kiểm chứng.
  3. Phân tích kết quả thống kê và nhận xét phê bình.
- **Chống rò rỉ dữ liệu (Data Leakage Prevention):** Mọi bộ biến đổi học tham số (Imputer, Scaler, Target Encoder, Vectorizer, SMOTE/ADASYN) đều được `fit` độc lập trên tập huấn luyện (`Train`) sau khi tách `Train/Test`.
- **Tái sản xuất (Reproducibility):** Cố định `random_state=42`, khóa phiên bản thư viện trong `requirements.txt`, và tải dữ liệu tự động từ Hugging Face.

---

## 3. Cấu trúc các chương

| Chương | Tập tin nguồn | Nội dung trọng tâm |
| :--- | :--- | :--- |
| **Chương 1** | `01_EDA_tabular.ipynb` | Phần (a): Khám phá dữ liệu bảng, kiểm định phân phối, tương quan đa biến & phân tích cơ chế thiếu dữ liệu. |
| **Chương 2** | `02_preprocessing_tabular.ipynb` | Phần (a): Pipeline tiền xử lý dữ liệu bảng (Imputation, Outlier, Scaling, Encoding, Feature Selection/Reduction) & `[Nâng cao]` Imbalanced Learning. |
| **Chương 3** | `06_text_preprocessing.ipynb` | Phần (b): Text EDA, Zipf, làm sạch, 4 chiến lược Tokenization, Stop words, Stem/Lemma, Vectorization & `[Nâng cao]` Sentence Transformer. |
| **Chương 4** | `report.md` | Báo cáo tổng hợp, bảng đối chiếu định lượng đa chiều, phân tích đánh đổi (*trade-offs*) và kết luận. |
