import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = [
    [6172, 1132, 437, 723, 429],
    [34.5, 32.8, 32.8, 31.1, 36.1],
    [53550, 46601, 55170, 35186, 70172]
]

columns = ['elevation', 'median_age', 'median_income']
index = ['Colorado Springs', 'Phoenix', 'Raleigh', 'Milwaukee', 'Seattle']

arr = np.array(data, dtype=int).transpose()
df4 = pd.DataFrame(arr, index=index, columns=columns)

'''
                  elevation  median_age  median_income
Colorado Springs       6172          34          53550
Phoenix                1132          32          46601
Raleigh                 437          32          55170
Milwaukee               723          31          35186
Seattle                 429          36          70172
'''

# ---------------------------------------------------------------

print(df4['elevation'])                             # a Series of the elevation column
print(df4['elevation'].Phoenix)                     # 1132
print(df4.get('elevation'))                         # a Series of the elevation column
print(df4.get('population'))                        # None
df4.get('elevation').plot()
plt.show()

print(df4[['elevation', 'median_income']])          # returns a DataFrame containing the elevation and median_income columns
print(df4[1:3])                                     # returns two rows: Phoenix, Raleigh
print(df4['elevation']['Colorado Springs'])         # 6172
print(df4[1:4]['elevation'])                        # returns 3 rows: Phoenix, Raleigh, Miwaukee with only elevation data

