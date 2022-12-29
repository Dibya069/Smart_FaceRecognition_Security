#For Entry the face Data
import cv2
import face_recognition
import numpy as np
import time
import os
from ..Branch.subBranch.notify import notify
from datetime import date

class faceRecognition3:
    def __init__(self):
        self.path = 'images'
        self.images = []
        self.personName = []
        self.myList = os.listdir(self.path)
        self.cam = int(input("enter camera: "))
        # self.cam = input("enter camera: ")

    def adva(self):

        for cu_img in self.myList:
            current_img = cv2.imread(f'{self.path}/{cu_img}')
            self.images.append(current_img)  # It will read the images & store in a image list
            self.personName.append(os.path.splitext(cu_img)[0])  # It will get the image name & store in a personName list

        # this function used to encode the face
        def faceEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList

        encodeFaces = faceEncodings(self.images)
        print("ALL ENCODINGS COMPLETE .....")

        cap = cv2.VideoCapture(self.cam)

        while 1:
            _, frame = cap.read()
            frame = cv2.resize(frame, (600, 400))
            _, fr = cap.read()
            fr = cv2.resize(fr, (600, 400))
            originalFrame = frame.copy()
            faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

            facesCurrentFrame = face_recognition.face_locations(faces)  # It will give the face location
            encodeCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)  # It will give the face encodes

            # this loop used to compare and give distance between data faces with current live face
            for encodeFace, faceLoc in zip(encodeCurrentFrame, facesCurrentFrame):
                matches = face_recognition.compare_faces(encodeFaces, encodeFace)
                faceDis = face_recognition.face_distance(encodeFaces, encodeFace)

                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    for e_fr in faceDis:
                        if e_fr <= 0.45:
                            name = self.personName[matchIndex].upper()
                            print(f'{name} is here, door unlocking for 5 second')
                            time.sleep(3)
                            print('locked')
                            break
                else:
                    pis = notify(cap)
                    pis.pic(cap, fr)

            cv2.imshow("camera", originalFrame)
            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
