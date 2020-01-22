import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print('stack:')
result1 = np.stack([v1, v2])
result2 = np.stack([v1, v2], axis=1)
print(result1)                              # [[1 2 3]
                                            #  [4 5 6]]
print(result2)                              # [[1 4]
                                            #  [2 5]
                                            #  [3 6]]

print('\ncolumn_stack: ')
result = np.column_stack([v1, v2])
print(result)                               # [[1 4]
                                            #  [2 5]
                                            #  [3 6]]
print(result.T)                             # [[1 2 3]
                                            #  [4 5 6]]

print('\nhstack:')
print(np.hstack((v1, v2)))                  # [1 2 3 4 5 6]
print(np.hstack((result, result)))          # [[1 4 1 4]
                                            #  [2 5 2 5]
                                            #  [3 6 3 6]]

print('\nvstack:')
print(np.vstack([v1, v2]))                  # [[1 2 3]
                                            #  [4 5 6]]

print('\nconcatenate:')
result = np.array([[1, 2, 3], [4, 5, 6]])
print(np.concatenate([v1, v2]))             # [1 2 3 4 5 6]
print(np.concatenate([result, result]))     # [[1 2 3]
                                            #  [4 5 6]
                                            #  [1 2 3]
                                            #  [4 5 6]]

print('\nroll:')
v1 = np.array([1, 2, 3])
a1 = np.array([[1, 2], [3, 4], [5, 6]])     # [[1 2]
                                            #  [3 4]
                                            #  [5 6]]

print(np.roll(v1, 1))                       # [3 1 2]
print(np.roll(v1, -1))                      # [2 1 3]

print(np.roll(a1, -1, axis=0))              # [[3 4]
                                            #  [5 6]
                                            #  [1 2]]

print(np.roll(a1, 1, axis=1))               # [[3 4]
                                            #  [5 6]
                                            #  [1 2]]
