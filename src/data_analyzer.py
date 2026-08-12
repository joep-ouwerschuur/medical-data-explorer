

def get_average_age(df):
  return df["age"].mean()

def get_target_distribution(df):
  return df["num"].value_counts()

def get_average_cholesterol_by_target(df):
  return df.groupby("num")["chol"].mean()

def get_correlations(df):
  return df.corr(numeric_only=True)

