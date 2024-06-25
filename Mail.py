from email.message import EmailMessage
import ssl
import smtplib
#Send a mail to anyone
def send_mail(sender,receiver,password,subject,body):
		'''This function asks for the subject and content of the mail and sends it to an email id given by the user'''
		Em=EmailMessage()
		Em['From']=sender
		Em['To']=receiver
		Em['Subject']=subject
		Em.set_content(body)

		context=ssl.create_default_context()#used to keep the internal connection secure

		with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
			smtp.login(sender,password)
			smtp.sendmail(sender,receiver,Em.as_string())

#Function for sending bulk mail			
def send_bulk(li,sender,password,subject,body):
	'''Works same as the send_mail function but instead of sending mail to single ID, it sends it to a list of mail IDs'''
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