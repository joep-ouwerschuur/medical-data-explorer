

def remove_missing_values(df):
  return df.dropna()

def remove_duplicates(df):
  return df.drop_duplicates()

def clean_dataset(df):

  rows_before = len(df)

  without_missing = remove_missing_values(df)
  rows_removed_missing = rows_before - len(without_missing)

  cleaned_df = remove_duplicates(without_missing)
  rows_removed_duplicates = len(without_missing) - len(cleaned_df)
  
  report = {
    "rows_before": rows_before,
    "rows_removed_missing": rows_removed_missing,
    "rows_removed_duplicates": rows_removed_duplicates,
    "rows_after": len(cleaned_df)
  }

  return cleaned_df, report