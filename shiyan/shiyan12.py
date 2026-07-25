import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

years = np.array([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])
total = [2100, 2350, 2640, 2950, 3260, 3540, 3910, 4330, 4750, 5120]
urban = [1220, 1400, 1610, 1840, 2060, 2280, 2560, 2880, 3210, 3500]
rural = [880, 950, 1030, 1110, 1200, 1260, 1350, 1450, 1540, 1620]

plt.fill_between(years, total, color='red', edgecolor='black', linewidth=2, label='全国游客总人次')
plt.fill_between(years, urban, color='green', edgecolor='black', linewidth=2, label='城镇居民游客人次')
plt.fill_between(years, rural, color='blue', edgecolor='black', linewidth=2, label='农村居民游客人次')

plt.xlabel('年份')
plt.ylabel('游客人次')

plt.xticks(years)
plt.ylim(800, 6000)

plt.suptitle('2010—2019年全国、城镇和农村游客人次情况')
plt.title('单位：百万人次')

plt.figtext(0.7, 0.01, '数据来源：国家统计局')

plt.legend(loc='upper left')

plt.show()