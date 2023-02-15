import numpy as np
import matplotlib.pyplot as plt
import cv2

"""
There were a lot of shenaigans to get cv2 imported. Make sure right clicking
on the 'import' menu and installing the full opencv2
"""

# Notice that this color is off because of the differences in Color Channel ordering
img = cv2.imread('../DATA/00-puppy.jpg')
# plt.imshow(img)
# plt.show()
# print(img.shape)

# Matplotlib --> RGB expected Red, Green, Blue; in that order
# OpenCV --> BGR expected Blue, Green, Red; in that order
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(fix_img)
# plt.show()

"""There are other cmap types, like 'magma' """
# img_gray = cv2.imread('../DATA/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
# plt.imshow(img_gray, cmap='gray')
# plt.show()
# notice this shape no longer has 3rd dimension
# print(img_gray.shape)

# Resize an image by dimension
# new_img = cv2.resize(fix_img,(1000,400))
# plt.imshow(new_img)
# plt.show()

# Resize an image by ratio
# w_ratio = .5
# h_ratio = .5
# new_img = cv2.resize(fix_img, (0,0), fix_img, w_ratio, h_ratio)
# plt.imshow(new_img)
# plt.show()

# flip along horizontal axis
# new_img = cv2.flip(fix_img, 0)
# plt.imshow(new_img)
# plt.show()

# flip along vertical axis
# new_img = cv2.flip(fix_img, 1)
# plt.imshow(new_img)
# plt.show()

# flip along both axis
# new_img = cv2.flip(fix_img, -1)
# plt.imshow(new_img)
# plt.show()

# write a new image
# cv2.imwrite('totally_new.jpg', new_img)

# creates a larger canvas to display image, as the image is scaled to fit the canvas anyways
# fig = plt.figure(figsize=(10,8))
# ax = fig.add_subplot(111)
# ax.imshow(fix_img)
# plt.show()