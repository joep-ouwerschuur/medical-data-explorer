import pandas as pd

COLUMN_NAMES = [
  "age",
  "sex",
  "cp",
  "trestbps",
  "chol",
  "fbs",
  "restecg",
  "thalach",
  "exang",
  "oldpeak",
  "slope",
  "ca",
  "thal",
  "num"
]


def load_csv(file_path):
  return pd.read_csv(file_path, header=None, names=COLUMN_NAMES, na_values="?")

