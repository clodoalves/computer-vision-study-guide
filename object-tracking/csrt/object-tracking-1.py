import cv2

tracker = cv2.TrackerCSRT_create()
video = cv2.VideoCapture('Content/Videos/race.mp4')

isOk, frame = video.read()
bbox = cv2.selectROI(frame)
ok = tracker.init(frame, bbox)

while not (cv2.waitKey(1) & 0XFF == 27) or isOk:
    isOk, frame = video.read()
    isOk, bbox = tracker.update(frame)
    
    if (isOk):
        xaxis, yaxis, width, length = bbox[0], bbox[1], bbox[2], bbox[3]
        cv2.rectangle(frame, (xaxis, yaxis), ((xaxis + width, yaxis + length)), color = (255,0,0), thickness = 1)
    else:
        cv2.putText(frame, "ERROR", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        
    cv2.imshow('rastreamento', frame)