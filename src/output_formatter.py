import column_metadata

def print_categorical_summary(column, description, summary):
  print(f"Analysis for column: {column}")
  print(f"Description: {description}")

  print("\nValue counts:")
  print(summary["value_counts"])

  print("\nPercentages:")
  print(summary["percentages"])


def print_numeric_summary(column, description, summary):
  print(f"Analysis for column: {column}")
  print(f"Description: {description}")

  print("\nTop 10 value counts:")
  print(summary["value_counts"].head(10))

  print("\nAverage:")
  print(summary["average"])

  print("\nMedian:")
  print(summary["median"])

  print("\nMinimum:")
  print(summary["minimum"])

  print("\nMaximum:")
  print(summary["maximum"])

  print("\nStandard deviation:")
  print(summary["standard_deviation"])

def print_available_columns(columns):
  print("Available columns:")

  for column in columns:
    description = column_metadata.get_column_description(column)
    print(f"{column} - {description} ")






