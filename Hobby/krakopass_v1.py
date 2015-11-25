

import random
import datetime
#from datetime import date 
#from PIL import ImageTk, Image
#from Tkinter import *
import os
import magic
import wand
import Tkinter
import pygame
import pygame.camera

from wand.image import Image as imo

brightnes = 100
imgName = ""


#IMPORTANT https://www.pygame.org/docs/ref/camera.html
def get_picture():
	pygame.camera.init()
	print(pygame.camera.list_cameras())
	#pygame.camera.list_camera() #Camera detected or not
	cam = pygame.camera.Camera("/dev/video0",(640,480))		#video0 for local webcam and video1 for external 
	cam.start()
	print(cam.get_controls())
	cam.set_controls(False, False, brightnes)
	print(cam.get_controls())
	img = cam.get_image()
	imgName = str(datetime.datetime.now())+ ".jpg" 
	#print(imgName)
	
	#------------------------------
	pygame.image.save(img,str(imgName))
	#------------------------------
	drawOnImage()
	
#draws some stuff on the picture so that it looks like a passport
def drawOnImage():
	
	with imo(filename=imgName) as i:
		i.type = 'grayscale';
		i.save(filename=imgName);
	
	#m=magic.open(magic.MAGIC_NONE)
	#m.load()
	
	#Draw on the image so it looks like a passport
	placeForPrint()

#prints or moves the passport	
def placeForPrint():
	#print the passport
	#else put the picture in a folder named pasports
	pass






def init():
	get_picture()
#init()
	
	
from Tkinter import *

class Application(Frame):

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.create = Button(self)
        self.create["text"] = "Create Pass",
        self.create["command"] = init()

        self.create.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.geometry('{}x{}'.format(600, 200))		#set the size of the window

app = Application(master=root)
app.mainloop()
root.destroy()