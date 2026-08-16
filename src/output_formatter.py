def print_categorical_summary(column, summary):
  print(f"Analysis for column: {column}")

  print("\nValue counts:")
  print(summary["value_counts"])

  print("\nPercentages:")
  print(summary["percentages"])


def print_numeric_summary(column, summary):
  print(f"Analysis for column: {column}")

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