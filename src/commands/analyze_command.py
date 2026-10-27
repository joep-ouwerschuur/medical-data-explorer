import column_metadata, data_analyzer, output_formatter

def handle(clean_df, column=None):

  if column is None:
    print("Please choose a column with --column")
    print("Example: python3 src/main.py analyse datasets/cleveland.heart.csv --column age")
    return

  description = column_metadata.get_column_description(column)

  if data_analyzer.is_categorical_column(column):
    summary = data_analyzer.get_categorical_summary(clean_df, column)
    output_formatter.print_categorical_summary(column, description, summary)
    return

  if not data_analyzer.is_numeric_column(clean_df, column):
    print(f"{column} is not a numeric column")
    return
  
  summary = data_analyzer.get_column_summary(clean_df, column)
  output_formatter.print_numeric_summary(column, description, summary)
  return