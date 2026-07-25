import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)

plt.plot(x, y, color='red', linewidth=3)

plt.title("AC voltage")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

xticks_num = [2, 4, 6, 8, 10]
xticks_text = ["Two", "Four", "Six", "Eight", "Ten"]
plt.xticks(xticks_num, xticks_text, color='red', fontstyle='italic')

plt.show()