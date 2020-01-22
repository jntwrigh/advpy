import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(type(arr))                # <class 'numpy.ndarray'>

print('Shape: {0}, Size: {1}, Axes: {2}, Types: {3}, Strides: {4}'
      .format(arr3.shape, arr3.size, arr3.ndim, arr3.dtype, arr3.strides))      # (4, 3)  12  2  int32  (12, 4)

print(arr3)                     # [[ 1  2  3][4  5  6][7  8  9][10 11 12]]
print(arr3[0])                  # [1 2 3]
print(arr3[0][2])               #3


arr4 = np.zeros((2, 2))
print(arr4)                     # [[ 0. 0.] [ 0. 0.]]
print(arr4.tolist())

arr5 = np.ones((2, 2))
print(arr5)                     # [[ 1. 1.] [ 1. 1.]]

arr6 = np.full((2, 2), 6)
print(arr6)                     # [[ 6. 6.] [ 6. 6.]]

arr7 = np.eye(2)
print(arr7)                     # 2x2 identity matrix

print(np.eye(3))                # [[1. 0. 0.][0. 1. 0.][0. 0. 1.]]
print(np.eye(3, 3, 1))          # defines 3 rows, 3 cols, and the diagonal offset: [[0. 1. 0.][0. 0. 1.][0. 0. 0.]]
print(np.eye(3, k=-1))          # defines 3 rows/cols, diagonal offset is negative: [[0. 0. 0.][1. 0. 0.][0. 1. 0.]]

arr8 = np.empty((2, 2))
print(arr8)                     # 2x2 random numbers

arr9 = np.array(range(11, 20))          # [11 12 13 14 15 16 17 18 19]
print(arr9)
