import cv2
import numpy as np

img = cv2.imread('picture/lena.jpg', 1)
img2 = np.zeros_like(img)

for i in range(3):
    img2[:, :, i] = 0.299 * img[:, :, 0] + 0.584 * img[:, :, 1] + 0.1148 * img[:, :, 2]

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()