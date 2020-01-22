import numpy as np
import pandas as pd


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

print(df4.values)
print(df4.describe())
print(df4.describe())
print(df4.info(verbose=True))
print(df4.T)
