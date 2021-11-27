import cv2
import numpy as np
img = cv2.imread('123.png')
img[img == 255] = 254
img2 = img
r1 = int(input('r1 '))
r2 = int(input('r2 '))
s1 = int(input('s1 '))
s2 = int(input('s2 '))
for i in range(0, img2.shape[0]):
    for j in range(0, img2.shape[1]):
        color = img2[i, j]
        r = 0
        g = 0
        b = 0
        if color[0] < r1:
            r = s1 / r1 * color[0]
        if color[0] >= r1 and color[0] <= r2:
            r = (s2 - s1) / (r2 - r1) * (color[0] - r1) + s1
        if color[0] > r2:
            r = (255 - s2) / (255 - r2) * (color[0] - r2) + s2

        if color[1] < r1:
            g = s1 / r1 * color[1]
        if color[1] >= r1 and color[1] <= r2:
            g = (s2 - s1) / (r2 - r1) * (color[1] - r1) + s1
        if color[1] > r2:
            g = (255 - s2) / (255 - r2) * (color[1] - r2) + s2

        if color[2] < r1:
            b = s1 / r1 * color[2]
        if color[2] >= r1 and color[2] <= r2:
            b = (s2 - s1) / (r2 - r1) * (color[2] - r1) + s1
        if color[2] > r2:
            b = (255 - s2) / (255 - r2) * (color[2] - r2) + s2
        img2[i, j] = (r, g, b)

cv2.imwrite('4.png', img2)