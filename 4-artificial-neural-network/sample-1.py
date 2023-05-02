import cv2
import numpy
import os
import zipfile
import tensorflow
import pandas
import seaborn
import matplotlib
from PIL import Image

#Extracting image pixels
zippedFile = zipfile.ZipFile('content/Datasets/homer_bart_1.zip', mode='r')
zippedFile.extractall('content/Datasets/')
zippedFile.close()

folderPath = 'content/Datasets/homer_bart_1'
defaultWidth, defaultHeigth = 128, 128

patternedImages = []
classes = []

for fileName in os.listdir(folderPath):
    if (not fileName.startswith('.DS')):
        fullPathImage = os.path.join(folderPath, fileName)
        image = cv2.imread(fullPathImage)
        image = cv2.resize(image, (defaultWidth, defaultHeigth))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)       
        image = image.ravel()        
        patternedImages.append(image)
       
        if (fileName.startswith('b')):
            imageClass = 0
        else:
            imageClass = 1
            
        classes.append(imageClass)
        
