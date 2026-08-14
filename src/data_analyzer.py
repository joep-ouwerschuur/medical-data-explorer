

def get_average_age(df):
  return df["age"].mean()

def get_target_distribution(df):
  return df["num"].value_counts()

def get_average_cholesterol_by_target(df):
  return df.groupby("num")["chol"].mean()

def get_correlations(df):
  return df.corr(numeric_only=True)

def get_column_summary(df, column):
  return {
    "value_counts": df[column].value_counts(),
    "average": df[column].mean(),
    "median": df[column].median(),
    "minimum": df[column].min(),
    "maximum": df[column].max(),
    "standard_deviation": df[column].std()
  }

def is_numeric_column(df, column):
  return df[column].dtype in ["int64", "float64"]

CATEGORICAL_COLUMNS = [
    "sex",
    "cp",
    "fbs",
    "restecg",
    "exang",
    "slope",
    "ca",
    "thal",
    "num"
]

def is_categorical_column(column):
  return column in CATEGORICAL_COLUMNS

def get_categorical_summary(df, column):
  return {
    "value_counts": df[column].value_counts(),
    "percentages": (df[column].value_counts(normalize=True) * 100).round(2)
  }


