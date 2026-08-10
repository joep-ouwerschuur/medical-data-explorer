from data_loader import load_csv
from data_inspector import *

df = load_csv("datasets/processed.cleveland.data")

# print(df.head())
# print(df.shape)

show_head(df)
