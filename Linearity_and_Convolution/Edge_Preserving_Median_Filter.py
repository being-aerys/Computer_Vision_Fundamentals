#Median filter is a non-linear filter and is edge-preserving. Watch video 19 on udacity's Linearity and Convolution Chapter
#We will apply ssalt and pepper noise and check the difference between mean filter and median filter
import cv2
img = cv2.imread("../Samples/banana-with-salt-and-pepper-noise.jpg",1)

'''Display the original image first'''
cv2.imshow("Original_Image",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

'''Median Filter'''
img_with_median_filter = cv2.medianBlur(img,5)
cv2.imshow("Median-Filtered_Image",img_with_median_filter)
cv2.waitKey(3000)
cv2.destroyAllWindows()

'''Implement Mean filter later'''

