
import cv2

sample_img_path = "../Samples/lena.png"
sample_img = cv2.imread(sample_img_path,1)

'''Draw something on top of this image and display the result'''
sample_img = cv2.line(sample_img,(0,0),(255,255),(100,0,100),3)
sample_img = cv2.arrowedLine(sample_img,(300,300),(500,500),(255,0,0),3)
sample_img = cv2.rectangle(sample_img, (200,200),(400,500), (0,255,0),2)
sample_img = cv2.rectangle(sample_img, (300,200),(400,500), (0,255,0),-1) #-1 fills the rectangle with the color provided
sample_img = cv2.circle(sample_img, (100,100),100,(255,255,0),3)
sample_font = cv2.FONT_HERSHEY_DUPLEX
sample_img = cv2.putText(sample_img,"HELLO OPENCV2",(100,100),sample_font,4,(0,255,255),cv2.LINE_AA)
cv2.imshow("Lena image",sample_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()