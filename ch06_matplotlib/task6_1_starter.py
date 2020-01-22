import matplotlib.pyplot as plt
import numpy as np
import warnings

np.set_printoptions(precision=3, suppress=True)
warnings.filterwarnings('ignore')

data = np.genfromtxt('../resources/baseball/Batting.csv', skip_header=1,
                     usecols=(1, 6, 8), delimiter=',', dtype=float)
print(data.shape)

data = data[data[:, 1] >= 502]
data = data[data[:, 0] >= 1957]

avgs = data[:, 2] / data[:, 1]
data = np.column_stack([data, avgs])
print(data.shape)

data = data[data[:, 3].argsort()]
print(data[-1:-100:-1, 3])


# add your plot code here, note: you may opt to use your task2_2_starter.py
# solution instead.

# Step 1. Create a figure and add axes.  set_xlabel() and set_ylabel()

# Step 2. Invoke scatter() from the figure.

# Step 3. Create a legend and annotate the maximum value.

# Step 4. Show the plot.
