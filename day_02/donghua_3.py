import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

plt.rcParams["font.sans-serif"] = ["simHei"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 1. 创建画布
fig = plt.figure()

# 2. 添加绘图区域，指定投影类型为3D
ax_3d = fig.add_subplot(projection='3d')

# 3. 绘制散点
xx = np.random.randint(0, 40, 30)
yy = np.random.randint(0, 40, 30)
zz = np.random.randint(0, 40, 30)
stars = ax_3d.scatter(
    xx, yy, zz,
    color='yellow',
    marker='*',
    s=160,
    linewidth=1,
    edgecolor='black'
)

# 4. 定制图表
ax_3d.set_xlabel('X轴')
ax_3d.set_ylabel('Y轴')
ax_3d.set_zlabel('Z轴')
ax_3d.set_title('三维散点图', fontproperties='simhei', fontsize=14)

# 定义动画绘制操作的函数
def animate(frame):
    # 根据frame的奇偶性区分星星的颜色
    if frame % 2 == 0:
        color = 'yellow'
    else:
        color = 'white'
    # 设置星星的颜色
    stars.set_color(color)
    # 设置星星的边框颜色
    stars.set_edgecolor('black')
    return stars,

# 创建动画
ani = FuncAnimation(
    fig=fig,
    func=animate,
    frames=100,
    interval=1000
)

# 5. 展示图表
plt.show(block=True)