import numpy as np
import warnings
warnings.filterwarnings('ignore')
np.set_printoptions(suppress=True)


# ----------------------------------------------
# remove rows with an nan or infinity...
data = np.genfromtxt('city_data2.dat', delimiter=',', usecols=(1,2), dtype=np.float32)
data[1, 1] = data[1, 1]/0
print(data)

print(data[~np.isnan(data).any(axis=1)])            # remove NaN rows
print(data[~np.isinf(data).any(axis=1)])            # remove inf rows
print(data[np.isfinite(data).all(axis=1)])          # remove both rows


# Understanding any() a little better...
data = np.array([[True, False, False],
                 [False, False, True],
                 [False, False, False]])
print(np.any(data))             # True
print(np.any(data, axis=0))     # [True False True]
print(np.any(data, axis=1))     # [True True False]
