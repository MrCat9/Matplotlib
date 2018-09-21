# -*- coding: utf-8 -*-
# 摘自 https://blog.csdn.net/chi_wawa/article/details/68062506

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure(figsize=plt.figaspect(0.5))  # figure的高度是宽度的0.5倍

# 子图1
ax = fig.add_subplot(121, projection="3d")
X = np.arange(-5, 5, 0.25)  # 生成的List的间隔为0.25
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
ax.set_zlim(-2, 2)
ax.zaxis.set_major_locator(LinearLocator(20))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.6, aspect=10)

# 子图2
ax = fig.add_subplot(122, projection="3d")
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_wireframe(X, Y, Z)


plt.show()