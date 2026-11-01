# Titanic Data Cleaning

This project cleans the raw Titanic passenger data with pandas. It fills missing values, checks for duplicates, adds a `HasCabin` column, and saves a clean file ready for analysis.

## Dataset

- Source: Titanic passengers
- Size before cleaning: 891 rows and 12 columns
- Important columns:
  - `Survived`: 0 = did not survive, 1 = survived
  - `Pclass`: ticket class (1, 2 or 3)
  - `Age`: age in years
  - `Cabin`: cabin number

## Cleaning decisions

| Problem | What I did | Why |
| --- | --- | --- |
| Age missing | Filled with the median age of passengers in the same `Pclass` and `Sex` | The median is not pulled by extreme ages, and a matching group gives a closer guess than one value for everyone |
| Cabin mostly missing | Added a `HasCabin` column (True/False) and filled the text with `Not Available` | Having no recorded cabin carries information, so I kept that fact instead of dropping the column |
| Embarked has 2 missing | Filled with `Unknown` | Only 2 rows, and I did not want to invent a port |
| Duplicates | Checked for duplicate rows, also without `PassengerId`: none found | Nothing needed removing |
| Fare = 0 (15 rows) | Kept all 15 rows | They are real records, and deleting or guessing would change the data without evidence |

## Files

- `data/titanic_raw.csv`: the original data, left unchanged
- `data/titanic_clean.csv`: the cleaned data that the script produces
- `clean_titanic.py`: the cleaning script

## How to run

1. Install pandas: `pip install pandas`
2. Run the script from this folder: `python clean_titanic.py`

## Result

`data/titanic_clean.csv` has no missing values and one new column, `HasCabin`.