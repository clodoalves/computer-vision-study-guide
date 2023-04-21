import cv2

colorFulImage = cv2.imread("content\Images\car.jpg")

grayScaleImage = cv2.cvtColor(colorFulImage, cv2.COLOR_BGR2GRAY)

detector = cv2.CascadeClassifier("Content\Cascades\cars.xml")

carDetections = detector.detectMultiScale(grayScaleImage, scaleFactor = 1.052, minSize = (30, 30))

retangleColor = (0, 255, 0)

for xaxis, yaxis, width, height in carDetections:
    cv2.rectangle(colorFulImage, (xaxis, yaxis), (xaxis + width, yaxis + height), color=retangleColor, thickness=2)
    print(xaxis, yaxis)
    
cv2.imshow("sample", colorFulImage)

cv2.waitKey(0)