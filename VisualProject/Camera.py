import cv2
import streamlit as st
#Takes a single photo
def takephoto(file_name,photo_name,res,filt):
	'''Take a photo of the user also asks to apply a black and white filter over the photo'''
	cap=cv2.VideoCapture(2)
	status,photo=cap.read()
	if filt=="Y":
		photo=cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
	if res=="Yes":
		cv2.imwrite(file_name,photo)
	st.write("Press Enter or Esc key to close the photo:")
	cv2.imshow(photo_name,photo)
	cv2.waitKey()
	cv2.destroyAllWindows()

#Crops out the face of the user
def cropPhoto(file,photo_name):
	'''It takes a photo of the user than crops out his/her face and paste it in on the top left corner of the photo'''
	cap=cv2.VideoCapture(2)
	status,photo=cap.read()
	face_model=cv2.CascadeClassifier(r"C:\Users\SUBHI JAIN\Summer Internship\EveryDayTasks\Python\haarcascade_frontalface_default.xml")
	crp=face_model.detectMultiScale(photo)
	if len(crp)==0:
		st.write("No Face Detected")
	else:
		x1=crp[0][0]
		y1=crp[0][1]
		x2=x1+crp[0][2]
		y2=y1+crp[0][3]
		crop=photo[y1:y2,x1:x2]
		photo[0:crp[0][3],0:crp[0][2]]=crop
		# cv2.imwrite(file,photo)
		cv2.imshow(photo_name,photo)
		cv2.waitKey()
		cv2.destroyAllWindows()

#Applies a shade over the user's face		
def shade_on(photo_name):
	'''Applies a shade over the face of the user and gives output in video form'''
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

#Photo Collage
def photo_collage(m,n):
	'''Takes input of two photos from two different camera and forms a collage of those to images'''
	cap1=cv2.VideoCapture(m)
	cap2=cv2.VideoCapture(n)
	status1,photo1=cap1.read()
	status2,photo2=cap2.read()
	photo2[0:480,320:640]=photo1[0:480,0:320]
	cv2.imwrite("Collage.png",photo2)
	cv2.imshow("Collage",photo2)
	cv2.waitKey()
	cv2.destroyAllWindows()

#Shoots a video		
def take_video(name):
	'''It streams a live feed of the whatever the user's camera is pointing towards'''
	cap=cv2.VideoCapture(2)
	while True:
		status,photo=cap.read()
		cv2.imshow(name,photo)
		if cv2.waitKey(8)==13:
			break
	cv2.destroyAllWindows()

#Display two video feeds side by side	
def video_in_video():
		'''This function takes input from two camera and steams their live feeds side by side'''
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