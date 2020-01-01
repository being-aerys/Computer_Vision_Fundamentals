import cv2

#read an image
lena_image = cv2.imread("../Samples/lena.png", 1) #what does 1 mean? IT IS A FLAG, 1 means in BGR format, if 0, then loads a grayscale version
#print(lena_image.shape)

#render an image from its matrix form
cv2.imshow("Image_Window", lena_image)

#will keep the image window for 1 second = 1000 milliseconds, put 0 as argument to keep the window as long as you want
cv2.waitKey(1000)

#destroy the window after displaying
cv2.destroyAllWindows()

#write an image matrix to an image file
cv2.imwrite("../Samples/lenna.png", lena_image)

#get a specific channel from the image matrix
only_green_of_rgb = lena_image[:,:,2]
#print(only_green_of_rgb.shape) #returns (512, 512)
cv2.imshow("New_Image_Window",only_green_of_rgb)
cv2.waitKey(0)