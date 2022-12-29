import cv2
from deepface import DeepFace

import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1YzdOYtG1h-Ox99X1SFdVwINzjlY8tbS3'
file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
for index, file in enumerate(file_list):
	print(index+1, 'file downloaded : ', file['title'])
	file.GetContentFile(file['title'])

path = r'./picture.jpg'
img = cv2.imread(path)

predictions = DeepFace.analyze(img)
emotions = predictions['emotion']

for key in emotions:
    if (emotions[key] > 1):
        print(key)




