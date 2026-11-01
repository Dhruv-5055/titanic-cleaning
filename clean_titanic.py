import pandas as pd

RAW_PATH = "data/titanic_raw.csv"
CLEAN_PATH = "data/titanic_clean.csv"


def clean(df):
    df = df.copy()
    # Rule 1: fill missing Age with the median age of the same class and sex
    group_median = df.groupby(['Pclass', 'Sex'])['Age'].transform('median')
    df['Age'] = df['Age'].fillna(group_median)
    # Rule 2: Cabin (your decision, below)
    return df


if __name__ == "__main__":
    raw = pd.read_csv(RAW_PATH)
    cleaned = clean(raw)
    cleaned.to_csv(CLEAN_PATH, index=False)
    print("Rows:", len(raw), "->", len(cleaned))
    print("Columns:", raw.shape[1], "->", cleaned.shape[1])
    print("Missing values:", int(raw.isna().sum().sum()), "->", int(cleaned.isna().sum().sum()))