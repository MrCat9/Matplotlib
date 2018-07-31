# -*- coding: utf-8 -*-
# 摘自 https://blog.csdn.net/chi_wawa/article/details/68062506

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, projection="3d")
a = zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0])
for c, z in a:
    xs = np.arange(20)  # [0,20)之间的自然数,共20个
    ys = np.random.rand(20)  # 生成20个[0,1]之间的随机数
    cs = [c] * len(xs)  # 生成颜色列表
    ax.bar(xs, ys, z, zdir='x', color=cs, alpha=0.8)  # 以zdir='x'，指定z的方向为x轴，那么x轴取值为[30,20,10,0]
#   ax.bar(xs, ys, z, zdir='y', color=cs, alpha=0.8)
#   ax.bar(xs, ys, z, zdir='z', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Bar plot', size=25, weight='bold')
plt.show()