from data_loader import load_csv
import data_inspector
import data_cleaner

df = load_csv("datasets/processed.cleveland.data")


data_inspector.show_shape(df)
data_inspector.show_missing_values(df)

clean_df = data_cleaner.remove_missing_values(df)
clean_df = data_cleaner.remove_duplicates(clean_df)

data_inspector.show_shape(clean_df)
data_inspector.show_missing_values(clean_df)



