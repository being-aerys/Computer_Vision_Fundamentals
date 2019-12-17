import cv2

def blend(path_to_image_1, path_to_image_2,alpha,beta):
    assert alpha + beta == 1
    image1 = cv2.imread(path_to_image_1)
    image_2  = cv2.imread(path_to_image_2)
    cropped_image1 = image1[0:320,0:500,:]
    cropped_image2 = image_2[0:320,0:500,:]

    blended_image = (cropped_image1 * 0.5).astype("uint8") + (cropped_image2*0.5).astype("uint8")
    return blended_image




blended_imagee = blend("../Samples/lena.png","../Samples/dolphin.png",0.1,0.9)
cv2.imshow("Display_Window",blended_imagee)
cv2.waitKey(5000)