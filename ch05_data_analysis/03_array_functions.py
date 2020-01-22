import numpy as np

# linspace(start, end, num) - creates an array with num number of items evenly spaced between start and end
arr14 = np.linspace(0, 20, 5)       # [ 0. 5. 10. 15. 20. ]
print(arr14)

arr15 = np.arange(0, 15, 3)         # [ 0 3 6 9 12 ]
print(arr15)

arr16 = np.diag(np.arange(1, 6, 2))          # [[1 0 0] [0 3 0] [0 0 5]
print(arr16)

np.random.seed(1001)
arr17 = np.random.rand(2, 3)        # [[ 0.30623218  0.26506357  0.19606006] [0.43052148  0.02311355  0.19578192]]
print(arr17)

arr18 = np.tile([1, 2], [3, 3])
print(arr18)                        # [[1 2 1 2 1 2] [1 2 1 2 1 2] [1 2 1 2 1 2]]
