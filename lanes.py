import cv2
import numpy as np 

image = cv2.imread('./Image/test_image.jpg')
lane_image = np.copy(image)

# Converting the image to gray
gray = cv2.cvtColor(lane_image, cv2.COLOR_BGR2GRAY)

# Converting image with the rbg
# cv2.imshow('result', image)

# Display image until you press any key of the keyboard 
cv2.imshow('result', gray)
cv2.waitKey(0)


