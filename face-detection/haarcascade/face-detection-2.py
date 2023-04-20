import cv2;

colorfulImage = cv2.imread("Content\Images\people2.jpg")

grayScaleImage = cv2.cvtColor(colorfulImage, cv2.COLOR_BGR2GRAY)

faceDetector = cv2.CascadeClassifier("content\Cascades\haarcascade_frontalface_default.xml")

detections = faceDetector.detectMultiScale(grayScaleImage, scaleFactor = 1.2, minNeighbors = 3, 
                                           minSize=(32,32), maxSize=(100,100))

rectangleColor = (255, 0, 0)

for axisx, axisy, width, height in detections:
    cv2.rectangle(colorfulImage ,(axisx, axisy), (axisx + width, axisy + height), rectangleColor, thickness = 2)
    
cv2.imshow("sample", colorfulImage)

cv2.waitKey(0)