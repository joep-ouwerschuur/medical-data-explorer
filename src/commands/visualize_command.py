import data_analyzer
import data_visualizer
import output_formatter

def handle(clean_df, output_path=None):
  target_distribution = data_analyzer.get_target_distribution(clean_df)
  data_visualizer.plot_target_distribution(target_distribution, output_path)

  if output_path:
    output_formatter.print_file_saved(output_path)