import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y1 = x**4 - x**3 - 6*x**2
y2 = -x**5 + 4*x**3

figure = plt.figure(figsize=(12, 6))

sub1 = figure.add_axes((0.1, 0.1, 0.8, 0.8))
sub1.plot(x, y1, color='#339955', lw=3.0, ls='solid')
sub1.plot(x, y2, color='#253397', lw=3.0, ls='solid')
sub1.legend([r'y1 = $x^4 + x^3 - 6x^2$', r'y2 = $\mathdefault{-x^5 + 4x^3}$'],
            loc='best', title='Legend', ncol=2)

sub1.annotate(s=r'$E = \frac{mc^2}{\sqrt{1-\frac{v^2}{c^2}}}$',
              xy=(0.7, 0.6),
              xycoords='figure fraction',
              fontsize=28)

sub1.annotate(r'$y2(1.6)$',
              xy=(1.6, -1.6**5 + 4*1.6**3),
              xycoords='data',
              xytext=(-100, +20),
              textcoords='offset points',
              fontsize=18,
              arrowprops=dict(facecolor='#3333ff', headwidth=10, width=2, edgecolor=None))

figure.savefig('legendary.png')

plt.show()
