import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y1 = 3 * x
y2 = x ** 2
y3 = 2 * x ** 2 + 3 * x + 1

plt.plot(x, y1, 'k-')
plt.plot(x, y2, 'b--v')
plt.plot(x, y3, 'r-.o')

plt.show()