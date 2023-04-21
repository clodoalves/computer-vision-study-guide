import cv2
import dlib

colorFul = cv2.imread("content/Images/people3.jpg")

detector = dlib.cnn_face_detection_model_v1("content/Weights/mmod_human_face_detector.dat")

detections = detector(colorFul,4)

rectangleColor = (255, 0, 0)

for face in detections:
    cv2.rectangle(colorFul, (face.react.left(), face.react.top()), face.react.right(), face.react.bottom(), rectangleColor, thickness=1)
    
cv2.imshow("sample", colorFul)
cv2.waitKey(0)
cv2.destroyAllWindows()