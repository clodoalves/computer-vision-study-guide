import cv2

tracker = cv2.TrackerKCF_create()
video = cv2.VideoCapture('content/Videos/race.mp4')

isOk, frame = video.read()
bbox = cv2.selectROI(frame)
ok = tracker.init(frame, bbox)

escASCIICode = 27

while not (cv2.waitKey(1) & 0XFF == escASCIICode) or isOk:
    isOk, frame = video.read()
    isOk, bbox = tracker.update(frame)
    
    if (isOk):
        xaxis, yaxis, width, length = bbox[0], bbox[1], bbox[2], bbox[3]
        cv2.rectangle(img=frame, pt1=(xaxis, yaxis), pt2=((xaxis + width, yaxis + length)), color=(255,0,0), thickness=1)
    else:
        cv2.putText(img=frame, text="ERROR", org=(100,80), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255))
        
    cv2.imshow('rastreamento', frame)