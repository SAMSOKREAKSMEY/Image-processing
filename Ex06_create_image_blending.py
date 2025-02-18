import cv2
import numpy as np
import time

# Read the images
image1 = cv2.imread('image/itc_logo.jpg')  # ITC campus image
image2 = cv2.imread('image/gic_logo.png')  # GIC department image

# Resize image2 to match image1 dimensions
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Blend the images using addWeighted
alpha = 0.9  # Weight of the first image
beta = 0.5  # Weight of the second image
blend_image = cv2.addWeighted(image1, alpha, image2, beta, 0)

# Create a loop to display the image with time and shapes
for _ in range(5): 
    current_time = time.strftime('%H:%M:%S') 

    # Copy the blended image 
    img_with_time = blend_image.copy()

    # Draw a rectangle and a circle 
    cv2.rectangle(img_with_time, (150, 30), (10, 70), (0, 255, 0), 2)  # Green rectangle
    cv2.circle(img_with_time, (50, 150), 40, (0, 255, 255), 2)  # Red circle
    
    # Add text 
    cv2.putText(img_with_time, "ITC campus", (70, 580), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(img_with_time, "letter G", (20, 535), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Add the current time to the image
    cv2.putText(img_with_time, "Time: " + current_time, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    
    cv2.imshow('Blended Image with Clock', img_with_time)
    
    # Wait for 1 second before updating the time
    cv2.waitKey(1000)
cv2.destroyAllWindows()
