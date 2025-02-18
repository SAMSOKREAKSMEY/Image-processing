import cv2

image = cv2.imread("image/paris.jpg")
image = cv2.resize(image,(image.shape[1]-500, image.shape[0]-500))
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Apply histogram equalization using function equalizeHist 
equalized_image = cv2.equalizeHist(image_gray)

#Display the results
cv2.imshow("Image original",image)
cv2.imshow("Graysccale", image_gray)
cv2.imshow("Equalized image", equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()