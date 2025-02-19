import cv2
import matplotlib.pyplot as plt

image = cv2.imread('asset/champei.jpg', cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread('asset/champei.jpg')

#sobel Edge Detection 
x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_edge = cv2.magnitude(x, y)

# Laplacian edge detection
laplacian_edge = cv2.Laplacian(image, cv2.CV_64F) 

# Canny edge detection
canny_edge = cv2.Canny(image, 100,200)

#Display the image
plt.figure(figsize=(10, 10))

plt.subplot(3, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Gray Image')
plt.subplot(3, 2, 2), plt.imshow(sobel_edge, cmap='gray'), plt.title('Sobel Edge Detection')
plt.subplot(3, 2, 3), plt.imshow(laplacian_edge, cmap='gray'), plt.title('Laplacian Edge')
plt.subplot(3, 2, 4), plt.imshow(canny_edge, cmap='gray'), plt.title('Canny_Edge')
plt.subplot(3, 2, 5), plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB)), plt.title('Color Image')
plt.tight_layout()
plt.show()