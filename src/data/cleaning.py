"""
Data cleaning module for insurance dataset.
"""
from sklearn.preprocessing import StandardScaler 
import pandas as pd
import os

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

    # scalecols = ["age","bmi","children"]
    # sdf = df[scalecols]

    # scaler = StandardScaler()
    # df_scaled = scaler.fit_transform(df[scalecols])
    # resdf = df.drop(scalecols)
    # df = pd.concat(resdf, df_scaled)
    
    # Save if output path provided
    if output_path:
        df.to_csv(output_path, index=False)

    return df


if __name__ == "__main__":
    inputpath = os.getcwd() +"/data/raw/insurance.csv"
    outputpath = os.getcwd() +"/data/processed/insurance.csv"

    df_cleaned = clean_and_encode(inputpath, outputpath)

    df = pd.read_csv(inputpath)
    ycol = ['charges']
    print(f"Shape: {df_cleaned.shape}")
    print(df_cleaned.head())
