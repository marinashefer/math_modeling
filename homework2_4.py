import glob
import pandas as pd

filenames = glob.glob("*.csv")

new = []
for filename in filenames:
    new.append(pd.read_csv(filename))

big_frame = pd.concat(new, ignore_index=True)
print(big_frame)