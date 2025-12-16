import cv2
import numpy as np

# Create a white test image
img = np.ones((300, 300, 3), dtype=np.uint8) * 255

# Draw colored circles (BGR format)
cv2.circle(img, (50, 150), 30, (0, 0, 255), -1)    # Red circle
cv2.circle(img, (125, 150), 30, (0, 255, 0), -1)  # Green circle
cv2.circle(img, (200, 150), 30, (255, 0, 0), -1)  # Blue circle

# Convert image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define green color range in HSV
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

# Create mask for green color
mask = cv2.inRange(hsv, lower_green, upper_green)

# Display results
cv2.imshow("Colored Circles", img)
cv2.imshow("Green Color Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
