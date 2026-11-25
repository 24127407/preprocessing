# Đồ án Tiền xử lý Dữ liệu (Data Preprocessing)

- **Sinh viên thực hiện:** Mã Đức Khải
- **MSSV:** 24127407
- **Liên kết Jupyter Book (GitHub Pages):** https://TheBrilliantCoder.github.io/24127407/
- **Mã nguồn (GitHub Repository):** https://github.com/TheBrilliantCoder/24127407

---

## 1. Tổ hợp bài toán & Mô tả tập dữ liệu

Đồ án triển khai đầy đủ phân tích thống kê khám phá (EDA), pipeline tiền xử lý định lượng, báo cáo so sánh phê bình và cả 2 mục `[Nâng cao]` cho hai dạng dữ liệu:

- **Phần (a) – Dữ liệu dạng bảng:** *Adult Census Income*
  - **Nguồn công khai:** [Hugging Face – `scikit-learn/adult-census-income`](https://huggingface.co/datasets/scikit-learn/adult-census-income)
  - **Đặc điểm:** 32.561 dòng, 15 thuộc tính (kết hợp biến số và biến phân loại), có giá trị khuyết thiếu tự nhiên $\ge 5\%$ ở các cột `workclass` (~5.64%) và `occupation` (~5.66%), có biến phân loại nhiều giá trị (`native.country` > 40 quốc gia) và mất cân bằng lớp (~24% nhãn `>50K`).
- **Phần (b) – Dữ liệu văn bản:** *IMDB Movie Reviews*
  - **Nguồn công khai:** [Hugging Face – `stanfordnlp/imdb`](https://huggingface.co/datasets/stanfordnlp/imdb)
  - **Đặc điểm:** 50.000 đánh giá phim tiếng Anh phân thành 2 nhãn cảm xúc (`pos`, `neg`), lấy mẫu phân tầng 20.000 văn bản (`random_state=42`) để tối ưu thời gian build Jupyter Book. Văn bản chứa nhiều thẻ HTML (`<br />`) và ký tự nhiễu, phù hợp kiểm chứng pipeline làm sạch và so sánh biểu diễn văn bản.

> **Lưu ý:** Dữ liệu thô không được đẩy trực tiếp lên repository (đã loại trừ qua `.gitignore`). Toàn bộ dữ liệu được tải tự động từ Hugging Face qua script [`src/prepare_data.py`](src/prepare_data.py) và gọi trực tiếp trong các notebook.

---

## 2. Cấu trúc Repository

```text
24127407/
├── README.md                              # Thông tin sinh viên, mô tả dữ liệu, hướng dẫn cài đặt & build
├── requirements.txt                       # Danh sách thư viện khóa phiên bản cụ thể
├── .github/workflows/deploy.yml           # GitHub Actions tự động build & deploy GitHub Pages
├── src/
│   └── prepare_data.py                    # Script tải và kiểm định ràng buộc 2 tập dữ liệu
├── book/                                  # Nguồn Jupyter Book duy nhất
│   ├── _config.yml                        # Cấu hình Jupyter Book
│   ├── _toc.yml                           # Mục lục các chương
│   ├── index.md                           # Trang mở đầu giới thiệu mục tiêu & kiến trúc pipeline
│   ├── 01_EDA_tabular.ipynb               # Phần (a) – Chương 1: EDA dữ liệu bảng
│   ├── 02_preprocessing_tabular.ipynb     # Phần (a) – Chương 2: Tiền xử lý dữ liệu bảng & [Nâng cao]
│   ├── 06_text_preprocessing.ipynb        # Phần (b) – Chương 3: EDA, tiền xử lý văn bản & [Nâng cao]
│   └── report.md                          # Chương 4: Báo cáo tổng hợp & phân tích so sánh
└── data/
    ├── raw/                               # Dữ liệu thô tải về cục bộ (ignored by Git)
    └── processed/                         # Dữ liệu sau tiền xử lý cục bộ (ignored by Git)
```

---

## 3. Hướng dẫn cài đặt môi trường và Build Book

Yêu cầu **Python 3.10** (khớp với môi trường CI/CD trên GitHub Actions).

### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
python src/prepare_data.py
jupyter-book build book/
```

### Linux / macOS (Bash)
```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python src/prepare_data.py
jupyter-book build book/
```

Sau khi build thành công, mở tệp `book/_build/html/index.html` trên trình duyệt để xem bản dựng cục bộ.
