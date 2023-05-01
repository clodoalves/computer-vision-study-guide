import cv2

colorfulImage = cv2.imread("content/Images/people1.jpg")

colorfulImage = cv2.resize(colorfulImage, (800, 600))

grayScaleImage = cv2.cvtColor(colorfulImage, cv2.COLOR_BGR2GRAY)

faceDetector = cv2.CascadeClassifier("content/Cascades/haarcascade_frontalface_default.xml")

detections = faceDetector.detectMultiScale(grayScaleImage, scaleFactor = 1.09)

for xaxis, yaxis, heigth, width in detections:
    cv2.rectangle(img=colorfulImage, pt1=(xaxis, yaxis), pt2=(xaxis + width, yaxis + heigth), color=(0, 255, 255), thickness=2)

cv2.imshow("sample", colorfulImage)

cv2.waitKey(0)

cv2.destroyAllWindows()