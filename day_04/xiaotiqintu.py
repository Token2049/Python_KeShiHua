import seaborn as sns
import matplotlib.pyplot as plt
tips_data = sns.load_dataset('tips',
                             data_home='data')
sns.violinplot(x='day', y='total_bill', data=tips_data, cut=0,width = 0.5)
plt.show()