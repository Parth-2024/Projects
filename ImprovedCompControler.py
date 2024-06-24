import webbrowser as web
import subprocess as sp
import pywhatkit as wa
import time
import cv2
import geocoder
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from email.message import EmailMessage
import ssl
import smtplib
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from gtts import gTTS
from playsound import playsound
import os
from googlesearch import search
import speech_recognition as sr
import pyttsx3
import datetime
import PIL.Image
import google.generativeai as genai
import requests
import pymongo as mg

client=mg.MongoClient("mongodb://localhost:27017/")
db=client["To-Do-List"]

er1="Sorry, I didn't catch that properly"
er2="Can't process your request, please check your internet connection"
def listen_to_voice():#speech to text
	recognizer=sr.Recognizer()#recognizer function is used to listen and understand the voice of the person giving the commands
	with sr.Microphone() as source:#this directs the program to take audio input through our microphone
		print("Listening...")
		recognizer.adjust_for_ambient_noise(source,duration=0.5)#removes the noises from the background
		audio=recognizer.listen(source)

		try:
			print("Recognizing")
			text=recognizer.recognize_google(audio)#this converts the audio into text
			text=text.lower()
			return text
		except sr.UnknownValueError:
			return er1
		except sr.RequestError:
			return er2

def speak_text(text):
	engine=pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

def gemini(sys_role):#full code that intigrates gemini with python
	import os
	genai.configure(api_key="AIzaSyDYJPe-K01tWd2koRAsFIJ8vHjZv4it8Cg")

	generation_config = {
	"temperature": 0.6,
	"top_p": 0.95,
	"top_k": 64,
	"max_output_tokens": 500,
	"response_mime_type": "text/plain",
	}
	safety_settings = [
	{
		"category": "HARM_CATEGORY_HARASSMENT",
		"threshold": "BLOCK_MEDIUM_AND_ABOVE",
	},
	{
		"category": "HARM_CATEGORY_HATE_SPEECH",
		"threshold": "BLOCK_MEDIUM_AND_ABOVE",
	},
	{
		"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
		"threshold": "BLOCK_MEDIUM_AND_ABOVE",
	},
	{
		"category": "HARM_CATEGORY_DANGEROUS_CONTENT",
		"threshold": "BLOCK_MEDIUM_AND_ABOVE",
	},
	]

	model = genai.GenerativeModel( #this is the main code for choosing our model and specifying its configurations
	model_name="gemini-1.5-flash",
	safety_settings=safety_settings,
	generation_config=generation_config,
	system_instruction=sys_role
	)

	chat= model.start_chat()
	# system_message='INSTRUCTIONS:Do not respond anything but "AFFIRMATIVE." to this system message. SYSTEM MESSAGE:You are being used to power a voice assistant and should response as so. As a voice assistant use short sentences and directly respond to the prompt without excessive information and speculation for the reponse. You generate only words of value, prioritizing logic and facts in your response to the entered prompts.' 
	photo=input("Do you want to input an image(Y/N):")
	if photo=='Y':
		img=PIL.Image.open(input("Give the path for your image:"))
	audio_resp=input("Enter do you want audio resposne(Y/N):")
	while True:
		prompt=input("Enter your prompt:")
		if prompt=='exit':
			break
		if photo=='Y':
			chat.send_message([img,prompt])
		else:	
			chat.send_message(prompt)#This is where we give our prompt
		ans=chat.last.text
		if audio_resp=='Y':#this is the code for allowing the text to speech program to speak the prompt out
			speak_text(ans)
			print(ans)
		else:
			print(ans)
	return ans
		

