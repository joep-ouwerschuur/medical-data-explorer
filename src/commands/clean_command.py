import output_formatter 

def handle(clean_df, cleaning_report, output_path=None):
  output_formatter.print_cleaning_summary(cleaning_report)

  if output_path:
    clean_df.to_csv(output_path, index=False, header=False)
    output_formatter.print_file_saved(output_path)