import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)
y1 = 3 * x
y2 = x ** 2
y3 = 2 * x ** 2 + 3 * x + 1

plt.plot(x, y1, 'k-')
plt.plot(x, y2, 'b--v')
plt.plot(x, y3, 'r-.o')

plt.text(-8, 0, 'y1=3x')

bbox2 = dict(boxstyle="round", facecolor="gray", edgecolor="green")
plt.text(-8.5, 150, 'y3=2x^2+3x+1', color='red', bbox=bbox2)

bbox3 = dict(boxstyle="round", facecolor="yellow", edgecolor="blue")
plt.annotate('node(0,0)',
             xy=(0, 0),
             xytext=(-1, 50),
             fontsize=12, color='red', weight='bold',
             bbox=bbox3,
             arrowprops=dict(arrowstyle='->', color='green'))

plt.grid()

plt.show()