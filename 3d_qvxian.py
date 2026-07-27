import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
x1 = np.arange(-5,5,0.25)
y1 = np.arange(-5,5,0.25)
x1,y1 = np.meshgrid(x1,y1)
r1 = np.sqrt(x1**2 + y1**2)
z1 = np.sin(r1)
fig = plt.figure()
ax_3d = fig.add_subplot(projection = '3d')
ax_3d.plot_surface(x1,y1,z1,cmap = cm.coolwarm,linewidth = 0,antialiased = False)
plt.show()
