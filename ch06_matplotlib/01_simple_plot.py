import matplotlib as mpl
mpl.use('Qt4Agg')                           # our default, so this is not necessary

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = 10 * np.random.rand(1, 10).squeeze()
plt.ylabel('Random Values')
plt.xlabel('Numbers')
plt.plot(x, y, 'ro')

x2 = np.arange(2, 11, 2)
y2 = 10 * np.random.rand(1, 5).squeeze()
plt.plot(x2, y2)

plt.show()
