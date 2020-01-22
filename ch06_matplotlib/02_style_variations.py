import matplotlib.pyplot as plt
import numpy as np

x_ticks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
x = np.arange(1, 13)
y = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

plt.xlabel('Month')
plt.ylabel('Number of Days')
plt.xticks(x, x_ticks)
plt.plot(x, y, 'c--')
# plt.plot(x, y, 'rs:')
# plt.plot(x, y, 'mx-')
# plt.plot(x, y, 'g*-.')
plt.show()
