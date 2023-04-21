import dlib
import cv2

selectedImage = cv2.imread("content/Images/people2.jpg")

faceDetector = dlib.cnn_face_detection_model_v1("content/Weights/mmod_human_face_detector.dat")

detections = faceDetector(selectedImage, 1)

rectangleColor = (255, 0, 0)

for face in detections:
    left, top, right, bottom, confidence = face.rect.left(), face.rect.top(), face.rect.right(), face.rect.bottom(), face.confidence
    cv2.rectangle(selectedImage, (left, top), (right, bottom), rectangleColor, thickness=1)
    
cv2.imshow("sample", selectedImage)

cv2.waitKey(0)