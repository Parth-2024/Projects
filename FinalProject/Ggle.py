from googlesearch import search
import PIL.Image
import google.generativeai as genai
import pyttsx3
import os
#Top 5 urls
def google(query):
		'''This function perfroms a google search for the query provided by the user and returns top 5 urls to the user'''
		for idx, result in enumerate(search(query, num_results=5), start=1):
			print(f"{idx}. {result}")

def speak_text(text):
	engine=pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

#Gemini Access
def gemini(sys_role):#full code that intigrates gemini with python
	'''This function enables the user to use Gemini on their system without opening it on their browser'''
	genai.configure(api_key="AIzaSyA9aKVprRaOwT2NblF5weiVyLnUhDXQjWo")

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
gemini("Act like a human")