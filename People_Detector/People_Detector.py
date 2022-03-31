import cv2

#HOG Detection is an OpenCV moduel that has been
#Trained solely on Humans Standing upright
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#Initialise Webcam Stream
#0 can be replaced with a video file to run HOG on that file
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Cannot access webcam")

while video.isOpened():
    ret, frame = video.read()
    if ret:
        #scale image for faster framerate
        frame = cv2.resize(frame, None, fx=0.75, fy=0.75)
   
        #People Detection
        (regions, _) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(4, 4), scale=1.05)
   
        # Drawing the area where
        # person is detected and labling them
        for (x, y, w, h) in regions:
            cv2.rectangle(frame, (x, y),
                          (x + w, y + h), 
                          (0, 0, 255), 2)
            
            cv2.putText(frame, 'person', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
   
        # Showing the output Image
        cv2.imshow("Person Detector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()