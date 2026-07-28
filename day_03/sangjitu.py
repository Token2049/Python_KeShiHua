import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

# 设置中文显示
plt.rcParams["font.sans-serif"] = "SimHei"  
plt.rcParams["axes.unicode_minus"] = False  

# 1. 生成初始图形
sankey = Sankey()  

# 2. 添加流量
flows = [0.7, 0.3, -0.3, -0.1, -0.3, -0.1, -0.1, -0.1]  # 流量数据
labels = ["工资", "副业", "生活", "服饰", "学习", "健身", "其他", "理财"]  # 流量标签
orientations = [1, 0, -1, -1, 1, -1, 0, 1]  # 流量方向

sankey.add(flows=flows, 
           labels=labels, 
           orientations=orientations, 
           color="black", 
           fc="lightgreen", 
           patchlabel="生活消费")  

# 3. 完成图形绘制
diagrams = sankey.finish()  

# 将索引为4的标签设为红色
diagrams[0].texts[4].set_color("red")  

# 将中心标签的字体大小设为20号并加粗
diagrams[0].text.set_fontsize(20)  
diagrams[0].text.set_fontweight("bold")  

plt.title("日常生活收支的桑基图")  
plt.show()