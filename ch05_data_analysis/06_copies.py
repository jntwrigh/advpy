import numpy as np

arr28 = np.arange(1, 5) + np.arange(0, 13, 4)[:, np.newaxis]

arr29 = np.array(arr28, copy=False)
arr29[2, 2] = 100
print(arr28)

arr30 = np.full_like(arr28, 10)
print(arr30)
