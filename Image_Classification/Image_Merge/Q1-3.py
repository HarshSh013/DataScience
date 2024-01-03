import cv2 as cv
import numpy as np
# def adjust_brightness_contrast(image, alpha, beta):
#     adjusted_image = image.copy()
#
#     for y in range(adjusted_image.shape[0]):        #iterate through each pixel in the image Red
#         for x in range(adjusted_image.shape[1]):    #iterate through each pixel in the image Green
#             for c in range(adjusted_image.shape[2]):#iterate through each pixel in the image Blue
#                 adjusted_pixel_value = int(alpha * image[y, x, c] + beta)
#                 if adjusted_pixel_value < 0:        #pixel value should not decreased below 0
#                     adjusted_image[y, x, c] = 0
#                 elif adjusted_pixel_value > 255:    #pixel value should not exceed above 255
#                     adjusted_image[y, x, c] = 255
#                 else:
#                     adjusted_image[y, x, c] = adjusted_pixel_value
#
#     return adjusted_image

originalimage = cv.imread('sample.jpg')

alpha = 1.5 #contrast 1 is for no change
beta=50     #brightness 0 is for no change

adjustedimage = np.clip(alpha * originalimage + beta, 0, 255).astype(np.uint8)
grayscaleimage = cv.cvtColor(originalimage, cv.COLOR_BGR2GRAY)

cv.imshow('Original Image', originalimage)
cv.imshow('Adjusted Image', adjustedimage)
cv.imshow('Gray-Scale Image', grayscaleimage)


cv.waitKey(0)
cv.destroyAllWindows()