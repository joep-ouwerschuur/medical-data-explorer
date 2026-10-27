import argparse
import data_cleaner
import data_loader

from data_loader import load_csv

from commands import inspect_command
from commands import clean_command
from commands import columns_command
from commands import analyze_command
from commands import visualize_command

def main():
  
  parser = argparse.ArgumentParser(description="Medical Data Explorer")
  parser.add_argument("command", choices=["inspect", "columns", "analyse", "visualize", "clean"])
  parser.add_argument("file_path")
  parser.add_argument("--column", choices=data_loader.COLUMN_NAMES)
  parser.add_argument("--output")
  parser.add_argument("--chart", choices=["target", "cholesterol-by-target", "average-by-category"], default="target")
  parser.add_argument("--group-by", choices=data_loader.COLUMN_NAMES)

  args = parser.parse_args()

  if (
    args.command == "visualize"
    and args.chart == "average-by-category"
    and (args.column is None or args.group_by is None)
  ):
    parser.error(
      "--column and --group-by are required for average-by-category"
    )

  df = load_csv(args.file_path)
  clean_df = data_cleaner.clean_dataset(df)

  if args.command == "inspect":
    inspect_command.handle(clean_df)

  elif args.command == "columns":
    columns_command.handle()

  elif args.command == "analyse":
    analyze_command.handle(clean_df, args.column)

  elif args.command == "visualize":
    visualize_command.handle(clean_df, args.output, args.chart, args.column, args.group_by)

  elif args.command == "clean":
    clean_command.handle(df, clean_df, args.output)

main()