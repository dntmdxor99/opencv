import cv2
import numpy as np
# import matplotlib.pyplot as plt

img = cv2.imread('picture/lena.jpg', 1)
img2 = np.zeros_like(img)
# hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# img = cv2.equalizeHist(img)

# plt.hist(img.ravel(), 256, [0, 256])
# img[:, :, 0] = img[:,:, 1] = img[:, :, 2] = (0.299 * img[:,:, 0] + 0.584 * img[:, :, 1] + 0.1148 * img[:, :, 2])
for i in range(3):
    img2[:, :, i] = (0.299 * img[:, :, 0] + 0.584 * img[:, :, 1] + 0.1148 * img[:, :, 2])

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()