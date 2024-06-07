import pandas as pd

data = pd.read_csv('clients.csv')

print(data.info)

print('Количество клиентов в каждой стране:', data['countries'].value_counts())

print('Средний возраст клиентов для каждой из стран:', data.groupby(by='countries')['age'].mean())