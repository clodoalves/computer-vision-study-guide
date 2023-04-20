import cv2;

colorFulImage = cv2.imread("Content\Images\people1.jpg")

grayScaleImage = cv2.cvtColor(colorFulImage, cv2.COLOR_BGR2GRAY)

eyeDetector = cv2.CascadeClassifier("Content\Cascades\haarcascade_eye.xml")

detections = eyeDetector.detectMultiScale(grayScaleImage, scaleFactor = 1.09, minNeighbors = 10, maxSize=(70,70))

retangleColor = (255, 0, 0)

for xaxis, yaxis, width, height in detections:
    print(width, height)
    cv2.rectangle(colorFulImage, (xaxis, yaxis), (xaxis + width, yaxis + height), retangleColor, thickness= 2)

cv2.imshow("sample", colorFulImage)

cv2.waitKey(0)

