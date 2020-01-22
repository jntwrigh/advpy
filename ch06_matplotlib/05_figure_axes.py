import matplotlib.pyplot as plt

figure = plt.figure(figsize=(8, 4))

sub221 = figure.add_subplot(221, axisbg='#ffffcc')
sub221.text(0.5, 0.5, s='subplot(221)', ha='center', va='center', fontsize=20, alpha=.5, color='#287171')

sub222 = figure.add_subplot(222, axisbg='#4455cc')
sub222.text(0.5, 0.5, 'subplot(222)', ha='center', va='center', fontsize=20, color='#5511aa')

sub223 = figure.add_subplot(223, axisbg='#aa5422')
sub223.text(0.5, 0.5, 'subplot(223)', ha='center', va='center', fontsize=20, color='g')

sub224 = figure.add_subplot(224, axisbg='#ccddee')
sub224.text(0.5, 0.5, 'subplot(224)', ha='center', va='center', fontsize=20,
            color='#ff0000')

plt.show()
