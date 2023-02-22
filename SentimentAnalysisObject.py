import cv2
from deepface import DeepFace

import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import tkinter as tk
import tkinter.font as font
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1YzdOYtG1h-Ox99X1SFdVwINzjlY8tbS3'
clicked = False

def predEmotions():
    global clicked
    if clicked == False:
        clicked = True
        canvas1.itemconfig(text, text="Please wait...", font="Comfortaa 20")
        root.update()
        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
        for index, file in enumerate(file_list):
            #print(index+1, 'file downloaded : ', file['title'])
            file.GetContentFile(file['title'])

        path = r'./picture.jpg'
        img = cv2.imread(path)

        predictions = DeepFace.analyze(img, enforce_detection=False)
        emotions = ""
        for key in predictions['emotion']:
            if ((predictions['emotion'])[key] > 1):
                emotions += key + " "
        #label1 = tk.Label(root, text=emotions, bg="#FFEBB7")
        #canvas1.create_window(200, 230, window=label1)
        canvas1.itemconfig(text, text=emotions, font="Comfortaa 35")
        clicked = False

root= tk.Tk()
root.configure(bg="#FFEBB7")
root.resizable(False, False)

canvas1 = tk.Canvas(root, width=800, height=600, bg="#FFEBB7")
canvas1.pack()

#entry1 = tk.Entry(root) 
text = canvas1.create_text(400,350,font="Comfortaa 20",text="Waiting...")
myFont = font.Font(family='Helvetica', size=25, weight='bold')
button1 = tk.Button(text='Predict Emotions!', command=predEmotions,height=2, width=20, bg="#A2E2FF", activebackground="#92E2FE")
button1['font'] = myFont

canvas1.create_window(400, 250, window=button1)

root.mainloop()
