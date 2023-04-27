import dlib
import cv2

image = cv2.imread("Content/Images/people2.jpg")

#facial points detection
faceDetector = dlib.get_frontal_face_detector()
pointsDetector = dlib.shape_predictor("Content/Weights/shape_predictor_68_face_landmarks.dat")
detections = faceDetector(image, 1)

rectangleColor = (0,255,255)

for face in detections:
    facePoints = pointsDetector(image, face)
    for point in facePoints.parts():
        cv2.circle(image, (point.x, point.y), radius = 2, color = rectangleColor, thickness = 1)    
    left, top, right, bottom = face.left(), face.top(), face.right(), face.bottom()
    cv2.rectangle(image, (left, top), (right, bottom), rectangleColor, 2)
    
cv2.imshow("sample", image)
cv2.waitKey()
cv2.destroyAllWindows()