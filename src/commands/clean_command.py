import output_formatter 

def handle(df, clean_df, output_path=None):
  output_formatter.print_cleaning_summary(len(df), len(clean_df))

  if output_path:
    clean_df.to_csv(output_path, index=False, header=False)
    output_formatter.print_file_saved(output_path)