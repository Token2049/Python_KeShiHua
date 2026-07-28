import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
arr_2d = np.round(np.random.rand(10,10),1)
heatmap = plt.imshow(arr_2d,cmap='hot_r')
cbar = plt.colorbar(heatmap)
plt.title('热力图')

labels = ['a','b','c','d','e','f','g','h','i','j']
plt.xticks(np.arange(len(labels)),labels=labels)
plt.yticks(np.arange(len(labels)),labels=labels)

for i in range(len(labels)):
    for j in range(len(labels)):
        text = plt.text(j,i,arr_2d[i,j],
                        ha = 'center', va = 'center', color = 'green')
plt.show()