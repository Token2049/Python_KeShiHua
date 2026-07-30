import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.sans-serif"] = "SimHei"  
plt.rcParams["axes.unicode_minus"] = False  

# 1.读取
app = pd.read_csv("googleplaystore.csv")

# 清洗脏数据
app = app[app["Price"] != "Everyone"]
# 价格转为数字格式
app["Price"] = app["Price"].str.replace("$", "", regex=False)
# 再转为数字
app["Price"] = pd.to_numeric(app["Price"])


# 任务1：所有App价格分布直方图
sns.histplot(app['Price'], bins=10)
plt.title("全部App价格分布直方图")
plt.xlabel("价格(美元)")
plt.ylabel("App数量")
plt.show()


# 任务2：筛选下载量最多的5大App分类
# 统计每个分类App数量，取数量前5的分类
top5 = app.groupby(['Category'])['App'].count().sort_values(ascending=False).head().index.tolist()
# 筛选出前5分类数据
app5 = app[app.Category.isin(top5)]
print("五大热门分类App预览：")
print(app5.head())

# 仅付费App，绘制各类别价格箱线图
plt.figure(figsize=(10,5))
sns.boxplot(x='Price', y='Category', data=app5[app['Type']=="Paid"])
plt.title("五大热门分类付费App价格分布")
plt.show()

# 任务3：不同分类下免费/付费App评分对比
plt.figure(figsize=(12,5))
# hue区分Free免费/Paid付费
sns.barplot(x='Category', y='Rating', hue='Type', data=app5)
plt.title("五大分类免费&付费App评分对比")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()