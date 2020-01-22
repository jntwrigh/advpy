import pandas as pd


ser4 = pd.Series([218, 15, 619, 13, 1295],
                 index=['Mobile', 'San Diego', 'Chicago', 'New York City', 'Oklahoma City'],
                 name='City Elevations')


# -----------Accessing a Series----------------
print(ser4['Mobile'])                                   # 218
print(ser4.get('New York City'))                        # 13
try:
    print(ser4['Albuquerque'])                          # KeyError
except KeyError:
    print('not found')                                  # not found
print(ser4.get('Albuquerque'))                          # None
print(ser4.get('Albuquerque', -1))                      # -1
print(ser4[['Chicago', 'Oklahoma City']])               # Chicago 619  Oklahoma City 1295 Name: City Elevations, dtype: int64
print(type(ser4[['Chicago', 'Oklahoma City']]))         # <class 'pandas.core.series.Series'>
print(ser4.Chicago)                                     # 619
print(ser4[1:3])                                        # San Diego 15 Chicago 619 Name: CIty Elevations, dtype: int64
print('Series: {name}, Median: {median}'.format(name=ser4.name, median=ser4.median()))  # Series: City Elevations, Median: 218.0

print(ser4.describe())
print(ser4.describe()['mean'])
print(ser4.index)
print(ser4.values)
