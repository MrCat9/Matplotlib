# -*- coding: utf-8 -*-
# 摘自 https://blog.csdn.net/chi_wawa/article/details/68062506

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(16, 12))
ax = fig.gca(projection="3d")

# 在x轴和y轴画sin函数
x = np.linspace(0, 1, 100)
y = np.sin(2 * np.pi * x) + 1  # 2*π*x∈[0,2π] y属于[0,2]
ax.plot(x, y, zs=0, zdir='z', label="sin curve in (x,y)")

colors = ('r', 'g', 'b', 'k')
x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.append([c] * 20)  # 比如，[colors[0]*5]的结果是['r','r','r','r','r']，是个list
colors_list = []
for c1 in c_list:
    for c2 in c1:
        colors_list.append(c2)

for n in range(colors_list.__len__()):
    ax.scatter(x[n], y[n], zs=0, zdir='y', c=colors_list[n], label="scatter points in (x,z)")

ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 2)
ax.set_zlim(0, 1)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.view_init(elev=20, azim=25)  # 调整坐标轴的显示角度

plt.show()