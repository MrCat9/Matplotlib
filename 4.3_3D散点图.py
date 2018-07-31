# -*- coding: utf-8 -*-
# 摘自 https://blog.csdn.net/chi_wawa/article/details/68062506

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

label_font = {
    'color': 'c',
    'size': 15,
    'weight': 'bold'
}

def randrange(n, vmin, vmax):
    r = np.random.rand(n)  # 随机生成n个介于0~1之间的数
    return (vmax - vmin) * r + vmin  # 得到n个[vmin,vmax]之间的随机数

fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, projection="3d")  # 添加子坐标轴，111表示1行1列的第一个子图
n = 200
for zlow, zhigh, c, m, l in [(4, 15, 'r', 'o', 'positive'),
                             (13, 40, 'g', '*', 'negative')]:  # 用两个tuple，是为了将形状和颜色区别开来
    x = randrange(n, 15, 40)
    y = randrange(n, -5, 25)
    z = randrange(n, zlow, zhigh)
    ax.scatter(x, y, z, c=c, marker=m, label=l, s=z * 10) #这里marker的尺寸和z的大小成正比

ax.set_xlabel("X axis", fontdict=label_font)
ax.set_ylabel("Y axis", fontdict=label_font)
ax.set_zlabel("Z axis", fontdict=label_font)
ax.set_title("Scatter plot", alpha=0.6, color="b", size=25, weight='bold', backgroundcolor="y")   #子图的title
ax.legend(loc="upper left")    #legend的位置左上    # fontweight设置字体粗细，可选参数 [‘light’, ‘normal’, ‘medium’, ‘semibold’, ‘bold’, ‘heavy’, ‘black’] 

plt.show()
