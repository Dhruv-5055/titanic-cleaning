import pandas as pd

RAW_PATH = "data/titanic_raw.csv"
CLEAN_PATH = "data/titanic_clean.csv"


def clean(df):
    df = df.copy()

    # Rule 1: fill missing Age with the median age of the same class and sex
    group_median = df.groupby(['Pclass', 'Sex'])['Age'].transform('median')
    df['Age'] = df['Age'].fillna(group_median)

    # Rule 2: write "Cabin not available" where the cabin is empty
    df['Cabin'] = df['Cabin'].fillna("Cabin not available")

    # Rule 3: write "Unknown port" where the boarding port is empty
    df['Embarked'] = df['Embarked'].fillna("Unknown port")

    # Decision, no rule needed: 15 passengers have Fare = 0. They are all male,
    # all boarded at Southampton, hold grouped tickets and only 1 of 15 survived
    # (6.7% against 38.4% overall). That pattern says the zeros are real, so
    # they are kept as they are.

    return df


if __name__ == "__main__":
    raw = pd.read_csv(RAW_PATH)
    cleaned = clean(raw)
    cleaned.to_csv(CLEAN_PATH, index=False)
    print("Rows:", len(raw), "->", len(cleaned))
    print("Columns:", raw.shape[1], "->", cleaned.shape[1])
    print("Missing values:", int(raw.isna().sum().sum()), "->", int(cleaned.isna().sum().sum()))