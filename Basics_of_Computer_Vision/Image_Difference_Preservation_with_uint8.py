import cv2
'''Can preserve the difference between images a and b by either using (a-b) + (b-a) or converting the images into floating point images before subtraction'''

def image_difference(image_a, image_b):
    return (image_a - image_b) + (image_b - image_a) #understand the meaning of this expression

if __name__ == "__main__":
    imaage1 = cv2.imread("../Samples/dolphin.png")
    imaage2 = cv2.imread("../Samples/dolphin.png")
    cv2.imshow("Image Difference",image_difference(imaage1,imaage2)) #should be an all-black image
    cv2.waitKey(5000)
