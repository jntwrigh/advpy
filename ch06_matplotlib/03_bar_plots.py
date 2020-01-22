import matplotlib.pyplot as plt
import numpy as np

cities = ['Colorado Springs', 'Phoenix', 'Raleigh', 'Milwaukee', 'Seattle']
cities_idx = np.arange(len(cities))
elevations = [6172, 1132, 437, 723, 429]

plt.xlabel('City')
plt.ylabel('Elevation')

bar_width = 0.5
plt.xticks(cities_idx + bar_width/2, cities)
plt.bar(left=cities_idx, height=elevations, width=bar_width)

plt.show()
