from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pymongo as mg
import cv2
import numpy as np
from gtts import gTTS
from playsound import playsound
import os
import random as rn
import math
#Volume level setter
def set_volume(volume_level):
    
	'''This functions sets the volume level of the system according to the level input by the user'''		
	devices = AudioUtilities.GetSpeakers()
	interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(IAudioEndpointVolume)) 
	volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)

client=mg.MongoClient("mongodb://localhost:27017/")
db=client["To-Do-List"]
#To-Do list
def to_do_list(name,choice):
	'''This function enables the user to create n number of to do list on any topic of their desire'''
	def enter_task(task):
		tasks=col.find()
		data={"To-Do":task,"Action":"Not Done"}
		col.insert_one(data)
		lst=list(filter(lambda x:x["Action"]=="Not Done",col.find({},{"_id":0})))
		for i in range(0,len(lst)):
			print(lst[i]["To-Do"], ":",lst[i]["Action"])

	def mark_done(task):
		lst=list(col.find({},{"_id":0}))
		count=0
		fnd=False
		while count<len(lst):
			if task == lst[count]["To-Do"]:
				print(1)
				col.update_one({"To-Do":task,"Action":"Not Done"},{"$set":{"Action":"Done"}})
				fnd=True
				break
			count+=1
		if fnd==False:
			print("Task not found")
		lst=list(col.find({},{"_id":0}))
		for i in range(0,len(lst)):
			print(lst[i]["To-Do"], ":",lst[i]["Action"])

	def display_all_tasks():
		lst=list(col.find({},{"_id":0}))
		for i in range(0,len(lst)):
			print(lst[i]["To-Do"], ":",lst[i]["Action"])

	def mark_undone(task):
		lst=list(col.find({},{"_id":0}))
		count=0
		fnd=False
		while count<len(lst):
			if task == lst[count]["To-Do"]:
				print(1)
				col.update_one({"To-Do":task,"Action":"Done"},{"$set":{"Action":"Not Done"}})
				fnd=True
				break
			count+=1
		if fnd==False:
			print("Task not found")
		lst=list(col.find({},{"_id":0}))
		for i in range(0,len(lst)):
			print(lst[i]["To-Do"], ":",lst[i]["Action"])

	def delete_task(task):
		task=input("Enter the task you wanna delete:")
		lst=list(col.find({},{"_id":0}))
		count=0
		fnd=False
		while count<len(lst):
			if task == lst[count]["To-Do"]:
				print(1)
				col.delete_one({"To-Do":task})
				fnd=True
				break
			count+=1
		if fnd==False:
			print("Task not found")
		lst=list(col.find({},{"_id":0}))
		for i in range(0,len(lst)):
			print(lst[i]["To-Do"], ":",lst[i]["Action"])
	col=db[name]
	if choice==1:
		task=input("Enter your task:")
		enter_task(task)
	elif choice==2:
		task=input("Enter the task you wanna mark done:")
		mark_done(task)
	elif choice==3:
		display_all_tasks()
	elif choice==4:
		task=input("Enter the task you wanna mark undone:")
		mark_undone(task)
	elif choice==5:
		task=input("Enter the task you wanna delete:")
		delete_task(task)

#Generates a photo from scratch
def generate_photo():
		'''This function creates a photo from scratch with just the help of numpy'''
		image=[]
		for i in range(1,76):
			for j in range(1,151):
				image.append([230,0,0])
		for i in range(76,151):
			for j in range(1,41):
				image.append([0,230,0])
			for k in range(41,151):
				image.append([0,0,230])
		print(image)
		image=np.array(image,dtype=np.uint8)
		image=image.reshape(150,150,3)
		image[81:101,71:91]=[0,0,0]
		image[81:101,121:141]=[0,0,0]
		image[121:151,96:116]=[0,0,0]
		image[76:151,61:66]=[0,0,0]
		# image[121:151,42:60]=[0,0,0]
		print(image)
		print(type(image))
		print(image.shape)
		cv2.imshow("pixel-art",image)
		cv2.waitKey()
		cv2.destroyAllWindows()

#Text to speech
def text_to_speech(text):
		'''This function takes a text as an input from the user, converts it into audio and plays it on the system'''
		def textToSpeech(txt,filename="output.mp3"):
			speech=gTTS(text=txt,lang="en")
			speech.save(filename)
			return filename

		def play(filename):
			playsound(filename)

		file=textToSpeech(text)
		play(file)
		os.remove(file)

def random_number_game():

	upper=int(input("Enter the upper limit:"))
	lower=int(input("Enter the lower limit:"))

	number=rn.randint(lower,upper)
	chances=round(math.log(upper-lower+1,2))
	count=0
	fnd=False

	print(f"You have got {chances} chances to guess the number!!!")
	while count<chances:
		guess=int(input("Guess a number:"))
		if guess==number:
			fnd=True
			print(f"Bravooo!!! You guessed the number in {count+1} chances")
			break
		elif guess<number:
			print(f"Go higher\nYou are left with {chances-(count+1)}")
		else:
			print(f"Go lower\nYou are left with {chances-(count+1)}")
		count+=1

	if count>=chances and fnd==False:
		print(f"The number was {number}\nYou didn't guess the number in the given {chances} chances :(\nBetter luck next time")
		return
	else:
		return 