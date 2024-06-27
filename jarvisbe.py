import time
import pyautogui
import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import sipbuild
import os
import cv2
import random
import wikipedia
from requests import get
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import requests
from PyQt5.QtCore import QThread
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from PyQt5.QtCore import QThread
import numpy
import sipbuild
import instaloader
import PyPDF2
from PyQt5 import  QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui import Ui_MainWindow
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()
# To convert voice to text
    def takecommand(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listneing...")
                r.pause_threshold = 1
                audio = r.listen(source, timeout=0, phrase_time_limit=4)

            try:
                print("Recognizing..")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}")
            except Exception as e:
                speak("say that again please")
                return "none"
            return query

    def TaskExecution(self):
            wish()
            while True:
                # if 1:
                self.query = self.takecommand()

                # logic building for task

                if "open notepad" in query:
                    npath = "C:\\Windows\\notepad.exe"
                    os.startfile(npath)

                elif "open chrome" in query:
                    apath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(apath)

                elif "open command prompt" in self.query:
                    os.system("Start cmd")

                elif "open camera" in self.query:
                    cap = cv2.VideoCapture(0)

                    while True:
                        ret, img = cap.read()
                        cv2.imshow('Webcam', img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break;
                    cap.release()
                    cv2.destroyAllWindows()

                elif "play music" in self.query:
                    music_dir = "D:\\Music"
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    '''for song in songs:
                        if song.endswith('.mp3'):'''
                    os.startfile(os.path.join(music_dir, rd))

                elif "open netflix" in self.query:
                    speak("opening Netflix")
                    webbrowser.open("https://www.netflix.com/browse")

                elif "open prime video" in self.query:
                    speak("opening Amazon prime")
                    webbrowser.open("https://www.primevideo.com/offers/nonprimehomepage/ref=dv_web_force_root")

                elif "tell me ip address" in self.query:
                    ip = get('https://api.ipify.org').text
                    speak(f'your IP address is {ip}')

                elif "wikipedia" in self.query:
                    speak("Searching Wikipedia..")
                    query = query.replace("Wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("according to Wikipedia...")
                    speak(results)


                elif "open youtube" in self.query:
                    webbrowser.open("youtube.com")

                elif "open spotify" in self.query:
                    webbrowser.open("https://open.spotify.com/")

                elif "open whatsapp" in self.query:
                    webbrowser.open("https://web.whatsapp.com/")

                elif "open google" in self.query:
                    speak("Sir,what should I search on Google")
                    cm = self.takecommand()
                    webbrowser.open(f"{cm}")

                elif "bring me food" in query or "order me something" in query:
                    speak("what you want to eat")
                    food = self.takecommand()
                    webbrowser.open("https://www.zomato.com/india")

                elif "send message" in query:
                    kit.sendwhatmsg("+917024262515", "oye gadhi", 18, 40)

                elif "play song on youtube" in self.query:
                    kit.playonyt("mahabali maharudra")

                elif "send image" in self.query:
                    kit.sendwhats_image("+917024262515", "D:\\IMG_20230111_222329.jpg")

                elif "you can sleep now" in self.query:
                    speak("Thanks for using me sir, have a good day.")
                    sys.exit()

                elif "i want to buy something" in self.query:
                    speak("from which site you want to purchase")

                elif "can you get me girlfriend" in self.query:
                    speak("I am not a broker anna go and find yourself")

                elif "who are you" in self.query:
                    speak("I am a AI bot who is capable of doing many task")

                elif "who made you" in self.query:
                    speak("I am made by students of CSIT")

                elif "from amazon" in self.query:
                    webbrowser.open("amazon.in")

                elif "from flipkart" in self.query:
                    webbrowser.open("https://www.flipkart.com/")

                elif "are you deaf" in self.query:
                    speak("No i am not a deaf bot you are not talking clearly to me")

                elif "can you talk in hindi" in self.query:
                    speak("recently i can talk only in english, sorry for your inconvinience i will be better next time ")


                # to set an alarm
                elif "set alarm" in self.query:
                    nn = int(datetime.datetime.now().hour)
                    if nn == 23:
                        music_dir = 'D:\Music'
                        songs = os.listdir(music_dir)
                        os.startfile(os.path.join(music_dir, songs[0]))

                # for jokes
                elif "tell me joke" in self.query:
                    joke = pyjokes.get_joke()
                    speak(joke)

                elif "shut down the system" in self.query:
                    os.system("shutdown /s /t 5")

                elif "restart the system" in self.query:
                    os.system("shutdown /r /t 5")

                elif "Sleep the system" in self.query:
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


                # window switch
                elif "switch the window" in self.query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                # finding location
                elif "where we are" in self.query:
                    speak("wait sir, let me check")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text
                        print(ipAdd)
                        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        # print geodata
                        city = geo_data['city']
                        # state = geo_data['state']
                        country = geo_data['country']
                        speak(f"Sir i am not sure, but i think we are in  {city} city of {country} country")
                    except Exception as e:
                        speak("sorry sir,due to network issue i am not able to find where we are.")
                        pass
                # to download instagram profile and search profile
                elif "instagram profile" in self.query or "profile on instagram" in self.query:
                    speak("sir please write the username correctly.")
                    name = input("Enter username here:")
                    webbrowser.open(f"www.instagram.com/{name}")
                    speak(f"sir here is the profile of the user {name}")
                    time.sleep(5)
                    speak("sir do you want to download profile picture of this id.")
                    condition = self.takecommand()
                    if "yes" in condition:
                        mod = instaloader.Instaloader()
                        mod.download_profile(name, profile_pic_only=True)
                        speak("i am done sir, profile picture is downloaded in your main file")
                    else:
                        pass

                # ......to take screenshot......
                elif "take screenshot" in self.query or "take a screenshot" in self.query:
                    speak("sir please tell me the name for this screenshot file")
                    name = self.takecommand()
                    speak("please sir hold the screen for few seconds, i am taking screenshot")
                    time.sleep(5)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("i am done sir, screenshot has taken")

                # read pdf
                elif "read pdf" in self.query:
                    pdf_reader()

                elif "thankyou" in self.query:
                    speak("It's my pleasure sir")

                # hiding folder
                elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                    speak("sir please tell me you want to hide this folder or make it visible for everyone")
                    condition = self.takecommand()
                    if "hide" in condition:
                        os.system("attrib +h /s /d")  # os module
                        speak("sir all the files in this folder are now hidden.")

                    elif "visible" in condition:
                        os.system("attrib -h /s /d")
                        speak("sir, all the files in this folder are now visible to everyone.")

                    elif "leave it" in condition or "leave for now" in condition:
                        speak("okay sir")
            pass

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning sir")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("I am Your buddy . please tell me how can I help you")


# pdf reader
def pdf_reader():
    book = open('E:\\College Notes\\5th  sem\\computer graphics\\BSP tree.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book is {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie =QtGui.QMovie("7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("62ac986e15368359793aa49a_ezgif.com-gif-maker (57).gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time =QTime.currentTime()
        current_date =QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())