# -*- coding: utf-8 -*-
# 摘自 https://zhuanlan.zhihu.com/p/24309547

import matplotlib.pyplot as plt
import numpy as np

# 3D图标必须的模块，project='3d'的定义
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)

n_grids = 51            # x-y平面的格点数 
c = n_grids / 2         # 中心位置
nf = 2                  # 低频成分的个数

# 生成格点
x = np.linspace(0, 1, n_grids)
y = np.linspace(0, 1, n_grids)

# x和y是长度为n_grids的array
# meshgrid会把x和y组合成n_grids*n_grids的array，X和Y对应位置就是所有格点的坐标
X, Y = np.meshgrid(x, y)

# 生成一个0值的傅里叶谱
spectrum = np.zeros((n_grids, n_grids), dtype=np.complex)

# 生成一段噪音，长度是(2*nf+1)**2//2
noise = [np.complex(x, y) for x, y in np.random.uniform(-1,1,((2*nf+1)**2//2, 2))]
# //表示整数除法，返回不大于结果的一个最大的整数
'''
print(np.random.uniform(-1,1,((2*nf+1)**2//2, 2)))
[[ 0.9662763   0.95846216]
 [-0.68845188 -0.61022464]
 [ 0.70945109 -0.13921098]
 [-0.81907828  0.07940303]
 [ 0.01832325  0.95498552]
 [-0.62557164  0.53283393]
 [ 0.20583798 -0.41104461]
 [-0.94045891  0.53707534]
 [ 0.31369726 -0.15973358]
 [-0.61492046 -0.44897398]
 [ 0.28009928  0.3280309 ]
 [-0.31891428 -0.52068987]]

print(noise)
# [(-0.250919762305275+0.9014286128198323j),···, (-0.4157107029295637-0.2672763134126166j)]
print(noise.__len__())      # 12
'''

# 傅里叶频谱的每一项和其共轭关于中心对称
noisy_block = np.concatenate((noise, [0j], np.conjugate(noise[::-1])))
# concatenate用于拼接矩阵        # conjugate返回共轭复数

# 将生成的频谱作为低频成分
spectrum[int(c-nf):int(c+nf+1), int(c-nf):int(c+nf+1)] = noisy_block.reshape((2*nf+1, 2*nf+1))

# 进行反傅里叶变换
Z = np.real(np.fft.ifft2(np.fft.ifftshift(spectrum)))

# 创建图表
fig = plt.figure('3D surface & wire')

# 第一个子图，surface图
ax = fig.add_subplot(1, 2, 1, projection='3d')

# alpha定义透明度，cmap是color map
# rstride和cstride是两个方向上的采样，越小越精细，lw是线宽
ax.plot_surface(X, Y, Z, alpha=0.7, cmap='jet', rstride=1, cstride=1, lw=0)

# 第二个子图，网线图
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3, lw=0.5)

plt.show()

