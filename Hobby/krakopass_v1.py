import random

#from datetime import date 
#from PIL import ImageTk, Image
#from Tkinter import *
import os
import time
import magic
import wand
import datetime

import datetime
import pygame
import pygame.camera
import time



from wand.display import display
from wand.drawing import Drawing

from wand.image import Image
#import wand.image as darr

brightnes = 64
imgName = ""

class takeImage:
	'takes image with webcam'
	def __init__(self, name):		#name	name of image
		self.name = name
	#IMPORTANT https://www.pygame.org/docs/ref/camera.html
	def get_picture(self):
		pygame.camera.init()
		print(pygame.camera.list_cameras())
		#pygame.camera.list_camera() #Camera detected or not
		cam = pygame.camera.Camera("/dev/video0",(640,480), "RGB")		#video0 for local webcam and video1 for external
		cam.start()
		print(cam.get_controls())
		cam.set_controls(False, False, 200)
		print(cam.get_controls())
		camImg = cam.get_image()
		 
		print(imgName)
		
		#------------------------------
		pygame.image.save(camImg,str(self.name))
		#------------------------------
		
		cam.stop()
		pygame.camera.quit()
		pygame.quit()
		
	

	



#draws some stuff on the picture so that it looks like a passport
def drawOnImage():
	navn = raw_input("Navn: ")
	farge = raw_input("Farge: ")
	patrulje = raw_input("patrulje: ")
	
	navn = "Navn: " + str(navn)
	farge = 'farge: ' + str(farge)
	patrulje = 'patrulje: ' + str(patrulje)
	
	imgName = (str(datetime.datetime.now())).replace(" ", "") + ".png"
	take1 = takeImage(imgName)
	take1.get_picture()
	time.sleep(2)
	file_path = imgName
	

	print("---grayscale image---")
	#var1 = raw_input("enter something: ")
	with Image(filename=file_path) as img:
		print(img.size)
		img.type = 'grayscale';
		with Image(filename='watermark.png') as fg_img:
			img.composite(fg_img, left=100, top=300)
			with Drawing() as draw:
				#add some text here
				draw.font_size = 30
				draw.text(100, 100, navn)
				draw.text(100, 250, farge)
				draw.text(100, 200, patrulje)
				with Image(filename='hvit.png') as hvit_img:
						draw(hvit_img)
						with Image(width=img.width+hvit_img.width, height=img.height) as big_img:
							big_img.composite_channel('default_channels',img,'over', 0, 0)
							big_img.composite_channel('default_channels',hvit_img,'blend', hvit_img.width, 0)
							big_img.resize(big_img.width/2, big_img.height/2)
							big_img.save(filename=file_path);
							print(big_img.size)



drawOnImage()
	


