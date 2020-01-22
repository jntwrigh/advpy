import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.25)
y1 = 2*x + 3
y2 = 3*x**2-1

figure = plt.figure(figsize=(12, 6), facecolor='#fff5ff')
sub1 = figure.add_subplot(2, 3, (1, 4))
sub1.plot(x, y1, 'b-', x, y2, 'r-')
sub1.set_title('Using Default Axis Ranges')

sub2 = figure.add_subplot(2, 3, 2)
sub2.plot(x, y1, 'b-', x, y2, 'r-')
sub2.axis('tight')
sub2.set_title('Using Tight Axes')

sub3 = figure.add_subplot(2, 3, 3)
sub3.plot(x, y1, 'b-', x, y2, 'g-')
sub3.set_xticks(np.linspace(1.52, 1.56, 5))
sub3.set_xlim((1.52, 1.56))
sub3.set_ylim((6.0, 6.1))
sub3.set_title('Using Custom Axes')

sub5 = figure.add_axes((0.46, 0.1, 0.4, 0.3))
sub5.plot(x, y1, 'b-', color='#339955', lw=2.5)
sub5.plot(x, y2, 'r-', color='#2533b7', lw=5.0, ls='dashdot')
sub5.set_yticks(np.linspace(-5, 10, 5))
sub5.set_xlim((0, 4))
sub5.set_ylim((-5, 10))
sub5.set_xlabel('x-values')
sub5.set_ylabel('y-values')
sub5.grid(color='g', alpha=0.5, ls='dashed', lw=0.5)
sub5.set_title('Using Custom Axes, Grid Lines, and Labels')

plt.show()
