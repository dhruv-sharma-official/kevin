from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime

flags = QtCore.QtWindowflags(QtCore.Qt.FrameslessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty()('voices')
engine.serproperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def speak(audio):
          engine.say(audio)
          engine.runAndWait()

def mainT(QThread):
        def __init__(self):
            super(mainT,self).__init__()
        @pyqtSlot
        def run(self):
            self.JARVIS()

        def STT(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:                # use the default microphone as the audio source
                print('online & listening...')
                r.pause_threshold = 1
                audio = r.listen(source, phrase_time_limit=5)
            try: 
                # recognize speech using Google Speech Recognition
                # print("You said " + r.recognize_google(audio, language='en-in'))
                ret = r.recognize_google(audio, language='en-in')
                print(f'User :{ret}')

            except Exception as e:                            # speech is unintelligible
                print("Listening Faild, say again:")
                return "none"
            return ret
        
        def JARVIS(self):
             
             while True:
                  self.query = self.STT()
                  print(self.query)






## gui starts from here

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
     def __init__(self,parent=None):
          super(Main,self).__init__(parent)
          self.setupUi(self)
          self
                 
        


