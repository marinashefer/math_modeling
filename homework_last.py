import pandas as pd

data = pd.read_csv('titanic.csv')

mean_age = round(data['Age'].mean())
print(mean_age)

print(pd.isnull(data['Age']))

data['Age'].fillna(mean_age, inplace = True)
print(data)

print(data.sort_values(by='Name'))
print(data)