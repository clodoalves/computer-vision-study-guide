import cv2

colorFulImage = cv2.imread("content/Images/car.jpg")

grayScaleImage = cv2.cvtColor(colorFulImage, cv2.COLOR_BGR2GRAY)

detector = cv2.CascadeClassifier("content/Cascades/cars.xml")

carDetections = detector.detectMultiScale(grayScaleImage, scaleFactor = 1.052, minSize = (30, 30))

for xaxis, yaxis, width, height in carDetections:
    cv2.rectangle(img=colorFulImage, pt1=(xaxis, yaxis), pt2=(xaxis + width, yaxis + height), color=(0, 255, 0), thickness=2)
    print(xaxis, yaxis)
    
cv2.imshow("sample", colorFulImage)

cv2.waitKey(0)