import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

years = np.array([2007,2008,2009,2010,2011,2012,2013,2014,2015,2016])
all_emp = [75321,75564,75828,76105,76420,76704,76977,77253,77451,77603]
town_emp = [29350,30210,31120,34687,35914,37102,38240,39310,40410,41428]
rural_emp = [45971,45354,44708,41418,40506,39602,38737,37943,37041,36175]

width = 0.25
x = np.arange(len(years))

plt.bar(x-width, all_emp, width, color='red', label='全部就业')
plt.bar(x, town_emp, width, color='green', label='城镇就业')
plt.bar(x+width, rural_emp, width, color='blue', label='乡村就业')

for i,val in enumerate(all_emp):
    plt.text(i-width, val, f"{val:d}", ha='center', va='bottom', fontsize=8)
for i,val in enumerate(town_emp):
    plt.text(i, val, f"{val:d}", ha='center', va='bottom', fontsize=8)
for i,val in enumerate(rural_emp):
    plt.text(i+width, val, f"{val:d}", ha='center', va='bottom', fontsize=8)

plt.xlabel("年份")
plt.ylabel("人员")

plt.xticks(x, years)
plt.ylim(30000, 80000)

plt.suptitle("2007—2016年全部、城镇和乡村就业人员情况")
plt.title("单位：万人")

plt.figtext(0.7, 0.01, "数据来源：国家统计局")

plt.legend(loc="center")

plt.show()