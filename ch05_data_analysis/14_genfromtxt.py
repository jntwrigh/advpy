import numpy as np


# ---------------------------------------------------------
# basic example
result = np.genfromtxt('tennis.dat', delimiter=',', dtype=float, usecols=(1,2))
print('Basic Example')
print(result)
print(result.dtype)


# ---------------------------------------------------------
# reading as structured data
data = np.genfromtxt('city_data1.dat', delimiter=',', dtype=('|U50', '<i4', '<f8'))
print('Structured data: compound dtypes')
print(data)
print(data.shape)


# ---------------------------------------------------------
# indicating data types
data = np.genfromtxt('city_data1.dat', delimiter=',', dtype=object)
print('Object-based: all types treated sequences of bytes')
print(data)
print(data.shape)
print(data.dtype)



# ---------------------------------------------------------
# accessing structured data sub-items using 'names'
data = np.genfromtxt('city_data1.dat', delimiter=',',
                     names=['name', 'elev', 'pop'],
                     dtype=['|U50', '<i4', '<i8'])
print('Accessing structured data sub-items')
print(data['name'])


# ---------------------------------------------------------
# works similar to the previous example
data = np.genfromtxt('city_data1.dat', delimiter=',',
                     dtype=[('name', '|U50'), ('elev', '<i4'), ('pop', '<f8')])
print(data['elev'][0])


# ---------------------------------------------------------
# handling missing values
data = np.genfromtxt('city_data2.dat', delimiter=',',
                     filling_values=['', -999, -1],
                     dtype=('S50', '<i4', '<f8'))
np.set_printoptions(suppress=True)
print('Using filling_values:')
print(data)
print(data.shape)
