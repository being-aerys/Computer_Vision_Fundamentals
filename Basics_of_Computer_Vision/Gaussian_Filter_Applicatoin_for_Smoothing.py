import cv2
sample_img = cv2.imread("../Samples/lenna.png",1)

#Apply a gaussian filter
gaussian_filtered_image = cv2.GaussianBlur(sample_img,(31,31),5)
cv2.imshow("Gaussian_Filtered_Image",gaussian_filtered_image)
cv2.waitKey(5000)
cv2.destroyAllWindows()