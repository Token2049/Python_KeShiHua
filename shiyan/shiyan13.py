import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = [38.26, 27.14, 22.53, 12.07]
labels = ["普通本专科", "成人本专科", "网络本专科", "研究生"]

fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    data,
    labels=labels,
    autopct='%.2f%%',
    pctdistance=0.01,
    
    startangle=90,
    wedgeprops={'width': 0.3, 'edgecolor': 'white'}
)

plt.title("2019年全国高等教育毕业生数占比情况")

plt.figtext(0.7, 0.01, "数据来源：国家统计局")

plt.legend(loc="best")

plt.show()