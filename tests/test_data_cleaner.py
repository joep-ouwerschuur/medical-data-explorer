import pandas as pd
from src import data_cleaner

def test_remove_missing_values_removes_rows_with_missing_values():
  df = pd.DataFrame({
    "age": [63, None, 41],
    "chol": [233, 286, None]
  })

  cleaned_df = data_cleaner.remove_missing_values(df)

  assert len(cleaned_df) == 1


def test_remove_duplicates_removes_duplicates_rows():
  df = pd.DataFrame({
    "age": [63, 63, 41],
    "chol": [233, 233, 204]
  })

  cleaned_df = data_cleaner.remove_duplicates(df)

  assert len(cleaned_df) == 2

def test_clean_dataset_remove_missing_values_and_duplicates():
  df = pd.DataFrame({
    "age": [63, 63, None, 41],
    "chol":[233, 233, 286, 204]
  })
  
  cleaned_df, _ = data_cleaner.clean_dataset(df)

  assert isinstance(cleaned_df, pd.DataFrame) 
    
  assert len(cleaned_df) == 2

def test_clean_dataset_reports_removed_rows_per_rule():
  df = pd.DataFrame({
    "age": [63, 63, None, 41],
    "chol":[233, 233, 286, 204]
  })

  cleaned_df, report = data_cleaner.clean_dataset(df)

  assert isinstance(cleaned_df, pd.DataFrame)
  assert isinstance(report, dict)

  assert report["rows_before"] == 4
  assert report["rows_removed_missing"] == 1
  assert report["rows_removed_duplicates"] == 1
  assert report["rows_after"] == 2

  assert len(cleaned_df) == 2

