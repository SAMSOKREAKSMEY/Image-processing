import cv2
import numpy as np

image = cv2.imread('image/cat.jpg')
height, width = image.shape[:2]

mask = np.zeros((height, width), dtype =np.uint8)
cv2.rectangle(mask, (100,100), (300,300), 255, -1)

bitwise_and = cv2.bitwise_and(image, image, mask=mask)
bitwise_or = cv2.bitwise_or(image, image, mask=mask)
bitwise_xor = cv2.bitwise_xor(image, image, mask=mask)
bitwise_not = cv2.bitwise_not(image, mask=mask)

cv2.imshow("Original Image", image)
cv2.imshow("bitwise AND", bitwise_and)
cv2.imshow("bitwise OR", bitwise_or)
cv2.imshow("bitwise XOR", bitwise_xor)
cv2.imshow("bitwise NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()


