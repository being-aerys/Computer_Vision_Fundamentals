
import cv2, numpy as np

sample_img = cv2.imread("../Samples/bicycle.png")

gaussian_noise = np.random.normal(100,20,sample_img.shape) #mean, SD, shape to be generated

sample_img_with_added_gaussian_noise = sample_img + gaussian_noise

cv2.imshow("Gaussian Noise",sample_img_with_added_gaussian_noise) #Everything will look like a white pixel but is correct.
cv2.waitKey(10000)