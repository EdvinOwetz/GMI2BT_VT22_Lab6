# Face recognition
import os
from os import path, getcwd
import cv2 as cv
import numpy as np

dirpath = getcwd()
print("dirpath=", dirpath)
trainingfolder = "Faces\\training"
validationfolder = "Faces\\validation"
print("trainingfolder=", trainingfolder)
print("validationfolder=", validationfolder)

person_names = []
for person_name in os.listdir(dirpath+"\\"+trainingfolder):
    person_names.append(person_name)
    
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

def face_req():
    face_features = []
    labels = []
    
    #working
    for person in person_names:
        print(person)
        cur_path = trainingfolder+"\\"+person
        print(cur_path)
        for image_name in os.listdir(dirpath+"\\"+cur_path):
            #print(image_name)
            #image_path= cur_path+"/"+image_name
            image_path= cur_path +"\\"+image_name
            #image_path = image_path
            print(image_name)
            print(image_path)
            image_data_raw=cv.imread(image_path)
            # if image_data_raw==None :
            #     print("FUCK there is no image!")
            #     continue
            #make in monochrome (svart vit)            
            image_data = cv.cvtColor(image_data_raw,cv.COLOR_RGB2GRAY)
            #cascade ? aka get the face!
            #face_recognition=
            face_recognition = face_cascade.detectMultiScale(image_data, scaleFactor=1.1, minNeighbors=6)
            for (x, y, w, h) in face_recognition:
                face_area = image_data[y:y + h, x:x + w]
                print(face_area)
                
            
            
face_req()