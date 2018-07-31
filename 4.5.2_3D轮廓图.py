# -*- coding: utf-8 -*-
# 摘自 https://blog.csdn.net/chi_wawa/article/details/68062506

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure(figsize=(16, 12))
ax = fig.gca(projection="3d")  # get current axis
X, Y, Z = axes3d.get_test_data(0.05)  #测试数据

ax.plot_surface(X, Y, Z, rstride=3, cstride=3, alpha=0.3)
cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir="x", offset=-40, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir="y", offset=40, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)
ax.set_title('Contour plot', alpha=0.5, color='g', weight='bold', size=30)

plt.show()
