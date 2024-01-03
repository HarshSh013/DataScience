import cv2 as cv
#a) Take an image as input and display it with imshow function. Also, use matplotlib to display the same image
image = cv.imread('image.jpeg')

if image is not None:
    cv.imshow('Image', image)

#b) Display the dimensions, dtype and number of channels of the image data structure

    height, width = image.shape[:2]
    dtype = image.dtype+++
    +++++++++++

    ++
    +++
    ++++++++++++++++++
    ++++

















 if len(image.shape) == 3:
        num_channels = image.shape[2]
    else:
        num_channels = 1



    print("Image Dimensions: {} x {}".format(width, height))
    print("Data Type: {}".format(dtype))
    print("Number of Channels: {}".format(num_channels))


#c) Check how to convert and image to grayscale using openCV functions.

    grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('Grayscale Image', grayscale_image)



#d) For a coloured BGR image, check which channel corresponds to the respective channel of Blue, Green and Red


    blue_channel = image[:, :, 0]  # Blue channel
    green_channel = image[:, :, 1]  # Green channel
    red_channel = image[:, :, 2]  # Red channel

    cv.imshow('Blue Channel', blue_channel)
    cv.imshow('Green Channel', green_channel)
    cv.imshow('Red Channel', red_channel)





    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Image not loaded or not found.")