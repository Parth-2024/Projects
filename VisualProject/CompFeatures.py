from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pymongo as mg
import cv2
import numpy as np
from gtts import gTTS
from playsound import playsound
import os
import streamlit as st
import random as rn
import math
import pyttsx3
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
			st.write(lst[i]["To-Do"], ":",lst[i]["Action"])

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
			st.write("Task not found")
		lst=list(col.find({},{"_id":0}))
		for i in range(0,len(lst)):
			st.write(lst[i]["To-Do"], ":",lst[i]["Action"])

	def display_all_tasks():
		lst=list(col.find({},{"_id":0}))
		for i in range(0,len(lst)):
			st.write(lst[i]["To-Do"], ":",lst[i]["Action"])

	def mark_undone(task):
		lst=list(col.find({},{"_id":0}))
		count=0
		fnd=False
		while count<len(lst):
			if task == lst[count]["To-Do"]:
				col.update_one({"To-Do":task,"Action":"Done"},{"$set":{"Action":"Not Done"}})
				fnd=True
				break
			count+=1
		if fnd==False:
			st.write("Task not found")
		lst=list(col.find({},{"_id":0}))
		for i in range(0,len(lst)):
			st.write(lst[i]["To-Do"], ":",lst[i]["Action"])

	def delete_task(task):
		lst=list(col.find({},{"_id":0}))
		count=0
		fnd=False
		while count<len(lst):
			if task == lst[count]["To-Do"]:
				col.delete_one({"To-Do":task})
				fnd=True
				break
			count+=1
		if fnd==False:
			st.write("Task not found")
		lst=list(col.find({},{"_id":0}))
		st.write("Remaining To-Dos:")
		for i in range(0,len(lst)):
			st.write(lst[i]["To-Do"], ":",lst[i]["Action"])
	col=db[name]
	if choice==1:
		task=st.text_input("Enter your task:")
		if st.button("Add"):
			enter_task(task)
	elif choice==2:
		task=st.text_input("Enter the task you wanna mark done:")
		if st.button("Done"):
			mark_done(task)
	elif choice==3:
		display_all_tasks()
	elif choice==4:
		task=st.text_input("Enter the task you wanna mark undone:")
		if st.button("Not Done"):
			mark_undone(task)
	elif choice==5:
		task=st.text_input("Enter the task you wanna delete:")
		if st.button("Delete"):
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
def text_to_speech():
		'''This function takes a text as an input from the user, converts it into audio and plays it on the system'''
		if "speech" not in st.session_state:
			st.session_state.speech=None
		with st.form(key="Voice"):
			st.session_state.speech= st.text_input("Enter a text:")
			st.write(st.session_state.speech)
			convert = st.form_submit_button(label="Convert to Speech")
			if convert:
				engine=pyttsx3.init()
				engine.say(st.session_state.speech)
				engine.runAndWait()
text_to_speech()
def random_number_game():# Initialize session state variables
	if "upper" not in st.session_state:
		st.session_state.upper = None
	if "lower" not in st.session_state:
		st.session_state.lower = None
	if "number" not in st.session_state:
		st.session_state.number = None
	if "chances" not in st.session_state:
		st.session_state.chances = None
	if "count" not in st.session_state:
		st.session_state.count = 0
	if "fnd" not in st.session_state:
		st.session_state.fnd = False

	# Game setup
	st.title("Guess the Number Game")

	if st.session_state.number is None:
		st.session_state.upper = st.number_input("Enter the upper limit:", min_value=1, step=1)
		st.session_state.lower = st.number_input("Enter the lower limit:", min_value=0, step=1)

		if st.button("Start Game"):
			if st.session_state.upper > st.session_state.lower:
				st.session_state.number = rn.randint(st.session_state.lower, st.session_state.upper)#it choose a random number from the range between the upper and lower limit
				st.session_state.chances = round(math.log(st.session_state.upper - st.session_state.lower + 1, 2))#Specifies the number of chances a player has
				st.session_state.count = 0
				st.session_state.fnd = False
				st.write(f"You have got {st.session_state.chances} chances to guess the number!")
			else:
				st.write("Upper limit must be greater than lower limit.")

	if st.session_state.number is not None and not st.session_state.fnd:
		guess = st.number_input("Guess a number:", min_value=st.session_state.lower, max_value=st.session_state.upper, step=1)

		if st.button("Submit Guess"):
			if st.session_state.count < st.session_state.chances:
				st.session_state.count += 1
				if guess == st.session_state.number:
					st.session_state.fnd = True
					st.write(f"Bravooo!!! You guessed the number in {st.session_state.count} chances")
				elif guess < st.session_state.number:
					st.write(f"Go higher! You have {st.session_state.chances - st.session_state.count} chances left.")
				else:
					st.write(f"Go lower! You have {st.session_state.chances - st.session_state.count} chances left.")
			
		if st.session_state.count >= st.session_state.chances and not st.session_state.fnd:
			st.write(f"The number was {st.session_state.number}. You didn't guess the number in the given {st.session_state.chances} chances :(\nBetter luck next time")
			st.session_state.number = None

	if st.button("Reset Game"):
		st.session_state.upper = None
		st.session_state.lower = None
		st.session_state.number = None
		st.session_state.chances = None
		st.session_state.count = 0
		st.session_state.fnd = False
		st.experimental_rerun()
