import cv2

colorfulImage = cv2.imread("content/Images/people3.jpg")

grayScaleImage = cv2.cvtColor(colorfulImage, cv2.COLOR_BGR2GRAY)

faceDetector = cv2.CascadeClassifier("content/Cascades/haarcascade_frontalface_default.xml")

detections = faceDetector.detectMultiScale(grayScaleImage, scaleFactor = 1.001, minNeighbors = 3)

retangleColor = (255, 0, 0)

for xaxis, yaxis, width, height in detections:
    cv2.rectangle(colorfulImage, (xaxis, yaxis), (xaxis + width, yaxis + height), retangleColor, thickness=1)
    print(width, height)

    
cv2.imshow("sample",colorfulImage)
cv2.waitKey(0)
cv2.destroyAllWindows()