# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:03:28 2020

@author: Piyush
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread("photo.jpg")
img_rgb1 = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
rowSize, columnSize, planes = img_rgb1.shape
img_luv = img_rgb1.copy(order = 'F')

for row in range(0, rowSize):
   for column in range(0, columnSize):
       img_luv[row, column, 0] = img_rgb1[row][column][0] + img_rgb1[row][column][1] + img_rgb1[row][column][2]
       img_luv[row, column, 1] = img_rgb1[row][column][1] + img_rgb1[row][column][2] - (2*img_rgb1[row][column][0])
       img_luv[row, column, 2] = img_rgb1[row][column][2] - img_rgb1[row][column][1]


plt.imshow(img_luv)


img_luv1 = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LUV)
plt.imshow(img_luv1)