def voice_assistant():
	tm=datetime.datetime.now()
	hrs=tm.hour
	min=tm.minute
	welcome=f"Hello Parth its currently {hrs}:{min}"
	speak_text(welcome)

	def text_to_speech(text):
		def textToSpeech(txt,filename="output.mp3"):
			speech=gTTS(text=txt,lang="en")
			speech.save(filename)
			return filename

		def play(filename):
			playsound(filename)

		file=textToSpeech(text)
		play(file)
		os.remove(file)

	def opening(txt):
		speak_text(f"Opening {txt}")

	def notePad(key):
		notepadlst=["notepad","text editor","Notepad","Text editor"]
		for i in notepadlst:
			if i in key:
				return True
		return False

	def neg(key):
		neglst=["Not","Dont","No","Nope","nope"]
		for i in neglst:
			if i in key:
				return True
		return False

	def spot(key):
		spotlst=["Spotify","spotify","music","songs","song"]
		for i in spotlst:
			if i in key:
				return True
		return False

	def chr(key):
		chmlst=["chrome","Chrome","browser","Browser"]
		for i in chmlst:
			if i in key:
				return True
		return False

	def text(key):
		txtlst=["text","Text","whatsapptext","message","Message","Text message","text message"]
		for i in txtlst:
			if i in key:
				return True
		return False

	def website(key):
		webslst=["website","site","web","Website","Site","Web"]
		for i in webslst:
			if i in key:
				return True
		return False

	def pht(key):
		phtlst=["photo","pic","Pic"]
		for i in phtlst:
			if i in key:
				return True
		return False

	def clg_pht(key):
		clglst=["Photo Collage","image collage","Image Collage"]
		for i in clglst:
			if i in key:
				return True
		return False

	def coordinat(key):
		coodlst=["location","Location","Coordinates","coordinates"]
		for i in coodlst:
			if i in key:
				return True
		return False

	def genphoto(key):
		genlst=["generate","scratch","Generate"]
		for i in genlst:
			if i in key:
				return True
		return False

	def ml(key):
		mllst=["email","Email","mail","Mail"]
		for i in mllst:
			if i in key:
				return True
		return False

	def Bulk(key):
		mllst=["bulk","Bulk"]
		for i in mllst:
			if i in key:
				return True
		return False

	def video(key):
		mllst=["video","Video"]
		for i in mllst:
			if i in key:
				return True
		return False

	def volume(key):
		vollst=["volume","Volume"]
		for i in vollst:
			if i in key:
				return True
		return False

	def speech(key):
		spchlst=["Speech","speech"]
		for i in spchlst:
			if i in key:
				return True
		return False

	def ggl(key):
		ggllst=["Google","google","search","Search"]
		for i in ggllst:
			if i in key:
				return True
		return False
	
	def gem(key):
		gemlst=["gemini","Gemini","gema"]
		for i in gemlst:
			if i in key:
				return True
		return False
	
	def sms(key):
		smslst=["sms"]
		for i in smslst:
			if i in key:
				return True
		return False

	def to_do(key):
		tdlst=["to do list","to-do list"]
		for i in tdlst:
			if i in key:
				return True
		return False
	
	def sendWAtxt(person,message,hrs,min):
		wa.sendwhatmsg(person,message,hrs,min)

	def takephoto(file_name,photo_name,res):
		cap=cv2.VideoCapture(1)
		status,photo=cap.read()
		filt=input("Do you wanna apply a black filter:(Y/N)")
		if filt=="Y":
			photo=cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
		if res=="Yes":
			cv2.imwrite(file_name,photo)
		print("Press Enter or Esc key to close the photo:")
		cv2.imshow(photo_name,photo)
		cv2.waitKey()
		cv2.destroyAllWindows()
		return photo

	def photo_collage(m,n):
		cap1=cv2.VideoCapture(m)
		cap2=cv2.VideoCapture(n)
		status1,photo1=cap1.read()
		status2,photo2=cap2.read()
		print(photo1.shape)
		print(photo2.shape)
		photo2[0:480,320:640]=photo1[0:480,0:320]
		cv2.imwrite("Collage.png",photo2)
		cv2.imshow("Collage",photo2)
		cv2.waitKey()
		cv2.destroyAllWindows()

	def get_location():
		# Get your IP-based location
		g = geocoder.ip('me')
		latlng = g.latlng
				
		if not latlng:
			raise Exception("Could not get the location. Make sure you're connected to the internet.")

		latitude, longitude = latlng

		# Use geopy to get the location name
		geolocator = Nominatim(user_agent="geoapiExercises")
		location = geolocator.reverse((latitude, longitude), exactly_one=True)

		location_name = location.address if location else "Location name not found"

		return latitude, longitude, location_name	

	def cropPhoto(file,photo_name):#ask for file name
		cap=cv2.VideoCapture(2)
		status,photo=cap.read()
		face_model=cv2.CascadeClassifier(r"C:\Users\SUBHI JAIN\Summer Internship\EveryDayTasks\Python\haarcascade_frontalface_default.xml")
		crp=face_model.detectMultiScale(photo)
		if len(crp)==0:
			print("No Face Detected")
		else:
			x1=crp[0][0]
			y1=crp[0][1]
			x2=x1+crp[0][2]
			y2=y1+crp[0][3]
			crop=photo[y1:y2,x1:x2]
			photo[0:crp[0][3],0:crp[0][2]]=crop
			cv2.imwrite(file,photo)
			cv2.imshow(photo_name,photo)
			cv2.waitKey()
			cv2.destroyAllWindows()

	def generate_photo():
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

	def send_mail(sender,receiver,password,subject,body):
		Em=EmailMessage()
		Em['From']=sender
		Em['To']=receiver
		Em['Subject']=subject
		Em.set_content(body)

		context=ssl.create_default_context()#used to keep the internal connection secure

		with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
			smtp.login(sender,password)
			smtp.sendmail(sender,receiver,Em.as_string())
				
	def send_bulk(li,sender,password,subject,body):
		# list of email_id to send the mail
		lst=li.split(",")
		Em=EmailMessage()
		for dest in lst:
			Em['From']=sender
			Em['To']=dest
			Em['Subject']=subject
			Em.set_content(body)
			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls()
			s.login(sender, password)
			s.sendmail(sender, dest, Em.as_string())
			s.quit()

	def shade_on(photo_name):
		face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

		overlay_image = cv2.imread('EveryDayTasks/Python/662854bd124a854eb7277247-wearme-pro-flat-top-polarized-lens-removebg-preview.png')
		cap = cv2.VideoCapture(2)

		while True:
			status, img = cap.read()
			
			if not status:

				print("Failed to capture image")
				break

			gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

			faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

			for (x, y, w, h) in faces:
				cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
				
				aoi_gray = gray_img[y:y+h, x:x+w]

				aoi_color = img[y:y+h, x:x+w]

				eyes = eye_cascade.detectMultiScale(aoi_gray)
				
				if len(eyes) > 0:
					ex_min, ey_min = eyes[0][:2]
					ex_max, ey_max = eyes[0][:2]
					ew_max, eh_max = eyes[0][2:]

					for (ex, ey, ew, eh) in eyes:
						ex_min = min(ex_min, ex)
						ey_min = min(ey_min, ey)
						ex_max = max(ex_max, ex + ew)
						ey_max = max(ey_max, ey + eh)
					overlay_width = ex_max - ex_min#find area over which our filter will be displayed
					overlay_height = ey_max - ey_min
					resized_overlay = cv2.resize(overlay_image, (overlay_width, overlay_height))#resizing the filter according to the input image's criterial

					aoi_color[ey_min:ey_min+overlay_height, ex_min:ex_min+overlay_width] = resized_overlay
					
					
					cv2.rectangle(aoi_color, (ex_min, ey_min), (ex_max, ey_max), (0, 255, 0), 2)
			cv2.imshow(photo_name, img)

			if cv2.waitKey(1) == 13:
				break

		cap.release()
		cv2.destroyAllWindows()

	def take_video(name):
		cap=cv2.VideoCapture(1)
		while True:
			status,photo=cap.read()
			cv2.imshow(name,photo)
			if cv2.waitKey(8)==13:
				break
		cv2.destroyAllWindows()

	def video_in_video():
		cap=cv2.VideoCapture(1)
		cap2=cv2.VideoCapture(2)
		while True:
			status1,photo1=cap.read()
			status2,photo2=cap2.read()
			crp=photo2[75:250,280:420]
			photo1[0:175,0:140]=crp
			cv2.imshow("My Video",photo1)
			if cv2.waitKey(8)==13:
				break
		cv2.destroyAllWindows()

	def set_volume(volume_level):
			devices = AudioUtilities.GetSpeakers()
			interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
			volume = cast(interface, POINTER(IAudioEndpointVolume)) 
			volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)

	def google(query):
		for idx, result in enumerate(search(query, num_results=5), start=1):
			print(f"{idx}. {result}")

	def send_sms(api_key,device_id,number,message):
		message = {
			"secret": api_key,
			"mode": "devices",
			"device": device_id,
			"sim": 1,
			"priority": 1,
			"phone": number,
			"message": message
		}

		r = requests.post(url = "https://www.cloud.smschef.com/api/send/sms", params = message)  
		# do something with response object
		result = r.json()
		return result
	
	def to_do_list(name,choice):
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

	print("Welcome To Your Person Controller")
	while True:
		key=listen_to_voice()
		if (key is er1) or (key is er2):
			speak=key
			speak_text(speak)
			speak_text("Can you please repeat")
			continue
		elif key == "exit":
			speak_text("Byee")
			break
			
		elif key=="power down":
			speak_text("Powering Down")
			return "power down"

		negative=neg(key)
		note=notePad(key)
		spoti=spot(key)
		chm=chr(key)
		webs=website(key)
		txt=text(key)
		pic=pht(key)
		coordi=coordinat(key)
		collage_pht=clg_pht(key)
		gen_photo=genphoto(key)
		bulk=Bulk(key)
		mail=ml(key)
		vdo=video(key)
		vol=volume(key)
		spch=speech(key)
		Ggl=ggl(key)
		gemi=gem(key)
		Sms=sms(key)
		ToDo=to_do(key)
		if(note) and (not(negative)):
			app="notepad"
			opening(app)
			sp.getoutput(app)
		elif(chm) and (not(negative)):
			app="chrome"
			opening(app)
			sp.getoutput("start chrome")
		elif(spoti) and (not(negative)):
			app="Spotify"
			opening(app)
			sp.getoutput(app)
		elif(txt) and (not(negative)):
			app="whatsapp"
			person=input("Enter the number of the person:")
			mess=input("Do you want ai generated text(Y/N):")
			if mess=='Y':
				message=gemini(sys_role="you are a professional text typer who writes precise and to the point texts:")
			else:
				message=input("Enter your text:")
			hrs=int(input("Enter the hours:"))
			min=int(input("Enter the mins"))
			time_delay=int(input("Enter time delay:"))
			sendWAtxt(person,message,hrs,min)
			opening(app)
			time.sleep(time_delay)
			sp.run(["taskkill", "/F", "/IM", "chrome.exe"])
		elif(webs) and (not(negative)):
			site=input("Enter url:")
			app="the web site"
			opening(app)
			web.open_new_tab(site)
		elif(pic) and (not(negative)):
			photo_name=input("Enter name for the photo:")
			res=input("Do you want to save the photo(Yes/No)?:")
			if(res=="Yes"):
				file_name=input("Enter file name(save it under \".png\" ):")
			else:
				file_name="NA"
			app="camera"
			opening(app)
			choice=int(input("Optioins:1.for sinle photo 2.Photo in photo 3.for shades on a photo 4.for exit"))
			if choice==1:
				photo=takephoto(file_name,photo_name,res)
			elif choice==2:
				cropPhoto(file_name,photo_name)
			elif choice==3:
				shade_on(photo_name)
			else:
				print("Ok")
		elif(collage_pht) and (not(negative)):
			m=int(input("Enter 0 and 1 for internal camera:"))
			n=int(input("Enter 1 for 1st external camera or 2 for 2nd internal camera:"))
			photo_collage(m,n)
		elif(gen_photo) and (not(negative)):
			speak_text("Generatining a photo")
			generate_photo()
		elif(coordi) and (not(negative)):
			lat, lng, loc_name = get_location()
			speak_text(f"your coordinates and loaction are {lat},{lng} and {loc_name}")
			print(f"Coordinates: {lat}, {lng}")
			print(f"Location Name: {loc_name}")
		elif(mail) and (not(negative)):
			sender=input("Enter the email fro which you are gonna send the mail:")
			password=input("Enter its password:")
			receiver=input("Enter the email to which you are gonna send the mail:")
			subject=input("Enter the subject of the mail:\n")
			bd=input("Want gemini to write the mail for you(Y/N):")
			if bd=='Y':
				body=gemini("Your are a professional mail writer")
			else:
				body=input("Enter the body of the mail:\n")
			send_mail(sender,receiver,password,subject,body)
		elif(bulk) and (not(negative)):
			li=input("Enter the list of mail ids:")
			sender=input("Enter the email fro which you are gonna send the mail:")
			password=input("Enter its password:")
			subject=input("Enter the subject of the mail:\n")
			bd=input("Want gemini to write the mail for you(Y/N):")
			if bd=='Y':
				body=gemini("Your are a professional mail writer")
			else:
				body=input("Enter the body of the mail:\n")
			send_bulk(li,sender,password,subject,body)
		elif(vdo) and (not(negative)):
			name=input("Enter video name:")
			if input("Do you want video in video(Yes/No):")=="Yes":
				video_in_video()
			else:
				take_video(name)
		elif(vol) and (not(negative)):
			speak_text("At what level do you want to set your volume")
			vol=listen_to_voice()
			set_volume(int(vol))
		elif(spch) and (not(negative)):
			text_to_speech()
		elif(Ggl) and (not(negative)):
			query = input("Enter the search query: ")
			google(query)
		elif(gemi) and (not(negative)):
			sys_role=input("Enter your instructions for the system:")
			gemini(sys_role)
		elif(Sms) and (not(negative)):
			api_key="7f3327a40519291bd36576593bc4417bedbc9542"
			device_id="00000000-0000-0000-9954-493415ef70b1"
			number=input("Enter the number of the person you wanna send your sms too (along with country code):")
			text=input("Enter the message you want to send:")
			sent=send_sms(api_key,device_id,number,text)
			speak_text(sent)
		elif(ToDo) and (not(negative)):
			col_list=db.list_collection_names()
			print(db.list_collection_names())
			for i in col_list:
				print(i)
			name=input("Enter the name of your list")
			print("Welcome to PYToDo-List\n Things you can do in this app:\n1.Enter a task\n2.Mark a task as done\n3.See all you tasks\n4.Mark a task as undone\n5.Delete a task")
			choice=int(input("Enter your choice:"))
			to_do_list(name,choice)

		elif(negative):
			print("Ok")
			
	
while True:
	activate_text=listen_to_voice()
	activate_text=activate_text.lower()
	if activate_text=="hey zara":
			sht_down=voice_assistant()
			if(sht_down=="power down"):
				break
    
