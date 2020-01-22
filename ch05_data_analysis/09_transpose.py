import numpy as np

# -----------------transpose--------------------
arr35 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(arr35.shape)                              # (4, 3)
arr36 = arr35.transpose()
print(arr36.shape)                              # (3, 4)
print(arr36)

