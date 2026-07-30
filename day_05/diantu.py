import matplotlib.pyplot as plt
import seaborn as sns
tips_data = sns.load_dataset("tips")
sns.pointplot(x="day", y="total_bill", data=tips_data)
plt.show()