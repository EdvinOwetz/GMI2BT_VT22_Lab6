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
    person_indexs = []
    
    #working
    for person in person_names:
        print(person)
        cur_path = trainingfolder+"\\"+person
        
        person_id=person_names.index(person)
        
        print(cur_path)
        for image_name in os.listdir(dirpath+"\\"+cur_path):
            image_path= cur_path +"\\"+image_name
            image_data_raw=cv.imread(image_path)
            #make in monochrome (svart vit)            
            image_data = cv.cvtColor(image_data_raw,cv.COLOR_RGB2GRAY)
            #cascade ? aka get the face!
            face_recognition = face_cascade.detectMultiScale(image_data, scaleFactor=1.1, minNeighbors=6)
            for (x, y, w, h) in face_recognition:
                face_data = image_data[y:y + h, x:x + w]
                face_features.append(face_data)
                person_indexs.append(person_id)
            # Save data in features (facearea)
    #save here
    # convert labels list as numpy same with feature list.
    face_features = np.array(face_features,dtype="object")
    person_indexs = np.array(person_indexs)
    
    face_recognizer= cv.face.LBPHFaceRecognizer_create()
    
    # Save traning data into trainer.yml
    face_recognizer.train(face_features, person_indexs)
    face_recognizer.save('surleywonderfulpeople.yml')
            # Handle labels, name of person on picture.


def face_validation():
    # Validate the training data on validation pictures.
    face_recognizer=cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read('surleywonderfulpeople.yml')
    #loop though images
    validation_image=list(os.listdir(dirpath+"\\"+validationfolder))
    for image in validation_image:
        image_path=validationfolder+"\\"+image
        image_data_raw=cv.imread(image_path)
        #make in monochrome (svart vit)            
        image_data = cv.cvtColor(image_data_raw,cv.COLOR_RGB2GRAY)
        # finds the face within the image
        face_recognition = face_cascade.detectMultiScale(image_data, scaleFactor=1.1, minNeighbors=6)
        
        for (x, y, w, h) in face_recognition:
                face_data = image_data[y:y + h, x:x + w]
                person_id, certainty = face_recognizer.predict(face_data)
                print(f"Image{validation_image.index(image)}[{image}] is {person_names[person_id]} with {certainty}% certainty. ")
        
        
        

    
        
# Show each result and confidence of the result.
            
face_req()
face_validation()