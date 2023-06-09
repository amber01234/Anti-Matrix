import cv2
face_cap=cv2.CascadeClassifier('C:/Users/11ars/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')  
eye_cap=cv2.CascadeClassifier('C:/Users/11ars/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_eye_tree_eyeglasses.xml')

video_cap=cv2.VideoCapture(0)
while True:
    ret,video=video_cap.read()
    col=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    faces=face_cap.detectMultiScale(
       col,
       scaleFactor=1.1,
       minNeighbors=5,
       minSize=(30,30),
       flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video,(x,y),(x+w,y+h),(255,0,0),2)
    eyes=eye_cap.detectMultiScale(
       col,
        scaleFactor = 1.2, 
        minNeighbors = 4
    )
    for (x,y,w,h) in eyes:
            cv2.rectangle(video,(x,y),(x+w,y+h),(0, 255, 0),3)
 

   
    cv2.imshow("video_live",video)
    if cv2.waitKey(10)==ord("a"):
     break
video_cap.release()
