import matplotlib.pyplot as plt
import seaborn as sns
tips_data = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips_data,
            errcolor="black", errwidth=2, capsize=0.05)
plt.show()