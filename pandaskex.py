import pandas as pd

df = pd.read_csv('sample.csv')
print(df)
print(df['age'].mean())


