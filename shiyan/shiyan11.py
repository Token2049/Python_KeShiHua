import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

sales = np.linspace(2, 28, 40)
tv_input = 9.0 * sales + np.random.randn(40) * 7
radio_input = 4.6 * sales + np.random.randn(40) * 6
news_input = 3.2 * sales + np.random.randn(40) * 7

size_tv = tv_input / sales * 8
size_radio = radio_input / sales * 8
size_news = news_input / sales * 8

plt.scatter(sales, tv_input, s=size_tv, color='red', label='TV')
plt.scatter(sales, radio_input, s=size_radio, color='green', label='radio')
plt.scatter(sales, news_input, s=size_news, color='blue', label='newspaper')

plt.xlabel('销售额')
plt.ylabel('广告投入')

plt.xlim(0, 30)
plt.ylim(0, 300)

plt.suptitle('广告投入、销售额及投入产出比的关系')
plt.title('单位：万元')

plt.legend(loc='best')

plt.show()