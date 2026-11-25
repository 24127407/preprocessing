import os
import pandas as pd
from datasets import load_dataset


def prepare_and_verify_tabular(output_path: str = "data/raw/tabular_adult.csv") -> None:
    """Tải dữ liệu bảng Adult Census Income và kiểm tra các ràng buộc của đề bài."""
    dataset = load_dataset("scikit-learn/adult-census-income", split="train")
    df = dataset.to_pandas()
    df.replace("?", pd.NA, inplace=True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    cat_cols = df.select_dtypes(exclude=["number"]).columns.tolist()
    missing_pct = (df.isna().mean() * 100).sort_values(ascending=False)
    high_card_cols = [c for c in cat_cols if df[c].nunique(dropna=True) > 20]

    print("=== KIỂM TRA DỮ LIỆU BẢNG (PHẦN A) ===")
    print(f"- Số dòng: {len(df):,} (Yêu cầu >= 10,000)")
    print(f"- Số thuộc tính: {df.shape[1]} (Yêu cầu >= 10)")
    print(f"- Thuộc tính số ({len(num_cols)}): {num_cols}")
    print(f"- Thuộc tính phân loại ({len(cat_cols)}): {cat_cols}")
    print(f"- Cột missing >= 5%:\n{missing_pct[missing_pct >= 5.0].round(2)}")
    print(f"- Cột high-cardinality (>20 giá trị): {high_card_cols}")
    print(f"- Phân bố nhãn mục tiêu:\n{df['income'].value_counts(normalize=True).round(4)}\n")


def prepare_and_verify_text(
    output_path: str = "data/raw/text_imdb_20k.csv",
    sample_size: int = 20000,
    random_state: int = 42,
) -> None:
    """Tải dữ liệu IMDB, lấy mẫu phân tầng 20,000 dòng và kiểm tra ràng buộc."""
    ds_train = load_dataset("stanfordnlp/imdb", split="train").to_pandas()
    ds_test = load_dataset("stanfordnlp/imdb", split="test").to_pandas()
    df_full = pd.concat([ds_train, ds_test], ignore_index=True)

    # Lấy mẫu phân tầng 20,000 mẫu để tối ưu thời gian build Jupyter Book
    df_sample = (
        df_full.groupby("label", group_keys=False)
        .sample(n=sample_size // 2, random_state=random_state)
        .reset_index(drop=True)
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_sample.to_csv(output_path, index=False)

    word_lengths = df_sample["text"].str.split().str.len()
    char_lengths = df_sample["text"].str.len()

    print("=== KIỂM TRA DỮ LIỆU VĂN BẢN (PHẦN B) ===")
    print(f"- Số mẫu: {len(df_sample):,} (Yêu cầu >= 10,000)")
    print(f"- Số nhãn phân loại: {df_sample['label'].nunique()} (Yêu cầu >= 2)")
    print(f"- Phân bố nhãn:\n{df_sample['label'].value_counts()}")
    print(
        f"- Độ dài (số từ): min={word_lengths.min()}, median={word_lengths.median():.1f}, "
        f"mean={word_lengths.mean():.1f}, max={word_lengths.max()}"
    )
    print(
        f"- Độ dài (số ký tự): min={char_lengths.min()}, median={char_lengths.median():.1f}, "
        f"mean={char_lengths.mean():.1f}, max={char_lengths.max()}"
    )


if __name__ == "__main__":
    prepare_and_verify_tabular()
    prepare_and_verify_text()