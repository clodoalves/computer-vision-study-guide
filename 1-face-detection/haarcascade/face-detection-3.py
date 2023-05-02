import cv2

colorFulImage = cv2.imread("content/Images/people3.jpg")

grayScaleImage = cv2.cvtColor(colorFulImage, cv2.COLOR_BGR2GRAY)

faceDetector = cv2.CascadeClassifier("content/Cascades/haarcascade_frontalface_default.xml")

detections = faceDetector.detectMultiScale(grayScaleImage, scaleFactor = 1.001, minNeighbors = 3)

for xaxis, yaxis, width, height in detections:
    cv2.rectangle(img=colorFulImage, pt1=(xaxis, yaxis), pt2=(xaxis + width, yaxis + height), color=(255, 0, 0), thickness=2)

cv2.imshow("sample",colorFulImage)
cv2.waitKey(0)
cv2.destroyAllWindows()