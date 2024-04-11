import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Image_Q2.tif') # load img

threshold = 200 # suppose threshold is 200

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # grayscale conversion
_, binary_image = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY) # intensity level slicing

cv2.imshow('Original Image', image)
cv2.imshow('Binary Image (Brightest Part)', binary_image)

# plotting for rows
white_pixels_per_row = np.sum(binary_image == 255, axis=1)
plt.plot(white_pixels_per_row)
plt.xlabel('Row')
plt.ylabel('Number of White Pixels')
plt.title('Number of White Pixels in Each Row')
plt.show()

# plotting for columns
white_pixels_per_column = np.sum(binary_image == 255, axis=0)
plt.plot(white_pixels_per_column)
plt.xlabel('Column')
plt.ylabel('Number of White Pixels')
plt.title('Number of White Pixels in Each Column')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
