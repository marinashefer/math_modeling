import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('weaher.csv')

data['temperature'].hist(bins = 2)
data.plot()