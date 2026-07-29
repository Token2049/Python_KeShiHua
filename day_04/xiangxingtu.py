import seaborn as sns
import matplotlib.pyplot as plt
tips_data = sns.load_dataset('tips', data_home='data')
sns.boxplot(x='day', y='total_bill', data=tips_data, width = 0.6,
            flierprops=dict(marker='o', markerfacecolor='red', markersize=1))  
plt.show()