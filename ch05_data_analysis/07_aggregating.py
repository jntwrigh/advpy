import numpy as np

arr31 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])

# this will also generate the array above
# arr31 = np.arange(1, 4) + np.arange(0, 10, 3)[:, np.newaxis]

print(np.sum(arr31))                                                # 78
print(arr31.sum())                                                  # 78

print(np.mean(arr31[:, 0]))                                         # 5.5
print(arr31[:, 0].mean())                                           # 5.5

print(np.var(arr31[1]))                                             # 0.667    ((4-5)^2 + (6-5)^2)/3
print(arr31[1].var())                                               # 0.667

print(np.std(arr31[1]))                                             # 0.816    sqrt() of 0.667 above
print(arr31[1].std())                                               # 0.816

print(np.prod(arr31[:2, :2]))                                       # 40
print(arr31[:2, :2].prod())                                         # 40
print(arr31.prod(axis=1))
