import cv2 
import os 
import numpy as np


image = cv2.imread('image/cat.jpg')
height,width = image.shape[:2]

# Apply mask 
mask = np.zeros((height,width),dtype=np.uint8)
cv2.rectangle(mask,(100,100),(300,300),255,-1)

bitwise_and = cv2.bitwise_and(image,image,mask=mask)

cv2.imshow("Apply Mask Image",bitwise_and)

directory = 'LAB02-SAMSOKREAKSMEY/Image'
filename1 = 'Ex4_Bitwise_AND_Image_Apply_Mask.jpg'
file_path1 = os.path.join(directory, filename1)

cv2.imwrite(file_path1,image)
cv2.waitKey(0)
cv2.destroyAllWindows()

