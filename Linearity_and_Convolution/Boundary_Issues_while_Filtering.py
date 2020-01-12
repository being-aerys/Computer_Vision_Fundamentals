#While using a filter, there is this issue of how you want to align the filter with the image
#Different alignments give different output image size as in Udacity's tutorial's Linearity and Concolution's Video 12
#Most of the time we replicate the image beyond its current position and then align the filter such that the output size is the same as the input image

import cv2

img = cv2.imread("../Samples/flower.jpg")


# '''Reduce the brightness of the original image and convert back to uint8'''
# img = img * 0.5
# img=img.astype('uint8') #VVI to do this conversion else you will get all white pizels

#Apply a gaussian filter
gaussian_filtered_image = cv2.GaussianBlur(img,(31,31),5,cv2.BORDER_REPLICATE) #5 is Gaussian kernel standard deviation for both X and Y directions
                                                                                #cant see much effect of the border type used
cv2.imshow("Gaussian_Filtered_Image",gaussian_filtered_image)
cv2.waitKey(5000)
cv2.destroyAllWindows()