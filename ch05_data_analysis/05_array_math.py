import numpy as np

arr22 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr23 = np.eye(3)

arr24 = arr22 + arr23                       # [[2. 2. 3.][4. 6. 6.][7. 8. 10.]]
print(arr24)

arr25 = np.full((1, 3), 1) + arr22          # [[2. 3. 4.][5. 6. 7.][8. 9. 10.]]
print(arr25)

arr26 = arr22 - arr23                       # [[0. 2. 3.][4. 4. 6.][7. 8. 8.]]
print(arr26)

arr27 = arr22 * arr23                       # same as np.multiply(arr1, arr2)
print(arr27)                                # [[1. 0. 0.][0. 5. 0.][0. 0. 9.]]

a = b = np.array([1, 2, 3])
c = np.array([[1, 2],[3, 4]])
print(np.dot(a, b))                         # 14
print(np.cross(a, c))                       # [[-6 3 0][-12 9 -2]



# ---------------------------------------
#  array broadcasting...

arr  = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.ones((1, 3))
for row in arr:
    row = row + arr2

print(arr2)

# the operation below is called array broadcasting
# which allows for operations on different size arrays...

print(arr + np.ones((1, 3)))                        # [[2 3 4] [5 6 7]]
