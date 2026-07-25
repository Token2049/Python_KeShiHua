import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

sales = np.linspace(2, 28, 50)
TV = 9.2 * sales + np.random.randn(50) * 8
radio = 4.5 * sales + np.random.randn(50) * 6
newspaper = 3.1 * sales + np.random.randn(50) * 7

plt.scatter(sales, TV, color='red', marker='o', label='TV')
plt.scatter(sales, radio, color='green', marker='x', label='radio')
plt.scatter(sales, newspaper, color='blue', marker='v', label='newspaper')

plt.xlabel('销售额')
plt.ylabel('广告投入')

plt.xlim(0, 30)
plt.ylim(0, 300)

plt.suptitle('广告投入与销售额之间的关系')
plt.title('单位：万元')

plt.legend(loc='best')

plt.show()