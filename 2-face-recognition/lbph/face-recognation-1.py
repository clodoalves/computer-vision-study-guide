from PIL import Image
import numpy
import zipfile
import os
import cv2
from sklearn.metrics import accuracy_score

#Yale faces database: http://cvc.cs.yale.edu/cvc/projects/yalefaces/yalefaces.html

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
#Classifier parameters for the best accuracy found 
#lbphClassifier = cv2.face.LBPHFaceRecognizer_create(radius = 4, neighbors = 14, grid_x = 9, grid_y = 9)
lbphClassifier = cv2.face.LBPHFaceRecognizer_create()
lbphClassifier.train(faces, numpy.array(ids))
lbphClassifier.write("content/GeneratedClassifiers/lbph_classifier.yml")

#Face recognition
def GetPredictedAndExpectedValues(imagePath):   
    grayScaleTestImage = Image.open(imagePath).convert('L')
    testImageNp = numpy.array(grayScaleTestImage, 'uint8')
    prediction = lbphClassifier.predict(testImageNp)
    predictedSubjectId = str(prediction[0])
    
    expectedSubjectId = str(getIdSubject(imagePath))

    return predictedSubjectId, expectedSubjectId

#Classifier evaluation
predictedSubjectIds = []
expectedSubjectIds = []

for fileName in os.listdir("content/Images/yalefaces/test"):
    predictedId, expectedId = GetPredictedAndExpectedValues(os.path.join("content/Images/yalefaces/test", fileName))
    predictedSubjectIds.append(predictedId)
    expectedSubjectIds.append(expectedId)

predictedSubjectIds = numpy.array(predictedSubjectIds)
expectedSubjectIds = numpy.array(expectedSubjectIds)

print(accuracy_score(expectedSubjectIds, predictedSubjectIds))