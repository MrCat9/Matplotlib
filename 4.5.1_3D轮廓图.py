# -*- coding: utf-8 -*-
# 摘自 https://blog.csdn.net/chi_wawa/article/details/68062506

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)       #测试数据
#cset = ax.contour(X, Y, Z, cmap=cm.coolwarm)  #color map选用的是coolwarm
cset = ax.contour(X, Y, Z,extend3d=True, cmap=cm.coolwarm)
ax.set_title("Contour plot", color='b', weight='bold', size=25)
plt.show()
