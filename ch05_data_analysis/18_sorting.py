import numpy as np

arr = np.roll(np.arange(1, 10).reshape((3, 3)), 2)
print(arr)                                              # [[8 9 1]
                                                        #  [2 3 4]
                                                        #  [5 6 7]]

sort_by_col0 = arr[arr[:, 0].argsort()]
print(sort_by_col0)

sort_by_col1 = arr[arr[:, 2].argsort()]
print(sort_by_col1)
