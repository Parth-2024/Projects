from googlesearch import search
import PIL.Image
import google.generativeai as genai
import pyttsx3
import os
import streamlit as st
#Top 5 urls
def google(query):
		'''This function perfroms a google search for the query provided by the user and returns top 5 urls to the user'''
		for idx, result in enumerate(search(query, num_results=5), start=1):
			st.write(f"{idx}. {result}")

def speak_text(text):
	engine=pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

#Gemini Access

def gemini(sys_role):
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
		{"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
		{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
		{"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
		{"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
	]

	model = genai.GenerativeModel(
		model_name="gemini-1.5-flash",
		safety_settings=safety_settings,
		generation_config=generation_config,
		system_instruction=sys_role
	)
	
	if 'chat' not in st.session_state:
		st.session_state.chat = model.start_chat()
	
	if 'last_response' not in st.session_state:
		st.session_state.last_response = None


	chat = st.session_state.chat

	st.title("Gemini AI Assistant")

	with st.form("gemini_form"):
		photo = st.text_input("Do you want to input an image (Y/N):")
		path = ""
		if photo == 'Y':
			path = st.text_input("Give the path for your image:")
		
		audio_resp = st.text_input("Do you want an audio response (Y/N):")
		prompt = st.text_input("Enter your prompt:")
		submitted = st.form_submit_button("Submit")
		exit=st.form_submit_button("Exit")

		if submitted:
			if photo == 'Y' and path:
				img = PIL.Image.open(path)
				chat.send_message([img, prompt])
			else:
				chat.send_message(prompt)
				
			ans = chat.last.text
			st.session_state.last_response=ans

			if audio_resp == 'Y':
				speak_text(ans)
			
			st.write(ans)
		if exit:
			st.write("Exiting the prompt session")
			return st.session_state.last_response

