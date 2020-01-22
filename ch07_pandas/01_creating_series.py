import pandas as pd


# -----------Creating Series----------------
ser1 = pd.Series([212, 32, 0, -273])
print(ser1)


ser2 = pd.Series(name='City Elevations',
                 index=['Colorado Springs', 'Phoenix', 'Raleigh', 'Milwaukee', 'Seattle'],
                 data=[6172, 1132, 437, 723, 429])
print(ser2)


city_elevations = {'Denver': 5883, 'Austin': 632, 'Philadelphia': 21, 'Billings': 3649, 'Anchorage': 144}
ser3 = pd.Series(city_elevations, name='City Elevations')
print(ser3)
