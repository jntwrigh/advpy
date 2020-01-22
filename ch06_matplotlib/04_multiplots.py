import matplotlib.pyplot as plt
import numpy as np

cities = ['Colorado Springs', 'Phoenix', 'Raleigh', 'Milwaukee', 'Seattle']
cities_idx = np.arange(5)
elevations = [6172, 1132, 437, 723, 429]
populations = [431, 1488, 423, 599, 634]
plt.xlabel('Cities and Populations')
plt.ylabel('Elevation (ft), Population (thousands)')
plt.plot(cities_idx, elevations, 'b-',cities_idx, populations, 'r-', linewidth=4.0)
plt.show()
