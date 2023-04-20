import dlib
import cv2

selectedImage =  cv2.imread("Content\Images\people3.jpg")

faceDetectorHog = dlib.get_frontal_face_detector()

detections = faceDetectorHog(selectedImage, 6)

retangleColor = (0, 255, 0)

for face in detections:
    cv2.rectangle(selectedImage, (face.left(), face.top()), (face.right(), face.bottom()), retangleColor, thickness = 1)
    
cv2.imshow("sample", selectedImage)

cv2.waitKey(0)