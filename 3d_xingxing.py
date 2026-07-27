import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax_3d = fig.add_subplot(projection='3d')
x = np.random.randint(0,40,30)
y = np.random.randint(0,40,30)
z = np.random.randint(0,40,30)
for xx,yy,zz in zip(x,y,z):
    color = 'y'
    if 10<zz<20:
        color = '#C71585'
    elif zz>=20:
        color = '#008b8b'
    ax_3d.scatter(xx,yy,zz,c = color,marker = '*',s = 160,
                  linewidth = 1,edgecolors = 'black')

ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

ax_3d.set_title('scatter')
plt.show()
