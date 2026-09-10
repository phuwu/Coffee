import pandas as pd

def clean_cafe_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df.columns = df.columns.str.lower().str.strip()
    return df

def clean_cappuccino_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    return df