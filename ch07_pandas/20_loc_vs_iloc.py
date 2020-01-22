import pandas as pd

ser = pd.Series(1, index=[10, 9, 8, 1, 2, 3, 4, 5])
print(ser)
print(ser.iloc[:3])
print(ser.loc[:3])


import pandas as pd

df = pd.DataFrame(1, columns=[4, 3, 2, 1], index=[10, 9, 8, 1, 2, 3, 4, 5])
print(df)
print(df.iloc[:3, :3])
print(df.loc[:3, :3])
