import cv2
import numpy as np
img = cv2.imread('123.png')
img[img==255]=254
img2=img
for i in range(0,img2.shape[0]):
  for j in range(0,img2.shape[1]):
    color=img2[i,j]
    r=255*np.log(1+color[0])/np.log(256)
    g=255*np.log(1+color[1])/np.log(256)
    b=255*np.log(1+color[2])/np.log(256)
    img2[i,j]=(r,g,b)


cv2.imwrite('2.png',img2)