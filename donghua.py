import numpy as np
import matplotlib.pyplot as plt
# 导入创建动画的类FuncAnimation
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
y = np.sin(x)
# 绘制正弦曲线
line, = ax.plot(x, y)

# 定义控制每一帧动画绘制操作的函数
def animate(frame):
    # 根据frame的值设置线条的y坐标值
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,

# 定义控制动画初始状态的函数
def init():
    # 设置线条的坐标值
    line.set_ydata(np.sin(x))
    return line,

# 创建动画
func_ani = FuncAnimation(
    fig=fig,
    func=animate,
    frames=100,
    init_func=init,
    interval=100
)

plt.show()