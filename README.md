[Download lesson 3](https://github.com/user-attachments/files/23432812/image.processing.pdf)

<img width="800" height="1200" alt="image" src="https://github.com/user-attachments/assets/ed33d570-0c61-4109-8ee2-4967cab25560" />

## Here’s the exact last class code! Ready to copy and paste into your Python editor (Visual Studio Code, or Jupyter Notebook).
```
import numpy as np
import cv2
from matplotlib import pyplot as plt
# Load image
# bob = cv2.imread("file name")
# img = cv2.imread("polar bear.png")
# You can replace "polar bear.png" with any image file name in your folder
spooky = cv2.imread("polar bear.png")

# Convert the image from BGR (OpenCV format) to RGB (for displaying with matplotlib)
gray = cv2.cvtColor(spooky, cv2.COLOR_BGR2GRAY)
blue_channel = spooky[:, :, 0]

# Define sharpening kernel
kernel = np.array([[0, -1, 1],
                   [0, 1, 0],
                   [1, -1, 1]])

print(spooky)
```
```spooky = cv2.imread("polar bear.png")```
This variable stores the image you loaded from your computer.
Variables = store information.

The image is saved as a NumPy array — a grid of numbers representing each pixel’s color (Blue, Green, Red).

Think of it like a spreadsheet full of color data for each pixel!

```rgb = cv2.cvtColor(spooky, cv2.COLOR_BGR2RGB)```
Converts the image from BGR (the format OpenCV uses) to RGB (the format matplotlib uses to display images). It helps show the image with correct colors when using plt.imshow().
```
kernel = np.array([[0, -1, 1],
                   [0, 1, 0],
                   [1, -1, 1]])
```
A matrix (small grid of numbers) that tells the computer how to change each pixel’s brightness. Used for image sharpening — it highlights edges and details. Each number in the kernel affects nearby pixels, kind of like giving instructions for how to “redraw” the image.

Define 

Reading:
1. https://setosa.io/ev/image-kernels/
2. https://www.geeksforgeeks.org/deep-learning/types-of-convolution-kernels/#1-identity-kernel
