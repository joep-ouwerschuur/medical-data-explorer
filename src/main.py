from data_loader import load_csv

df = load_csv("datasets/processed.cleveland.data")

print(df.head())
print(df.shape)

