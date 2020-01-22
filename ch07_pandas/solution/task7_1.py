"""
        task 7_1.py     - Using only Pandas, repeat the Batting average
                          exercise
                          - Display the top 100 batting averages
                          - Find the 50% average
                          - Plot the averages vs. atbats

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True, precision=3)


data = pd.read_csv('../../resources/baseball/Batting.csv',
                   usecols=('yearID', 'AB', 'H'))

data = data.loc[(data['yearID'] >= 1957) & (data['AB'] >= 502)]

data['avgs'] = data.loc[:, 'H'] / data.loc[:, 'AB']

data.sort_values(by='avgs', inplace=True, ascending=False)

print(data.shape)
print(data.head())
print(data.describe().loc['50%', 'avgs'])

data.plot(kind='scatter', x='avgs', y='AB', marker='.')



plt.show()

