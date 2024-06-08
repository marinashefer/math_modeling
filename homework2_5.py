import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('weather.csv')

data['temperature'].plot(kind = 'hist', bins = 2)
plt.savefig('temperature.png')