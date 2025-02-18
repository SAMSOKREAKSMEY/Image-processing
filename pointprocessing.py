import cv2
from matplotlib import pyplot as plt
image_color = cv2.imread('image/cat.jpg')
image_gray = cv2.imread('image/cat.jpg', cv2.IMREAD_GRAYSCALE)

alpha =0.9
beta = 100

adjusted_image = cv2.convertScaleAbs(image_gray, alpha=alpha, beta=beta)

plt.figure(figsize=(10,5))

plt.subplot(2,3,1), plt.imshow(image_gray, cmap='gray'), plt.title('Original Grayscale')

plt.subplot(2,3,2), plt.imshow(adjusted_image, cmap='gray'), plt.title('Brightness and Contrast')
plt.subplot(2,3,3), plt.imshow(image_color, cmap=None), plt.title('color Image')
plt.show()

cv2.imshow('color', image_color)
cv2.imshow('gray', image_gray)
cv2.imshow('Edit brightness and contrast', adjusted_image)
cv2.waitkey(0)
cv2.destroyAllwindows()