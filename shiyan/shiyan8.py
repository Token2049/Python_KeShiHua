import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

years = np.array([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])
highway = [15020.81,16020.81,16306.54,15763.64,14825.17,13733.12,13049.57,12458.40,11760.74,11024.00]
railway = [8762.18,9612.29,9812.33,10595.62,11373.96,11960.49,12579.29,13456.92,14146.59,14706.64]
air = [4039.00,4536.27,5025.74,5652.40,6334.19,7282.55,8378.30,9513.00,10711.60,11705.30]
water = [71.50,74.50,77.40,78.70,83.80,73.10,72.00,75.90,80.30,82.60]

x = np.arange(len(years))
width = 0.6

plt.bar(x, highway, width, color='blue', label='公路')
plt.bar(x, railway, width, bottom=highway, color='red', label='铁路')
plt.bar(x, air, width, bottom=np.array(highway)+np.array(railway), color='yellow', label='民航')
plt.bar(x, water, width, bottom=np.array(highway)+np.array(railway)+np.array(air), color='black', label='水运')

for i in range(len(years)):
    plt.text(x[i], highway[i], f"{highway[i]:.2f}", ha='center', va='bottom', fontsize=7)
    plt.text(x[i], highway[i]+railway[i], f"{railway[i]:.2f}", ha='center', va='bottom', fontsize=7)
    plt.text(x[i], highway[i]+railway[i]+air[i], f"{air[i]:.2f}", ha='center', va='bottom', fontsize=7)
    plt.text(x[i], highway[i]+railway[i]+air[i]+water[i], f"{water[i]:.2f}", ha='center', va='bottom', fontsize=14)

plt.xlabel("年份")
plt.ylabel("旅客周转量")

plt.xticks(x, years)
plt.ylim(0, 41000)

plt.suptitle("2010—2019年我国各类运输方式旅客周转量")
plt.title("单位：亿人公里")

plt.figtext(0.7, 0.01, "数据来源：国家统计局")

plt.legend(loc="upper center", ncol=2)

plt.show()