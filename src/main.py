from data_loader import load_csv
import data_cleaner
import data_analyzer
import data_visualizer

df = load_csv("datasets/processed.cleveland.data")
clean_df = data_cleaner.remove_missing_values(df)

target_distribution = data_analyzer.get_target_distribution(clean_df)

data_visualizer.plot_target_distribution(target_distribution)

