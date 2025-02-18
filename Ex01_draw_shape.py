import cv2

image = cv2.imread("C:/Users/User/Pictures/cat.jpg")

rec = cv2.rectangle(image, (125, 100) , (200, 170) , (255, 0, 0), thickness=2)

circ= cv2.circle(image,(160,135), 38, (0,0,255), thickness=2)

cv2.imshow("Image with Rectangle and circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
