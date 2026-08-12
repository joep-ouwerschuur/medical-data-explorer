from data_loader import load_csv
import data_cleaner
import data_analyzer

df = load_csv("datasets/processed.cleveland.data")
clean_df = data_cleaner.remove_missing_values(df)

print("Average age:")
print(data_analyzer.get_average_age(clean_df))
print("\nTarget distribution:")
print(data_analyzer.get_target_distribution(clean_df))
print("\nAverage cholesterol by target:")
print(data_analyzer.get_average_cholesterol_by_target(clean_df))


