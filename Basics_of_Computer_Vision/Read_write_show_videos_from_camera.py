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
video_capture = cv2.VideoCapture("../Samples/Video_Sample.mp4")
#can retrieve several properties of the video capture using get() method
frame_width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH) #means  Capture property == Frame width
print("Frame Width = ", frame_width)



fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
#VIDEO Output to save in a file
video_output = cv2.VideoWriter("Filename_to_save.mp4", fourcc, 20.0, (720, 1280)) #VVI this dimension of the video source, either th camera or the video file must matchqq

#work on it only if it is open --> only if the path is correct
while video_capture.isOpened() == True:
    is_frame_available, frame = video_capture.read()
    #display the video
    if is_frame_available == True:
        #Save the frame
        video_output.write(frame)

        cv2.imshow("Video display_window", frame)
        pressed_key = cv2.waitKey(1)
        if pressed_key == ord("q"):
            break
    else:
        break

video_output.release()
video_captured.release()
video_capture.release()
cv2.destroyAllWindows()