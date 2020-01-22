"""
        task 5_3.py     - This represents a modified version of the exercise where only batting averages
                           1957 or later were considered.

                           Year information can be found in the second column of the data file.

"""
import numpy as np
import warnings

np.set_printoptions(precision=3, suppress=True)
warnings.filterwarnings('ignore')

data = np.genfromtxt('../../resources/baseball/Batting.csv', skip_header=1,
                     usecols=(1, 6, 8), delimiter=',', dtype=float)
print(data.shape)

data = data[data[:, 1] >= 502]
data = data[data[:, 0] >= 1957]

avgs = data[:, 2] / data[:, 1]
data = np.column_stack([data, avgs])
print(data.shape)

data = data[data[:, 3].argsort()]
print(data[-1:-100:-1, 3])