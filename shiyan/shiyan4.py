import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, color='red', linewidth=1, label='sin(x)')
plt.plot(x, y_cos, color='blue', linestyle='--', label='cos(x)')

plt.legend(title='curve', loc='lower left', edgecolor='green', fontsize='small', ncol=2)

plt.show()