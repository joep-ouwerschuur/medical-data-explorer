import argparse
import data_cleaner
import data_analyzer
import data_inspector
import data_loader
import output_formatter
import column_metadata

from data_loader import load_csv
from commands import inspect_command, columns_command, clean_command, visualize_command, analyze_command

def main():
  
  parser = argparse.ArgumentParser(description="Medical Data Explorer")
  parser.add_argument("command", choices=["inspect", "analyse", "visualize", "columns", "clean"])
  parser.add_argument("file_path")
  parser.add_argument("--column", choices=data_loader.COLUMN_NAMES)
  parser.add_argument("--output")

  args = parser.parse_args()

  df = load_csv(args.file_path)
  clean_df = data_cleaner.clean_dataset(df)

  if args.command == "inspect":
    inspect_command.handle(clean_df)

  elif args.command == "analyse":
    if args.column is None:
      print("Please choose a column with --column")
      print("Example: python3 src/main.py analyse datasets/cleveland.heart.csv --column age")
      return

    description = column_metadata.get_column_description(args.column)

    if data_analyzer.is_categorical_column(args.column):
      summary = data_analyzer.get_categorical_summary(clean_df, args.column)
      output_formatter.print_categorical_summary(args.column, description, summary)
      return

    if not data_analyzer.is_numeric_column(clean_df, args.column):
      print(f"{args.column} is not a numeric column")
      return

    summary = data_analyzer.get_column_summary(clean_df, args.column)
    output_formatter.print_numeric_summary(args.column, description, summary)

  elif args.command == "visualize":
    import data_visualizer
      
    target_distribution = data_analyzer.get_target_distribution(clean_df)
    data_visualizer.plot_target_distribution(target_distribution, args.output)

    if args.output:
      output_formatter.print_file_saved(args.output)

  elif args.command == "columns":
    output_formatter.print_available_columns(data_loader.COLUMN_NAMES)

  elif args.command == "clean":
    clean_command.handle(df, clean_df, args.output)

     
main()