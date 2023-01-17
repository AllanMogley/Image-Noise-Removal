import cv2
import os
print(os.getcwd())

# Load the image
img = cv2.imread(r"Me 2.png")
img = cv2.imread(r"noisy.jpeg")




# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a kernel for the morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Apply the morphological opening to the image
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

# Apply the morphological closing to the image
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

# Save the filtered image
cv2.imwrite("Filtered Image.jpg", closing)
