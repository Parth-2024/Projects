import webbrowser as web
import subprocess as sp
import pywhatkit as wa
import time
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

def sendWAtxt(info):
	info1=info.split(",")
	wa.sendwhatmsg(info1[0],info1[1],int(info1[2]),int(info1[3]))

print("Welcome To Your Person Controller")
key=input("Enter your command:")
negative=neg(key)
note=notePad(key)
spoti=spot(key)
chm=chr(key)
webs=website(key)
txt=text(key)
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
elif(negative):
	print("Ok")