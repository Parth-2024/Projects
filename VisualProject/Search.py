'''All the functions with key as their parameter perform a search for specific set of words present in the lists they contain and return true or false according to the presence of the words of the list in the input key'''
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

def whats(key):
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
	clglst=["image collage","Image Collage"]
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

def machine(key):
	mllst=["machine"]
	for i in mllst:
		if i in key:
			return True
	return False

def game(key):
	gamelst=["game"]
	for i in gamelst:
		if i in key:
			return True
	return False

def log(key):
	loglist=["logistic"]
	for i in key:
		return True
	return False