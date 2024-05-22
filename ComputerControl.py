import webbrowser as web
import subprocess as sp
import pywhatkit as wa
import time
import cv2
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
	phtlst=["Photo","photo","pic","Pic"]
	for i in phtlst:
		if i in key:
			return True
	return False

def sendWAtxt(info):
	info1=info.split(",")
	wa.sendwhatmsg(info1[0],info1[1],int(info1[2]),int(info1[3]))

def takephoto(file_name,photo_name,save):
	cap=cv2.VideoCapture(1)
	status,photo=cap.read()
	if(save):
		cv2.imwrite(file_name,photo)
	print("Press Enter or Esc key to close the photo:")
	cv2.imshow(photo_name,photo)
	cv2.waitKey()
	cv2.destroyAllWindows()

print("Welcome To Your Person Controller")
key=input("Enter your command:")
negative=neg(key)
note=notePad(key)
spoti=spot(key)
chm=chr(key)
webs=website(key)
txt=text(key)
pic=pht(key)
if(note) and (not(negative)):
	sp.getoutput("notepad")
elif(chm) and (not(negative)):
	sp.getoutput("start chrome")
elif(spoti) and (not(negative)):
	sp.getoutput("Spotify")
elif(txt) and (not(negative)):
	info=input("Enter the number of the person, text you want to send, hr of the time, min of the time:")
	time_delay=int(input("Enter time delay:"))
	sendWAtxt(info)
	time.sleep(time_delay)
	sp.run(["taskkill", "/F", "/IM", "chrome.exe"])
elif(webs) and (not(negative)):
	site=input("Enter url:")
	web.open_new_tab(site)
elif(pic) and (not(negative)):
	photo_name=input("Enter name for the photo:")
	save=bool(input("Do you want to save the photo(0/1)?:"))
	if(save):
		file_name=input("Enter file name(save it under \".png\" ):")
	else:
		file_name="NA"
	takephoto(file_name,photo_name,save)

elif(negative):
	print("Ok")
