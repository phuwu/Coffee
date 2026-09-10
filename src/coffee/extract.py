import pandas as pd

CAFE_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-09-08/cafe.csv"
CAPPUCCINO_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-09-08/cappuccino_index.csv"

def extract_cafe() -> pd.DataFrame:
    return pd.read_csv(CAFE_URL)

def extract_cappuccino_index() -> pd.DataFrame:
    return pd.read_csv(CAPPUCCINO_URL)