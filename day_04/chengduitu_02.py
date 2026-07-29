import seaborn as sns
import matplotlib.pyplot as plt
tips_data = sns.load_dataset('tips',data_home='data')
sns.pairplot(tips_data,hue='size',palette='deep',markers=['o','s','D','^','v','*'])
plt.show()