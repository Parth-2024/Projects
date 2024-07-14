import streamlit as st
from Search import *
import webbrowser as web
import subprocess as sp
import speech_recognition as sr
import pyttsx3
import datetime
import pymongo as mg

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #000000;
    }
    .title {
        color: #00008B;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #FFFFFF;
        font-size: 24px;
        text-align: center;
        margin-bottom: 20px;
    }
    .label {
        font-size: 20px;
        color: #FFFFFF;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def voice_assistant(respon):
    tm = datetime.datetime.now()
    hrs = tm.hour
    mins = tm.minute
    welcome = f"Hello Parth, it's currently {hrs}:{mins}"
    st.markdown('<div class="title">Welcome To Your Personal System Controller</div>', unsafe_allow_html=True)
    st.write(welcome)

    st.markdown(
        '''
        <div class="subtitle">Program's Features:</div>
        <ul>
            <li>Open Apps (command app_name): Chrome, NotePad, Spotify</li>
            <li>Send a Whatsapp text (Command: send a text)</li>
            <li>Open a website through URL (Command: open a website)</li>
            <li>Take a picture (Command: Take a photo)</li>
            <li>Generate a photo from numpy (Command: generate)</li>
            <li>Shoot a video (Command: shoot a video)</li>
            <li>Make a collage photo (Command: make a collage)</li>
            <li>Get your current coordinates (Command: what are my current coordinates)</li>
            <li>Send a mail (Command: send a mail)</li>
            <li>Send bulk mail (Command: send a bulk)</li>
            <li>Set your system's volume level (Command: set the volume)</li>
            <li>Convert text to speech (Command: convert to speech)</li>
            <li>Google a query and get top 5 URLs (Command: I wanna google something)</li>
            <li>Access Gemini (Command: open Gemini)</li>
            <li>Send SMS from your phone (Command: send SMS)</li>
            <li>Create your own to-do list (Command: open to-do-list)</li>
            <li>Random number game(Command: lets play a game)</li>
            <li>Input your fat percentage to get the risk percentage of you having a heart attack (Command: access machine learning model)</li>
            <li>Logistic Regression Model Maker(Command: make a logistic regression model)</li>
        </ul>
        ''', 
        unsafe_allow_html=True
    )
    st.write("You can speak or type the above-given commands to use the features")

    if respon == 1:
        key = st.text_input("Enter a command:")
        if st.button("Execute"):
            st.write(f"Stored Input: {key}")
        if key == "exit":
            st.write("Byee")
        elif key == "power down":
            st.write("Powering Down")
            return "power down"

        # Functions like neg, notePad, spot, chr, website, etc., need to be defined
        negative = neg(key)
        note = notePad(key)
        spoti = spot(key)
        chm = chr(key)
        webs = website(key)
        txt = whats(key)
        pic = pht(key)
        coordi = coordinat(key)
        collage_pht = clg_pht(key)
        gen_photo = genphoto(key)
        bulk = Bulk(key)
        mail = ml(key)
        vdo = video(key)
        vol = volume(key)
        spch = speech(key)
        Ggl = ggl(key)
        gemi = gem(key)
        Sms = sms(key)
        ToDo = to_do(key)
        mach = machine(key)
        gam = game(key)
        logistic=log(key)
        if note and not negative:
            app = "notepad"
            sp.getoutput(app)
        elif chm and not negative:
            app = "chrome"
            sp.getoutput("start chrome")
        elif spoti and not negative:
            app = "Spotify"
            sp.getoutput(app)
        elif txt and not negative:#send instanly
            st.markdown('<div class="title">WhatsApp Message Sender</div>', unsafe_allow_html=True)

            # State initialization
            if "ai" not in st.session_state:
                st.session_state.ai = False
            if "text_send" not in st.session_state:
                st.session_state.text_send = None
            if "text_pressed" not in st.session_state:
                st.session_state.text_pressed = False

            person = st.text_input("Enter the number of the person (with country code):")
            hrs = st.number_input("Enter the hours:", min_value=0, max_value=23, step=1)
            mins = st.number_input("Enter the minutes:", min_value=0, max_value=59, step=1)
            time_delay = st.number_input("Enter time delay (seconds):", min_value=0, step=1)
            use_ai_text = st.selectbox("Do you want AI-generated text?", ["No", "Yes"])

            if use_ai_text == 'Yes':
                st.session_state.ai = True
                if st.session_state.ai and st.session_state.text_send is None:
                    from Ggle import gemini
                    st.session_state.text_send = gemini("You are a professional text typer who writes precise and to the point texts:")
                st.write(st.session_state.text_send)
            else:
                st.session_state.ai = False

            if st.session_state.ai:
                if st.button("Send AI Generated Text", key="send_ai"):
                    st.session_state.text_pressed = True
                    if st.session_state.text_pressed:
                        from Text import whatsapp
                        whatsapp(person, st.session_state.text_send, hrs, mins, time_delay)
            else:
                message = st.text_area("Enter your text:")
                if st.button("Send Text", key="send_text"):
                    st.session_state.text_pressed = True
                    if st.session_state.text_pressed:
                        from Text import whatsapp
                        whatsapp(person, message, hrs, mins, time_delay)
        elif webs and not negative:
            with st.form(key="web"):
                site = st.text_input("Enter URL:")
                search = st.form_submit_button(label="Search")
            if search:
                web.open_new_tab(site)
        elif pic and not negative:
            st.markdown('<div class="title">Photo Options</div>', unsafe_allow_html=True)
            with st.form("photo_form"):
                photo_name = st.text_input("Enter name for the photo:")
                res = st.text_input("Do you want to save the photo (Yes/No)?:")
                if res == "Yes":
                    file_name = st.text_input("Enter file name (save it under \".png\" ):")
                else:
                    file_name = "NA"
                choice = st.number_input("Options: 1 for single photo, 2 for photo in photo, 3 for shades on a photo, 4 for exit\nEnter your choice:", min_value=1, max_value=4)
                filt = st.text_input("Do you wanna apply a black filter:(Y/N)")
                submitted = st.form_submit_button("Submit")

                if submitted:
                    if choice == 1:
                        from Camera import takephoto
                        takephoto(file_name, photo_name, res, filt)
                        st.success("Photo taken successfully!")
                    elif choice == 2:
                        from Camera import cropPhoto
                        cropPhoto(file_name, photo_name)
                        st.success("Photo cropped successfully!")
                    elif choice == 3:
                        from Camera import shade_on
                        shade_on(photo_name)
                        st.success("Shade applied successfully!")
                    else:
                        st.write("Ok")
        elif collage_pht and not negative:
            with st.form(key="Collage"):
                m = int(st.number_input("Enter 0 for internal camera:", min_value=0, max_value=1))
                n = int(st.number_input("Enter 1 for 1st external camera or 2 for 2nd internal camera:", min_value=1, max_value=2))
                search = st.form_submit_button(label="Create")
            if search:
                from Camera import photo_collage
                photo_collage(m, n)
        elif gen_photo and not negative:
            st.write("Generating a photo")
            from CompFeatures import generate_photo
            generate_photo()
        elif coordi and not negative:#add root for a different location
            from Location import get_location
            lat, lng, loc_name = get_location()
            st.write(f"Coordinates: {lat}, {lng}")
            st.write(f"Location Name: {loc_name}")
        elif mail and not negative:
            from Mail import send_mail
            sender = st.text_input("Enter the email from which you are gonna send the mail:")
            password = st.text_input("Enter its password:", type="password")
            receiver = st.text_input("Enter the email to which you are gonna send the mail:")
            subject = st.text_input("Enter the subject of the mail:\n")
            bd = st.text_input("Want Gemini to write the mail for you (Y/N):")
            if bd == 'Y':
                from Ggle import gemini
                body = gemini("You are a professional mail writer")
            else:
                body = st.text_input("Enter the body of the mail:\n")
            if "email_pressed" not in st.session_state:
                st.session_state.email_pressed = False
            if st.button("Send Mail", key="send_mail"):
                st.session_state.email_pressed = True
            if st.session_state.email_pressed:
                send_mail(sender, receiver, password, subject, body)
        elif bulk and not negative:
            li = st.text_input("Enter the list of mail ids:")
            sender = st.text_input("Enter the email from which you are gonna send the mail:")
            password = st.text_input("Enter its password:", type="password")
            subject = st.text_input("Enter the subject of the mail:\n")
            bd = st.text_input("Want Gemini to write the mail for you (Y/N):")

            if bd == 'Y':
                from Ggle import gemini
                body = gemini("You are a professional mail writer")
            else:
                body = st.text_input("Enter the body of the mail:\n")
            if "mail_pressed" not in st.session_state:
                st.session_state.mail_pressed = False
            if st.button("Send Bulk Mail", key="send_bulk"):
                st.session_state.mail_pressed = True
            if st.session_state.mail_pressed:
                from Mail import send_bulk
                send_bulk(li, sender, password, subject, body)
        elif vdo and not negative:
            with st.form(key="video"):
                name = st.text_input("Enter video name:")
                choice = st.text_input("Do you want video in video (Yes/No):")
                shoot = st.form_submit_button(label="Shoot")
            if shoot:
                if choice == "Yes":
                    from Camera import video_in_video
                    video_in_video()
                else:
                    from Camera import take_video
                    take_video(name)
        elif vol and not negative:
            with st.form(key="Volume"):
                vol = st.number_input("At what level do you want to set your volume:", min_value=0, max_value=100)
                set = st.form_submit_button(label="Set")
            if set:
                from CompFeatures import set_volume
                set_volume(int(vol))
        elif spch and not negative:
            from CompFeatures import text_to_speech
            text_to_speech()
        elif Ggl and not negative:
            with st.form(key="Google"):
                query = st.text_input("Enter the search query:")
                Google = st.form_submit_button(label="Google")
            if Google:
                from Ggle import google
                google(query)
        elif gemi and not negative:
            sys_role = st.text_input("Enter your instructions for the system:")
            if "Button_pressed" not in st.session_state:
                st.session_state.Button_pressed = False
            if st.button("Start", key="start"):
                st.session_state.Button_pressed = True
            if st.session_state.Button_pressed:
                from Ggle import gemini
                gemini(sys_role)
        elif Sms and not negative:
            api_key = "7f3327a40519291bd36576593bc4417bedbc9542"
            device_id = "00000000-0000-0000-9954-493415ef70b1"
            with st.form(key="sent"):
                number = st.text_input("Enter the number of the person you wanna send your SMS to (along with country code):")
                text = st.text_input("Enter the message you want to send:")
                sent = st.form_submit_button(label="Send")
            if sent:
                from Text import send_sms
                sent = send_sms(api_key, device_id, number, text)
                st.write(sent)
        elif ToDo and not negative:
            run = True
            client = mg.MongoClient("mongodb://localhost:27017/")
            db = client["To-Do-List"]
            col_list = db.list_collection_names()
            st.write(db.list_collection_names())
            for i in col_list:
                st.write(i)
            name = st.text_input("Enter the name of your list")
            st.write("Welcome to PYToDo-List\n Things you can do in this app:\n1.Enter a task\n2.Mark a task as done\n3.See all your tasks\n4.Mark a task as undone\n5.Delete a task")
            from CompFeatures import to_do_list
            choice = int(st.number_input("Enter your choice:"))
            if choice:
                to_do_list(name, choice)
        elif mach and not negative:
            with st.form(key="sent"):
                query = int(st.number_input("Enter your Body Fat percentage:"))
                predict = st.form_submit_button(label="Predict")
            if predict:
                from MachineLearning import machine_learning
                machine_learning(query)
        elif gam and not negative:
            from CompFeatures import random_number_game
            random_number_game()
        elif logistic and not negative:
            from MachineLearning import Log_reg
            Log_reg()
        elif negative:
            st.write("Ok")

st.markdown('<div class="title">Your Assistant</div>', unsafe_allow_html=True)
activate_text = st.text_input("Enter wake up phrase (e.g., hey zara):")
if activate_text.lower() == "hey zara":
    shut_down = voice_assistant(1)
