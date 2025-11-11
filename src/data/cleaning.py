"""
Data cleaning module for insurance dataset.
"""

import pandas as pd


def clean_and_encode(filepath: str, output_path: str = None) -> pd.DataFrame:
    """
    Clean data and perform one-hot encoding.

    Args:
        filepath: Path to the input CSV file
        output_path: Path to save cleaned data (optional)

    Returns:
        Cleaned and encoded DataFrame
    """
    # Load data
    df = pd.read_csv(filepath)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # One-hot encode categorical columns
    df = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)

    # Save if output path provided
    if output_path:
        df.to_csv(output_path, index=False)

    return df


if __name__ == "__main__":
    df_cleaned = clean_and_encode("../../insurance.csv")
    print(f"Shape: {df_cleaned.shape}")
    print(df_cleaned.head())
