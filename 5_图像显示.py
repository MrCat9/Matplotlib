# -*- coding: utf-8 -*-
# 摘自 https://zhuanlan.zhihu.com/p/24309547

import matplotlib.pyplot as plt

# 读取一张图片并显示
plt.figure('test_img')
test_img = plt.imread('test_img.jpg')
plt.imshow(test_img)

# ---------------------------------------

# img1是img0做了个简单的变换
img0 = test_img
img1 = 3*test_img + 4

fig = plt.figure('img')

ax0 = fig.add_subplot(121)
ax0.set_title('img0')
plt.imshow(img0)

ax1 = fig.add_subplot(122)
ax1.set_title('img1')
plt.imshow(img1)

# ---------------------------------------

# cmap指定为'gray'用来显示灰度图
fig = plt.figure('Auto Normalized Visualization')

if img0.ndim == 3:
    img0 = img0[:,:,0]

ax0 = fig.add_subplot(131)
ax0.imshow(img0)

ax1 = fig.add_subplot(132)
ax1.imshow(img0, cmap='gray')

ax2 = fig.add_subplot(133)
ax2.imshow(img0, cmap='gray_r')

plt.show()
