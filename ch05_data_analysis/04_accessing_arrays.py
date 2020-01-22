# ------------------------------------------------
#             accessing arrays
import numpy as np

arr19 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(arr19[3, 1])                                          # 11
print(arr19[3][1])                                          # 11
print(arr19[2:, 1:])                                        # [ [8 9] [11 12] ]

print(arr19[-1])                                            # [10 11 12]
print(arr19[-2, -3])                                        # 7

arr20 = np.tile([1, 2, 3, 4], [4, 1])
print(arr20[1::2, 1::2])                                    # [[2 4][2 4]]

arr20[:,1] = 8
print(arr20)                                                # [[1 8 3 4] [1 8 3 4] [1 8 3 4] [1 8 3 4]]

print(arr20[:, [0,3]])                                      # [[1 4][1 4][1 4][1 4]]
print(arr20[(1, 2), :])                                     # [[1 8 3 4][1 8 3 4]]

print(arr20[:, np.array([True, False, True, False])])       # [[1 3][1 3]]

arr20[:, np.array([False, False, False, True])] = [[6], [7], [8], [9]]
print(arr20)