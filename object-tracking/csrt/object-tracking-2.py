import cv2

video = cv2.VideoCapture("Content/Videos/street.mp4")
tracker = cv2.TrackerCSRT_create()

isOk, frame = video.read()
bbox = cv2.selectROI(frame)
tracker.init(frame, bbox)

while(not(cv2.waitKey(1) & 0XFF == 27) and isOk):
    isOk, frame = video.read()    
    isOk, bbox = tracker.update(frame)
    
    if (isOk):
        xaxis, yaxis, width, heigth = bbox[0], bbox[1], bbox[2], bbox[3]
        cv2.rectangle(frame, (xaxis, yaxis), (xaxis + width, yaxis + heigth), color = (0, 255, 0), thickness=1)
    else:
        cv2.putText(frame, "ERROR", org=(155,100), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale= 1, color = (0, 0, 255))
        
    cv2.imshow("Sample", frame)
        