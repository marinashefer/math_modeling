import glob
import pandas as pd

data1 = pd.read_csv('weather.csv')
data2 = pd.read_csv('sales.csv')

data2['sales'].append(data1)
print(data1)