import dlib
import cv2

selectedImage = cv2.imread("Content\Images\people2.jpg")

faceDetectorHog = dlib.get_frontal_face_detector()

detections = faceDetectorHog(selectedImage, 1)

rectangleColor = (0, 255, 0)

for face in detections:
    left, top, right, bottom = face.left(), face.top(), face.right(), face.bottom()
    cv2.rectangle(selectedImage, (left, top), (right, bottom), rectangleColor, thickness=2)

cv2.imshow("sample", selectedImage)

cv2.waitKey(0)