import cv2
import numpy as np
img = cv2.imread('123.png')
img[img==255]=254
img2=img
y=int(input())
for i in range(0,img2.shape[0]):
  for j in range(0,img2.shape[1]):
    color=img2[i,j]
    r=color[0]**y/255**(y-1)
    g=color[1]**y/255**(y-1)
    b=color[2]**y/255**(y-1)
    img2[i,j]=(r,g,b)


cv2.imwrite('3.png',img2)