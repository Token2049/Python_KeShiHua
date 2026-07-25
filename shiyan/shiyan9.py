import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

labels = ['北京','上海','天津','重庆']

software_product = [4800, 3600, 1200, 950]
info_service = [7200, 5100, 1600, 1100]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
software_product = np.concatenate((software_product, [software_product[0]]))
info_service = np.concatenate((info_service, [info_service[0]]))
angles = np.concatenate((angles, [angles[0]]))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

ax.plot(angles, software_product, 'o-', linewidth=2, label='软件产品收入/亿元')
ax.plot(angles, info_service, 'o-', linewidth=2, label='信息技术服务收入/亿元')

ax.fill(angles, software_product, color='green', alpha=0.25)
ax.fill(angles, info_service, color='green', alpha=0.25)

ax.set_ylim(0, 10000)
ax.grid(True)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.title("2019年我国直辖市软件项目收入情况")

plt.figtext(0.7, 0.01, "数据来源：国家统计局")

plt.legend(loc="best")

plt.show()