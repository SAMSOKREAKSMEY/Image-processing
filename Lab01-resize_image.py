import cv2

# Read the image
image = cv2.imread("your pictures")
if image is None:
    print("Failed to load image.")
else:
    print("Image loaded successfully.")

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Save the grayscale image
    cv2.imwrite("C:/Users/User/Pictures/Saved Pictures/Paris_gray.jpg", gray_image)
    print("Grayscale image saved successfully as Paris_gray.jpg")

    # Resize the original image
    new_width = 200
    new_height = 300
    resized_image = cv2.resize(image, (new_width, new_height))

    # Display the original, grayscale, and resized images
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.imshow('Resized Image', resized_image)
    
    # Wait for a key press to close the images
    cv2.waitKey(0)
    cv2.destroyAllWindows()
