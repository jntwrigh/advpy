import numpy as np

arr37 = np.arange(1, 13).reshape((3, 4))

for row in arr37:
    print(row, end=' ')


for elem in np.nditer(arr37):
    print(elem, end=' ')


for col in arr37.T:
    print(col, end=' ')
print(arr37.strides)
print(arr37.T.strides)

arr38 = arr37.T
arr38[1, 0] = 10
print(arr37[0, 1])
