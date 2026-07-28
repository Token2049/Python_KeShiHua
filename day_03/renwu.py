import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. 创建画布与坐标轴
fig, ax = plt.subplots(figsize=(10, 6))
# 生成正弦曲线数据 x范围0~6，足够密集保证曲线平滑
x_total = np.linspace(0, 6, 1000)
y_total = np.sin(x_total)

# 绘制正弦曲线（默认蓝色线条）
ax.plot(x_total, y_total)
# 设置坐标轴范围，匹配示例图
ax.set_xlim(-0.2, 6.2)
ax.set_ylim(-1.1, 1.1)
ax.grid(False)

# 2. 创建红色圆点标记，初始位置在最左端 x=0,y=0
point, = ax.plot([], [], 'ro', markersize=8)
# 创建坐标文本，放在图表右上角实时更新坐标
text = ax.text(3.2, 0.9, '', fontsize=18)

# 3. 动画初始化函数（修复：传入列表）
def init():
    x0 = 0
    y0 = np.sin(x0)
    point.set_data([x0], [y0])  # 包裹成列表序列
    text.set_text(f'x={x0:.3f}, y={y0:.3f}')
    return point, text

# 4. 动画更新函数：第i帧，圆点沿曲线移动（修复：传入列表）
def update(frame):
    # 总帧数100，x从0均匀走到6
    x_now = 6 * (frame / 99)
    y_now = np.sin(x_now)
    point.set_data([x_now], [y_now])  # 包裹成列表序列
    # 更新坐标文本，保留3位小数，和示例格式一致
    text.set_text(f'x={x_now:.3f}, y={y_now:.3f}')
    return point, text

# 5. 创建动画：总帧数100，间隔100ms
ani = FuncAnimation(
    fig=fig,
    func=update,
    init_func=init,
    frames=100,        # 总帧数100
    interval=100,      # 每帧间隔100毫秒
    blit=True,         # 加速动画渲染
    repeat=True        # 循环播放动画
)

plt.show()