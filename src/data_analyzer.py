

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
    "average": round(df[column].mean(), 2),
    "median": round(df[column].median(), 2),
    "minimum": round(df[column].min(), 2),
    "maximum": round(df[column].max(), 2),
    "standard_deviation": round(df[column].std(), 2)
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

def get_column_type(column):
  if is_categorical_column(column):
    return "categorical"

  return "numeric"

