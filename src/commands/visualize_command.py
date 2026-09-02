import data_analyzer
import data_visualizer
import output_formatter

def handle(clean_df, output_path=None, chart="target", column=None, group_by=None):

  if chart == "target":
    target_distribution = data_analyzer.get_target_distribution(clean_df)
    data_visualizer.plot_target_distribution(target_distribution, output_path)

  elif chart == "cholesterol-by-target":
    average_values = data_analyzer.get_average_by_category(clean_df, "chol", "num")
    data_visualizer.plot_average_by_category(average_values, output_path)

  elif chart == "average-by-category":
    average_values = data_analyzer.get_average_by_category(clean_df, column, group_by)
    data_visualizer.plot_average_by_category(average_values, output_path)

  if output_path:
    output_formatter.print_file_saved(output_path)