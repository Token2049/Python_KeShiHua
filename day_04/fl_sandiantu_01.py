import seaborn as sns
import matplotlib.pyplot as plt
tips_data = sns.load_dataset('tips',
                             data_home='data')
sns.swarmplot(x='day', y='total_bill', data=tips_data, hue='day', 
              palette='deep',legend=False)
plt.show()