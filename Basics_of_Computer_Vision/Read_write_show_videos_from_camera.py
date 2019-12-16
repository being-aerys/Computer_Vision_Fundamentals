import cv2


'''-------------------------------------------directly capture from your device camera------------------------------------'''
video_captured = cv2.VideoCapture(0) #sometimes by default its -1 instead of 0 for the primary camera

#run the while loop so that the camera will continuously capture
while True:
    is_frame_available, frame = video_captured.read()

    #display the captured video as you are capturing it
    cv2.imshow("Video Window", frame)

    pressed_key = cv2.waitKey(1)
    #break if the key "q" is pressed
    if pressed_key == ord("q"):
        break

#run the while loop so that the camera will continuously capture
while True:
    is_frame_available, frame = video_captured.read()

    grayscale_video_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #display the captured video as you are capturing it
    cv2.imshow("Video Window", grayscale_video_frame)

    pressed_key = cv2.waitKey(1)
    #break if the key "q" is pressed
    if pressed_key == ord("q"):
        break


'''---------------------------------------read from a video file--------------------------------------------------'''
video = cv2.VideoCapture("../Samples/Video_Sample.mp4")
#work on it only if it is open --> only if the path is correct

while video.isOpened() == True:
    is_frame_available, frame = video.read()
    #display the video
    cv2.imshow("Video display_window", frame)
    pressed_key = cv2.waitKey(1)
    if pressed_key == ord("q"):
        break
