import numpy as np
import pandas as pd


df1 = pd.DataFrame([['Colorado Springs', 'Phoenix', 'Raleigh', 'Milwaukee', 'Seattle'],
              [6172, 1132, 437, 723, 429]] )
print(df1)
df1.index = ['City', 'Elevation']
print(df1)


# -------------initializing using a dictionary---------------
data = {
    'elevation': [6172, 1132, 437, 723, 429],
    'median_age': [34.5, 32.8, 32.8, 31.1, 36.1],
    'median_income': [53550, 46601, 55170, 35186, 70172],
}


df2 = pd.DataFrame(data, index=['Colorado Springs', 'Phoenix', 'Raleigh', 'Milwaukee', 'Seattle'])

print(df2)


# -------------using lists, setting index & columns after---------------
data = [
    [6172, 1132, 437, 723, 429],
    [34.5, 32.8, 32.8, 31.1, 36.1],
    [53550, 46601, 55170, 35186, 70172]
]

columns = ['elevation', 'median_age', 'median_income']
index = ['Colorado Springs', 'Phoenix', 'Raleigh', 'Milwaukee', 'Seattle']

arr = np.array(data, dtype=int)
df3 = pd.DataFrame(arr.transpose(), index=index, columns=columns)

print(df3)
