"""
        task 6_1.py     - scatter plot the batting averages from the
        previous exercise against atbats

"""
import matplotlib.pyplot as plt
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

# ----------------------------------------

data[:,3] = data[:,3] * 1000

max_avg_idx = data[:, 3].argmax()
max_avg = data[max_avg_idx, 3]
atbats = data[max_avg_idx, 1]

fig = plt.figure(figsize=(8,6), facecolor='#ccccff')
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
ax.scatter(data[:, 3], data[:, 1], marker='.', c='#cdcd24')
ax.annotate('Max', xy=(max_avg, atbats), xytext=(-30, 40), textcoords='offset points',
            arrowprops=dict(facecolor='#3333ff', headwidth=10, frac=0.3, width=2))
print('Max average and its atbats: {}, {}'.format(max_avg, atbats))

ax.legend([r'At bats'], loc='best', title='Legend')

plt.show()
