import cv2;

image = cv2.imread("content/images/people1.jpg")

print(image.shape)

image = cv2.resize(image, (800, 600))

grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("sample", grayScaleImage)

print(grayScaleImage.shape)

cv2.waitKey(0)

cv2.destroyAllWindows()