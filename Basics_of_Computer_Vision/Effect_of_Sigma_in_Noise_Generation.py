
import cv2, numpy as np, time

saturn = cv2.imread("../Samples/Saturn.jpg")

#Just add a gaussian noise centered around 0 and an SD of 1, will not make much effect
gaus_noise = np.random.normal(0,1,saturn.shape)

saturn_1 = saturn + gaus_noise
cv2.imshow("New saturn",saturn_1)
cv2.waitKey(5000)

cv2.destroyAllWindows()