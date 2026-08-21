

def remove_missing_values(df):
  return df.dropna()

def remove_duplicates(df):
  return df.drop_duplicates()

def clean_dataset(df):
  df = remove_missing_values(df)
  df = remove_duplicates(df)
  return df