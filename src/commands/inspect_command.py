import data_inspector

def handle(clean_df):
  data_inspector.show_head(clean_df)
  data_inspector.show_shape(clean_df)
  data_inspector.show_missing_values(clean_df)

