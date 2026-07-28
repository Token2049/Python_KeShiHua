import matplotlib.pyplot as plt
import seaborn as sns
tips_data = sns.load_dataset('tips',
data_home='seaborn-data')#绘制直方图
sns.displot(tips_data['total_bill'], bins=10)
plt.show()