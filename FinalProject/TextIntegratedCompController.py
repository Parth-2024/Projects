from Search import *
import webbrowser as web
import subprocess as sp
import speech_recognition as sr
import pyttsx3
import datetime
import pymongo as mg

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

def voice_assistant(respon):
	tm=datetime.datetime.now()
	hrs=tm.hour
	min=tm.minute
	welcome=f"Hello Parth its currently {hrs}:{min}"
	print("Welcome To Your Person System Controller")
	if respon==0:
			speak_text("Welcome To Your Person System Controller")
			speak_text(welcome)
	print(welcome)
		

	def opening(txt):
		speak_text(f"Opening {txt}")

	print('''Program's Features:\n1.Open Apps(command app_name):\nChrome\tNotePad\tSpotify\n2.Send a Whatsapp text(Command:send a text)\n3.Open a website through url(Command:open a website)\n4.Take a picture(command:Take a photo)\n5. Generate a photo from numpy(Command:generate)\n6.Shoot a video(Command:shoot a video)\n7.Make a collage photo(Command:make a collage)\n8. Get your current coordinates(Command:what are my current coordinates)\n9.Send a mail(Command:send a mail)\n10.Send bulk mail(Command:send a bulk)\n11.Set your system's volume level(Command: set the volume)\n12.Convert text to speech(Command: convert to speech)\n13.Google a query c=abd get top 5 urls(Command:i wanna google something)\n14.Access gemini(Command: open gemini)\n15.Send sms from your phone(Command:send sms)\n16.Create your own to do list(Command: open to-do-list)\n17.Input your fat percentage to get risk percentage of you having a heart attack(Command:access machine learning model)''')
	print("You can speak or type the above given commands to use the features")
	while True:
		if respon==0:
			key=listen_to_voice()
		else:
			key=input("Enter a command:")
		if (key is er1) or (key is er2):
			speak=key
			speak_text(speak)
			speak_text("Can you please repeat")
			continue
		elif key == "exit":
			if respon==0:
				speak_text("Byee")
			else:
				print("Byee")
			break
			
			
		elif key=="power down":
			if respon==0:
				speak_text("Powering Down")
			else:
				print("Powering Down")
			return "power down"

		negative=neg(key)
		note=notePad(key)
		spoti=spot(key)
		chm=chr(key)
		webs=website(key)
		txt=whats(key)
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
		mach=machine(key)
		gam=game(key)
		if(note) and (not(negative)):
			app="notepad"
			if respon==0:
				opening(app)
			sp.getoutput(app)
		elif(chm) and (not(negative)):
			app="chrome"
			if respon==0:
				opening(app)
			sp.getoutput("start chrome")
		elif(spoti) and (not(negative)):
			app="Spotify"
			if respon==0:
				opening(app)
			sp.getoutput(app)
		elif(txt) and (not(negative)):
			app="whatsapp"
			person=input("Enter the number of the person:")
			mess=input("Do you want ai generated text(Y/N):")
			if mess=='Y':
				from Ggle import gemini
				message=gemini(sys_role="you are a professional text typer who writes precise and to the point texts:")
			else:
				message=input("Enter your text:")
			hrs=int(input("Enter the hours:"))
			min=int(input("Enter the mins:"))
			time_delay=int(input("Enter time delay:"))
			if respon==0:
				opening(app)
			from Text import whatsapp
			whatsapp(person,message,hrs,min,time_delay)
		elif(webs) and (not(negative)):
			site=input("Enter url:")
			app="the web site"
			if respon==0:
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
			if respon==0:
				opening(app)
			choice=int(input("Optioins:1.for sinle photo 2.Photo in photo 3.for shades on a photo 4.for exit\nEnter your choice:"))
			if choice==1:
				from Camera import takephoto
				takephoto(file_name,photo_name,res)
			elif choice==2:
				from Camera import cropPhoto
				cropPhoto(file_name,photo_name)
			elif choice==3:
				from Camera import shade_on
				shade_on(photo_name)
			else:
				print("Ok")
		elif(collage_pht) and (not(negative)):
			m=int(input("Enter 0 and 1 for internal camera:"))
			n=int(input("Enter 1 for 1st external camera or 2 for 2nd internal camera:"))
			from Camera import photo_collage
			photo_collage(m,n)
		elif(gen_photo) and (not(negative)):
			speak_text("Generatining a photo")
			from CompFeatures import generate_photo
			generate_photo()
		elif(coordi) and (not(negative)):
			from Location import get_location
			lat, lng, loc_name = get_location()
			if respon==0:
				speak_text(f"your coordinates and loaction are {lat},{lng} and {loc_name}")
			print(f"Coordinates: {lat}, {lng}")
			print(f"Location Name: {loc_name}")
		elif(mail) and (not(negative)):
			from Mail import send_mail
			sender=input("Enter the email fro which you are gonna send the mail:")
			password=input("Enter its password:")
			receiver=input("Enter the email to which you are gonna send the mail:")
			subject=input("Enter the subject of the mail:\n")
			bd=input("Want gemini to write the mail for you(Y/N):")
			if bd=='Y':
				from Ggle import gemini
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
				from Ggle import gemini
				body=gemini("Your are a professional mail writer")
			else:
				body=input("Enter the body of the mail:\n")
			from Mail import send_bulk
			send_bulk(li,sender,password,subject,body)
		elif(vdo) and (not(negative)):
			name=input("Enter video name:")
			if input("Do you want video in video(Yes/No):")=="Yes":
				from Camera import video_in_video
				video_in_video()
			else:
				from Camera import take_video
				take_video(name)
		elif(vol) and (not(negative)):
			if respon==0:
				speak_text("At what level do you want to set your volume")
				vol=listen_to_voice()
			else:
				vol=int(input("At what level do you want to set your volume:"))
			from CompFeatures import set_volume
			set_volume(int(vol))
		elif(spch) and (not(negative)):
			text=input("Enter a text:")
			from CompFeatures import text_to_speech
			text_to_speech(text)
		elif(Ggl) and (not(negative)):
			query = input("Enter the search query: ")
			from Ggle import google
			google(query)
		elif(gemi) and (not(negative)):
			sys_role=input("Enter your instructions for the system:")
			from Ggle import gemini
			gemini(sys_role)
		elif(Sms) and (not(negative)):
			api_key="7f3327a40519291bd36576593bc4417bedbc9542"
			device_id="00000000-0000-0000-9954-493415ef70b1"
			number=input("Enter the number of the person you wanna send your sms too (along with country code):")
			text=input("Enter the message you want to send:")
			from Text import send_sms
			sent=send_sms(api_key,device_id,number,text)
			speak_text(sent)
		elif(ToDo) and (not(negative)):
			run=True
			client=mg.MongoClient("mongodb://localhost:27017/")
			db=client["To-Do-List"]
			col_list=db.list_collection_names()
			print(db.list_collection_names())
			for i in col_list:
				print(i)
			name=input("Enter the name of your list")
			print("Welcome to PYToDo-List\n Things you can do in this app:\n1.Enter a task\n2.Mark a task as done\n3.See all you tasks\n4.Mark a task as undone\n5.Delete a task")
			from CompFeatures import to_do_list
			while run:
				choice=int(input("Enter your choice:"))
				to_do_list(name,choice)
				resp=input("Do you wanna perfrom some more operations in your list(Y/N):")
				if resp=='N':
					run=False
		elif(mach) and (not(negative)):
			query=int(input("Enter your Body Fat percentage:"))
			from MachineLearning import machine_learning
			machine_learning(query)
		elif(gam) and (not(negative)):
			from CompFeatures import random_number_game
			random_number_game()
		elif(negative):
			print("Ok")
				
respon=int(input("0 for voice input \n1 for text input\nEnter your choice:"))
while True:
	if respon==0:
		print("Speak the wake up phrase (hey zara)")
		activate_text = listen_to_voice()
		activate_text = activate_text.lower()
		if activate_text=="hey zara":
			shut_down=voice_assistant(0)
			if shut_down=="power down":
				break
	else:
		activate_text = input("Enter wake up phrase(hey zara):")
		if activate_text=="hey zara":
			shut_down=voice_assistant(1)
			if shut_down=="power down":
				break