import numpy as np

print('First with a 1D array:')
arr = np.arange(1, 7)
print(arr)                                          # [1 2 3 4 5 6]
arr_match = arr <= 3
print(arr_match)                                    # [True True True False False False]

new_arr = arr[arr_match]
print(new_arr)                                      # [1 2 3]


arr2 = np.arange(11, 17)
print(arr2)                                         # [11, 12, 13, 14, 15, 16]
new_arr = arr2[arr <= 3]
print(new_arr)                                      # [4 5 6]


