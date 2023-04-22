from PIL import Image
import numpy
import zipfile
import os
import cv2

#loading database
zipObject = zipfile.ZipFile(file="content/Datasets/yalefaces.zip", mode = "r")
zipObject.extractall("./content/Images")
zipObject.close()

#pre-process of images
faces = []
ids = []

def getIdSubject (fileName):
    splitString = fileName.split('.')
    return int(splitString[0][-2:]) 

for fileName in os.listdir("content/Images/yalefaces/train"):
    id = getIdSubject(fileName)
    ids.append(id)
    grayScaleImage = Image.open(os.path.join("content/Images/yalefaces/train", fileName)).convert('L')
    imageNp = numpy.array(grayScaleImage, 'uint8')
    faces.append(imageNp)    
    
#LBPH classifier training    
lbphClassifier = cv2.face.LBPHFaceRecognizer_create()
lbphClassifier.train(faces, numpy.array(ids))
lbphClassifier.write("content/GeneratedClassifiers/lbph_classifier.yml")

#Face recognize
lbphClassifierTest = cv2.face.LBPHFaceRecognizer_create()
lbphClassifierTest.read("content/GeneratedClassifiers/lbph_classifier.yml")

grayScaleTestImage = Image.open("content/Images/yalefaces/test/subject01.happy.gif").convert('L')

testImageNp = numpy.array(grayScaleTestImage, 'uint8')

expectedSubjectId = str(getIdSubject("content/Images/yalefaces/test/subject01.happy.gif"))

predction = lbphClassifierTest.predict(testImageNp)

predictedSubjectId = str(predction[0])

cv2.putText(testImageNp, "Predicted: "+ predictedSubjectId, (10,30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,255,0))
cv2.putText(testImageNp, "Expected: "+ expectedSubjectId, (10,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0))

cv2.imshow("Foo", testImageNp)

cv2.waitKey(0)

cv2.destroyAllWindows()