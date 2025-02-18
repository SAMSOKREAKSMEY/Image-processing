import cv2

img1 = cv2.imread('image/cat.jpg')
img2 = cv2.imread('image/paris.jpg')

img2 = cv2.resize(img2, (img1.shape[0], img1.shape[1]))

alpha = 0.7  #when it hight img2 is blur    
beta = 0.3 #when it hight img1 is blur    
blended_image = cv2.addWeighted(img1, alpha, img2, beta, 0)

text = "Welcome home!"
position = (100, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 0, 255)
thickness = 2

putText = cv2.putText(blended_image, text, position, font, font_scale, color, thickness)

cv2.imshow("Blended Image", putText)
cv2.waitKey(0)
cv2.destroyAllWindows()
