import column_metadata
import data_analyzer

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
    column_type = data_analyzer.get_column_type(column)
    print(f"{column} - [{column_type}] - {description}")

def print_cleaning_summary(rows_before, rows_after):
  print("Rows before cleaning:")
  print(rows_before)

  print("\nRows after cleaning:")
  print(rows_after)

  print("\nRows removed:")
  print(rows_before - rows_after)


