# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 20:09
# @Author  : lance
# @File    : circles.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:15:39 2017

@author: tina
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('E:/jianguocloud/learn/Python/pythonTest/pythonUtils/datas/img/6.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.imread('E:/jianguocloud/learn/Python/pythonTest/pythonUtils/datas/img/1.jpg',0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
print(hist)

# plt.hist(img.ravel(),256,[0,256])
# plt.show()



# 设置画布参数
plt.subplot(121), plt.imshow(gray, 'gray')
plt.xticks([]), plt.yticks([])
plt.show()

'''
dp，用来检测圆心的累加器图像的分辨率于输入图像之比的倒数，且此参数允许创建一个比输入图像分辨率低的累加器。上述文字不好理解的话，来看例子吧。例如，如果dp= 1时，累加器和输入图像具有相同的分辨率。如果dp=2，累加器便有输入图像一半那么大的宽度和高度。
minDist，为霍夫变换检测到的圆的圆心之间的最小距离，即让我们的算法能明显区分的两个不同圆之间的最小距离。这个参数如果太小的话，多个相邻的圆可能被错误地检测成了一个重合的圆。反之，这个参数设置太大的话，某些圆就不能被检测出来了。
param1，有默认值100。它是method设置的检测方法的对应的参数。对当前唯一的方法霍夫梯度法，它表示传递给canny边缘检测算子的高阈值，而低阈值为高阈值的一半。
param2，也有默认值100。它是method设置的检测方法的对应的参数。对当前唯一的方法霍夫梯度法，它表示在检测阶段圆心的累加器阈值。它越小的话，就可以检测到更多根本不存在的圆，而它越大的话，能通过检测的圆就更加接近完美的圆形了。
minRadius，默认值0，表示圆半径的最小值。
maxRadius，也有默认值0，表示圆半径的最大值。
'''

circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,220, param1=35, param2=34, minRadius=80, maxRadius=100)
circles = circles1[0, :, :]
circles = np.uint16(np.around(circles))
print(circles)
for i in circles[:]:
    print("圆心坐标", i[0], i[1])
    # 画圆
    cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 5)
    # 画点
    cv2.circle(img, (i[0], i[1]), 2, (255, 0, 255), 10)
    # 画矩形
    cv2.rectangle(img, (i[0] - i[2], i[1] + i[2]), (i[0] + i[2], i[1] - i[2]), (255, 255, 0), 5)


# 设置画布参数
plt.subplot(122), plt.imshow(img)
plt.xticks([]), plt.yticks([])


#plt.show()