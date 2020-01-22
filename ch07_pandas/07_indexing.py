import numpy as np
import pandas as pd

df5 = pd.DataFrame(np.arange(16).reshape(4, 4),
                   index=['row0', 'row1', 'row2', 'row3'],
                   columns=['col0', 'col1', 'col2', 'col3'])

print(df5)
'''
     col0  col1  col2  col3
row0    0     1     2     3
row1    4     5     6     7
row2    8     9    10    11
row3   12    13    14    15
'''


print(df5.iloc[1:3])
'''
      col0  col1  col2  col3
row1     4     5     6     7
row2     8     9    10    11
'''


print(df5.loc['row1'])
'''
col0    4
col1    5
col2    6
col3    7
Name: row1, dtype: int32
'''


print(df5.ix[1:3, 'col2'])
'''
row1     6
row2    10
Name: col2, dtype: int32
'''


# Other examples:

print(df5.iloc[2:, 2:])
'''
      col2  col3
row2    10    11
row3    14    15
'''


print(df5.loc['row2':, 'col2':])
