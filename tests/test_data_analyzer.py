import pandas as pd
from src import data_analyzer

def test_get_column_summary_returns_numeric_statistics():
  df = pd.DataFrame({
    "chol": [200, 240, 280]
  })

  summary = data_analyzer.get_column_summary(df, "chol")

  assert summary["average"] == 240
  assert summary["median"] == 240
  assert summary["minimum"] == 200
  assert summary["maximum"] == 280 

def test_get_categorical_summary_returns_counts_and_percentages():
  df = pd.DataFrame({
    "sex": [1, 1, 0, 1]
  })

  summary = data_analyzer.get_categorical_summary(df, "sex")

  assert summary["value_counts"][1] == 3
  assert summary["value_counts"][0] == 1
  assert summary["percentages"][1] == 75
  assert summary["percentages"][0] == 25


def test_get_average_by_category_groups_column_average():
  df = pd.DataFrame({
    "chol": [200, 240, 300, 360],
    "sex": [0, 0, 1, 1]
  })

  result = data_analyzer.get_average_by_category(df, "chol", "sex")

  assert result[0] == 220
  assert result[1] == 330