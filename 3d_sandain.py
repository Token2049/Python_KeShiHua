import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax_3d = fig.add_subplot(projection='3d')
x_data = np.random.randint(1,10,10)
y_data = np.random.randint(1,10,10)
z_data = np.random.randint(1,10,10)
ax_3d.scatter(x_data,y_data,z_data,c = 'red')
plt.show()
