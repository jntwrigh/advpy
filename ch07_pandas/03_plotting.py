import matplotlib.pyplot as plt
import pandas as pd

ser4 = pd.Series([218, 15, 619, 13, 1295],
                 index=['Mobile', 'San Diego', 'Chicago', 'New York City', 'Oklahoma City'],
                 name='City Elevations')

figure = plt.figure(facecolor='#fff5ff')
axis = figure.add_subplot(111)
axis.set_title('City Elevations')
axis.set_xlabel('Name')
axis.set_ylabel('Height (ft)')
ser4.plot(style='--', kind='line', ax=axis, color='#24a1f2', grid=True)        # same as ser4.plot.line()

plt.show()
