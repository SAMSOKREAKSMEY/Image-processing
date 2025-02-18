import cv2
import numpy as np

img1 = cv2.imread('image/cat.jpg')
img2 = cv2.imread('image/Paris.jpg')

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

add_image = cv2.add(img2, img1)
wrapped_addition = img1 + img2

subtracted_image = cv2.subtract(img1, img2)
wrapped_subtraction = img1 - img2

cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.imshow(' Added Image', add_image)
cv2.imshow(' Wrapped Added Image', wrapped_addition)
cv2.imshow('Subtracted Image', subtracted_image)
cv2.imshow('Wrapped Subtracted Image', wrapped_subtraction)
cv2.waitKey(0)
cv2.destroyAllWindows()

