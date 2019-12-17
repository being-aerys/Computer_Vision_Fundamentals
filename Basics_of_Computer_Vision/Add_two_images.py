import cv2, time
dolphin_image = cv2.imread("../Samples/dolphin.png")
bicycle_image = cv2.imread("../Samples/bicycle.png")

'''-----------------------------Make sure the images to be added are of the same dimension----------------------------'''
print("Dolphin Image dimensions are ",dolphin_image.shape) #908, 1224, 3
print("Bicycle image dimensions are ",bicycle_image.shape) #320, 500, 3

#Get the same size to do arithmetic operations of the matrices
cropped_dolphin_image = dolphin_image[0:320,0:500,:]


'''----------------------------Incorrect way---It doubles the brightness----------------------------------'''
added_image = cropped_dolphin_image + bicycle_image
cv2.imshow("First_window", added_image)
cv2.waitKey(5000)


'''------------------------------Incorrect way -- First sum,  then truncate--> results in more number of white pixels------------------------'''
summed = cropped_dolphin_image + bicycle_image
averaged = summed * 0.5
averaged = averaged.astype('uint8')#VVI to do this conversion else you will get all white pizels
cv2.imshow("Third_window", averaged)
cv2.waitKey(5000)

'''-----------------------------Correct way---It truncates the value of all the x,y coordinates before summing, results in less number of whiter pixels'''
brightness_halved_dolphin = cropped_dolphin_image * 0.5
brightness_halved_dolphin=brightness_halved_dolphin.astype('uint8') #VVI to do this conversion else you will get all white pizels
brightness_halved_cycle = bicycle_image* 0.5
brightness_halved_cycle = brightness_halved_cycle.astype('uint8')#VVI to do this conversion else you will get all white pizels
summed_image = brightness_halved_cycle + brightness_halved_dolphin
cv2.imshow("Second window", summed_image)
cv2.waitKey(5000)
