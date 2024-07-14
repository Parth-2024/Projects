import subprocess as sp
import pywhatkit as wa
import time
import requests
import streamlit as st
#Whatsapp
def whatsapp(person,message,hrs,mins,time_delay):
	'''Sends a whatsapp text to the specified number at the specified time'''
	wa.sendwhatmsg(person,message,hrs,mins)
	time.sleep(time_delay)
	st.write("sent")

#Sends sms from the user's phone
def send_sms(api_key,device_id,number,message):
		'''This function sends an sms from the user's phone to the person whose number is specified by the user'''
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