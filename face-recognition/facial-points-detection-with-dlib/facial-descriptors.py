import cv2
import dlib
import os
from PIL import Image
import numpy

pathNameTrainDataset = "Content/Images/yalefaces/train/"
pathNameTestDataset = "Content/Images/yalefaces/test/"
confianca = 0.5

faceDetector = dlib.get_frontal_face_detector()
facePointsDetector = dlib.shape_predictor("Content/Weights/shape_predictor_68_face_landmarks.dat")
faceDescriptorExtractor = dlib.face_recognition_model_v1("Content/Weights/dlib_face_recognition_resnet_model_v1.dat")
facesDescriptorsTrainDataset = None
facesDescriptorsTestDataset = None

def getIdSubject(fileName):
    splitString = fileName.split('.')
    return int(splitString[0][-2:]) 

def getFacesDescriptorsByDataset(pathName):
    dic = {}
    index = 0
    for imageName in os.listdir(pathName):
        fullPathImage = pathName+imageName
        image = Image.open(fullPathImage).convert('RGB')
        imageNp = numpy.array(image, 'uint8')
        detections = faceDetector(imageNp, 1)
            
        for face in detections:
            dic[index] = fullPathImage
            index += 1
            facePoints = facePointsDetector(imageNp, face)     
                
        faceDescriptor = list(faceDescriptorExtractor.compute_face_descriptor(imageNp, facePoints))
        faceDescriptor = numpy.asarray(faceDescriptor, dtype=numpy.float64)
        faceDescriptor = faceDescriptor[numpy.newaxis, :]

        facesDescriptorsTrainDataset = None
        
        if (facesDescriptorsTrainDataset is None):
            facesDescriptorsTrainDataset = faceDescriptor
        else:
            facesDescriptorsTrainDataset = numpy.concatenate((facesDescriptorsTrainDataset, faceDescriptor), axis = 0)

    return dic,facesDescriptorsTrainDataset

trainDatasetDic, facesDescriptorsTrainDataset = getFacesDescriptorsByDataset(pathNameTrainDataset)
testDatasetDic, facesDescriptorsTestDataset = getFacesDescriptorsByDataset(pathNameTestDataset)
indexTestDatabase = 0

#TODO: refactoring of code

for imageName in os.listdir(pathNameTestDataset):
    fullPathImage = pathNameTestDataset+imageName
    image = Image.open(fullPathImage).convert('RGB')
    imageNp = numpy.array(image, 'uint8')
    detections = faceDetector(imageNp, 1)
    for face in detections:
        points = facePointsDetector(imageNp, face)
        
        faceDescriptor = faceDescriptorExtractor.compute_face_descriptor(imageNp, points)
        faceDescriptor = numpy.asarray(faceDescriptor, dtype=numpy.float64)
        faceDescriptor = faceDescriptor[numpy.newaxis, :]
        
        distancias = numpy.linalg.norm(faceDescriptor - facesDescriptorsTrainDataset, axis = 1)
        indiceMinino = numpy.argmin(distancias)
        distanciaMinina = distancias[indiceMinino]
        
        print(distanciaMinina)        

        if (distanciaMinina <= confianca):
            predictedId = getIdSubject(trainDatasetDic[indiceMinino])
        else:
            predictedId = 'Face nao identificada'
        
        expectedId = getIdSubject(testDatasetDic[indexTestDatabase])
                
        image = Image.open(testDatasetDic[indexTestDatabase]).convert('RGB')
        imageNp = numpy.array(image, 'uint8')
        
        cv2.putText(imageNp, 'Pred: ' + str(predictedId), (10,30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0))
        cv2.putText(imageNp, 'Exp: ' + str(expectedId), (10,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0))
        cv2.imshow('sample', imageNp)    
        cv2.waitKey(0)
        indexTestDatabase += 1 

cv2.destroyAllWindows()