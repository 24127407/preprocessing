# Chương 4: Báo cáo Tổng hợp & Phân tích So sánh

> *Trạng thái: Khung chương khởi tạo (Giai đoạn 1). Nội dung phân tích đối chiếu định lượng đầy đủ sẽ được tổng hợp sau khi hoàn tất Phần (a) và Phần (b).*

## 1. Tổng hợp kết quả Phần (a) – Dữ liệu dạng bảng

- Đối chiếu RMSE của 5 chiến lược điền khuyết (Mean, Median, Mode, k-NN, MICE).
- So sánh độ chồng chéo (Jaccard) và tác động phân phối (KS test) giữa 4 nhóm phát hiện ngoại lai.
- Đánh giá đồng nhất phương sai (Levene's test) sau chuẩn hóa và đa cộng tuyến (VIF) sau mã hóa biến phân loại.
- So sánh hiệu năng CV F1-score qua 3 tầng chọn/giảm chiều đặc trưng và tác động của SMOTE/ADASYN/RUS.

## 2. Tổng hợp kết quả Phần (b) – Dữ liệu văn bản

- Tổng kết đặc trưng ngôn ngữ (Mann-Whitney U, TTR, định luật Zipf).
- Đánh giá đánh đổi giữa 4 chiến lược Tokenization (Vocab size, OOV rate, độ dài chuỗi).
- Tác động của loại bỏ Stop words (MI, Naive Bayes) và chuẩn hóa gốc từ (Collision rate, Logistic Regression CV).
- So sánh không gian biểu diễn thưa (BoW, TF-IDF) vs dày đặc (Word2Vec, `all-MiniLM-L6-v2`) qua Silhouette score và Linear SVM F1-score.

## 3. Phân tích phê bình (Critical Analysis) & Kết luận

- Thảo luận các đánh đổi (*trade-offs*) chính về độ chính xác, chi phí tính toán và khả năng diễn giải.
- Các bài học về chống rò rỉ dữ liệu (*Data Leakage*) trong thiết kế pipeline thực tế.
