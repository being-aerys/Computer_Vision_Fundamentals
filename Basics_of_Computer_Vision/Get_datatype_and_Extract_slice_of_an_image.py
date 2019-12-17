import cv2

'''------------------Data type----------------------'''
sample_image = cv2.imread("../Samples/lena.png",1)
sample_image_data_type = sample_image.dtype
print(sample_image_data_type) #returns uint8, means 8 bits, unsigned integers, i.e., from 0 to 255 only to represent intensity values

'''----------------Slice an image-------------------'''
cropped_image = sample_image[0:1000,0:50] #VVI to note that the first argument is the y axis, and also the easurement goes downwards foy y axis
cv2.imshow("Display_Window",cropped_image)
cv2.waitKey(5000)

'''-----------------Select only the red channel of an image----------------'''
red_channel = sample_image[:,:,0] #Channel 0 for RED, 1 for GREEN, 2 for BLUE
cv2.imshow("New_Window", red_channel)
cv2.waitKey(5000)
