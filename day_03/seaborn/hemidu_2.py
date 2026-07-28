import matplotlib.pyplot as plt
import seaborn as sns
tips_data =sns.load_dataset('tips',data_home='seaborn-data') #进绘制核度图
sns.displot(tips_data['total_bill'],kind='kde',rug='True')
plt.show()