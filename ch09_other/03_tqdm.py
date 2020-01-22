"""
        03_tqdm.py

        Uses the 3rd Party tool: tqdm.  To use this module:
            pip install tqdm (unless using Anaconda)

"""
import time

import pandas as pd
import tqdm
avgs = []

batting = pd.read_csv('../resources/baseball/Batting.csv',
                      usecols=('yearID', 'AB', 'H'))
batting = batting.loc[(batting['yearID'] >= 1957) & (batting['AB'] >= 502)]

for idx, row in tqdm.tqdm(batting.iterrows(), total=batting.shape[0]):
    avg = row['H'] / row['AB']
    time.sleep(0.01)
    avgs.append(avg)
print(len(avgs))