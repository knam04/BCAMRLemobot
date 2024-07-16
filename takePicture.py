import picamera
import RPi.GPIO as GPIO 
import subprocess 
import time 
import os 

camera = picamera.PiCamera ()
camera.brightness = 70
camera.color_effects = (128,128)

subprocess.Popen ('rclone mount emobot: $HOME/mnt/emobot --allow-non-empty', shell=True)

def button_callback ():
  print ("picture taken")
  camera.capture ('picture.jpg')
  os.system ('mv picture.jpg $HOME/mnt/emobot/picture.jpg")

GPIO.setwarnings(False)
GPIO.setmode(GPIO. BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD UP)

while True:
  input_state=GPIO.input(14)
  if input_state == False:
    button_callback()
    time.sIeep (0.2)

GPIO.cleanup ()
