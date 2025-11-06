import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load image
img = cv2.imread("polar bear.png")

# Convert from BGR (OpenCV) to RGB (for matplotlib)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blue_channel = img[:, :, 0]
# Define sharpening kernel
kernel = np.array([[0, -1, 1],
                   [0, 1, 0],
                   [1, -1, 1]])
print(img)
print("Image shape:", img.shape)
print("Image size:", img.size)
result_gray = cv2.filter2D(gray, -1, kernel)
result = cv2.filter2D(blue_channel, -1, kernel)
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.title("Original Blue Channel")
plt.imshow(blue_channel, cmap='gray')
plt.axis("off")

plt.subplot(2, 2, 2)
plt.title("After Kernel on Blue Channel")
plt.imshow(result, cmap='gray')
plt.axis("off")

plt.subplot(2, 2, 3)
plt.title("Original Grayscale")
plt.imshow(gray, cmap='gray')
plt.axis("off")

plt.subplot(2, 2, 4)
plt.title("After Kernel on Grayscale")
plt.imshow(result_gray, cmap='gray')
plt.axis("off")

plt.show()
