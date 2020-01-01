
import cv2, numpy as np
img = cv2.imread("../Samples/lena.png",1)

'''Generate Gaussian Noise'''
gaussian_noise = np.random.normal(255/2,10,img.shape) #mean, SD, shape to be generated

'''Reduce the brightness of the original image and convert back to uint8'''
img = img * 0.5
img=img.astype('uint8') #VVI to do this conversion else you will get all white pizels

'''Reduce the brightness of the noise and convert back to uint8'''
gaussian_noise = gaussian_noise * 0.5
gaussian_noise = gaussian_noise.astype('uint8')

'''Add the two'''
sample_img_with_gaussian_noise = img + gaussian_noise
cv2.imshow("sample",sample_img_with_gaussian_noise)
cv2.waitKey(3000)
cv2.destroyAllWindows()

'''Now remove the noise using Gaussian smoothing/ filter'''
gaussian_filtered_image = cv2.GaussianBlur(sample_img_with_gaussian_noise,(25,25),5)
cv2.imshow("sample",gaussian_filtered_image)
cv2.waitKey(5000)
cv2.destroyAllWindows()
