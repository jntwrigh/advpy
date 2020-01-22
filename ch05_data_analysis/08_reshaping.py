import numpy as np


# ------------reshape()-------------------------------
arr32 = np.arange(1, 17).reshape((4,4))                 # [[ 1  2  3  4][5  6  7  8][9 10 11 12][13 14 15 16]]
print(arr32)


# ------------ravel()-------------------------------
print(np.ravel(arr32)[8])                               # 9
np.ravel(arr32)[6] = 100
print(arr32)                                            # [[ 1  2  3  4][5  6  100  8][9 10 11 12][13 14 15 16]]
print(arr32.shape)                                      # (4, 4)


# -----------squeeze()------------------------------
arr33 = np.array([[[[0], [1], [2]], [[3], [4], [5]]]])
print(arr33)
print(arr33.shape)                                      # (1, 2, 3, 1)

arr34 = arr33.squeeze()
print(arr34)                                            # [[0 1 2] [3 4 5]]
print(arr34.shape)                                      # (2, 3)
print(arr33.shape)                                      # (1, 2, 3, 1)
