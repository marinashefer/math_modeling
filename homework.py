import pandas as pd

data = pd.read_csv('data.csv')

print(data.head(5))
print(data.tail(5))

print(data.info)

print(data.describe())

missing_values = data.isnull().sum()
print(missing_values)
#=>все хорошо!