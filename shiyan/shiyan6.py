import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
mileage = [9.10, 9.32, 9.76, 10.31, 11.18, 12.10, 12.40, 12.70, 13.17, 13.99]

plt.bar(years, mileage, label="营业里程")

for x, y in zip(years, mileage):
    plt.text(x, y, f"{y:.2f}", ha="center", va="bottom")

plt.xlabel("年份")
plt.ylabel("铁路营业里程")

plt.xlim(2009.5, 2019.5)
plt.ylim(0, 15)
plt.xticks(years)

plt.suptitle("2010—2019年我国铁路营业里程")

plt.title("单位：万公里")

plt.figtext(0.5, 0.01, "数据来源：国家统计局", ha="center")

plt.legend()

plt.show()