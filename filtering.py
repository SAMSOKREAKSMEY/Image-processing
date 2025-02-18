import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('image/Paris.jpg')

#Apply Filter
mean_filtered = cv2.blur(image,(20,20))
median_filtered = cv2.medianBlur(image,5)
gaussian_filtered = cv2.GaussianBlur(image, (5,5), 0)

#Apply Sharpening using kernel
kernel_sharpening = np.array([[-1,-1,-1],
                                   [-1,9,-1],
                                   [-1,-1,-1]])
sharpened_image = cv2.filter2D(image, -1, kernel_sharpening)

#Display all filtered images
plt.figure(figsize=(12,8))
plt.subplot(2,2,1), plt.imshow(mean_filtered, cmap='gray'),plt.title('Mean filter')
plt.subplot(2,2,2), plt.imshow(median_filtered, cmap='gray'),plt.title('Median Filter')
plt.subplot(2,2,3), plt.imshow(gaussian_filtered, cmap='gray'),plt.title('Gaussian filter')
plt.subplot(2,2,4), plt.imshow(sharpened_image, cmap='gray'),plt.title('Sharpened filter')

plt.show()



           