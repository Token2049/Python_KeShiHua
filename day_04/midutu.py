import seaborn as sns
import matplotlib.pyplot as plt
tips_data = sns.load_dataset('tips',data_home='data')
sns.jointplot(x='total_bill', y='tip', data=tips_data, kind='kde',fill=True)
plt.show()