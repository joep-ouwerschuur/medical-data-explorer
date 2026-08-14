import argparse

import data_cleaner
import data_analyzer
import data_inspector
import data_loader
from data_loader import load_csv

def main():
  parser = argparse.ArgumentParser(description="Medical Data Explorer")
  parser.add_argument("command", choices=["inspect", "analyse", "visualize"])
  parser.add_argument("file_path")
  parser.add_argument("--column", choices=data_loader.COLUMN_NAMES)

  args = parser.parse_args()

  df = load_csv(args.file_path)
  clean_df = data_cleaner.remove_missing_values(df)

  if args.command == "inspect":
    data_inspector.show_head(clean_df)
    data_inspector.show_shape(clean_df)
    data_inspector.show_missing_values(clean_df)

  elif args.command == "analyse":
    if args.column is None:
        print("Please choose a column with --column")
        print("Example: python3 src/main.py analyse datasets/cleveland.heart.csv --column age")
        return


    print(f"Analysis for column: {args.column}")

    if data_analyzer.is_categorical_column(args.column):
        summary = data_analyzer.get_categorical_summary(clean_df, args.column)


        print("\nValue counts:")
        print(summary["value_counts"])

        print("\nPercentages:")
        print(summary["percentages"])

        return

    if not data_analyzer.is_numeric_column(clean_df, args.column):
      print(f"{args.column} is not a numeric column")
      return

    summary = data_analyzer.get_column_summary(clean_df, args.column)

    print("\nValue counts:")
    print(summary["value_counts"])

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

  elif args.command == "visualize":
      import data_visualizer
      
      target_distribution = data_analyzer.get_target_distribution(clean_df)
      data_visualizer.plot_target_distribution(target_distribution)


main()