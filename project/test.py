import imageio

import time
import requests
import smtplib
import picamera                                                               

from PIL import Image
import os



for i in range(10):
    camera=picamera.PiCamera()
    camera.resolution=(1024,768)
    camera.capture('./project/test/'+str(i)+'.jpg')
    camera.close()

path = [f"./project/test/{i}" for i in os.listdir("./project/test")]
print(path)
imgs = [ Image.open(i) for i in path]
imageio.mimsave('./project/test.gif', imgs, fps=2.0)