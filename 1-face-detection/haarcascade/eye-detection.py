import cv2;

colorFulImage = cv2.imread("content/Images/people1.jpg")

grayScaleImage = cv2.cvtColor(colorFulImage, cv2.COLOR_BGR2GRAY)

eyeDetector = cv2.CascadeClassifier("content/Cascades/haarcascade_eye.xml")

detections = eyeDetector.detectMultiScale(grayScaleImage, scaleFactor = 1.09, minNeighbors = 10, maxSize=(70,70))

for xaxis, yaxis, width, height in detections:
    print(width, height)
    cv2.rectangle(img=colorFulImage, pt1=(xaxis, yaxis), pt2=(xaxis + width, yaxis + height), color=(255, 0, 0), thickness=2)

cv2.imshow("sample", colorFulImage)

cv2.waitKey(0)
