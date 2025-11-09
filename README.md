[image processing.pdf](https://github.com/user-attachments/files/23432812/image.processing.pdf)
Copy and paste last class code 
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load image
# bob = cv2.imread("file name")
# img = cv2.imread("polar bear.png")
# You can replace "polar bear.png" with any image file name in your folder
spooky = cv2.imread("polar bear.png")
# Convert the image from BGR (OpenCV format) to RGB (for displaying with matplotlib)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blue_channel = img[:, :, 0]
# Define sharpening kernel
kernel = np.array([[0, -1, 1],
                   [0, 1, 0],
                   [1, -1, 1]])
            
print(spooky)

