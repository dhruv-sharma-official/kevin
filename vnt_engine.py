import urllib.request
import pyttsx3
import speech_recognition as sr
from vosk import Model,KaldiRecognizer
import pyaudio
import os

# mainengine
path = os.getcwd()
engine = pyttsx3.init('sapi5')  # defining engine with sapi5
voices = engine.getProperty('voices')  # getting property to speak
rate = engine.getProperty('rate')  # getting property to control voice rate
engine.setProperty('voice', voices[0].id)  # setting voice id
engine.setProperty('rate', 130)  # setting voice rate

def speak(audio):  # defining speak function
    engine.say(audio)
    engine.runAndWait()
    # print(audio)


def check_internet_connection():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False

#### normal function for user voice
def takecmd():
    ret = ':'
    if check_internet_connection():
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
            # listen for the first phrase and extract it into audio data
            print('Online and listening...')
            r.pause_threshold = 1
            audio = r.listen(source, phrase_time_limit=5)
        try: 
            # recognize speech using Google Speech Recognition
            # print("You said " + r.recognize_google(audio, language='en-in'))
            ret = r.recognize_google(audio, language='en-in')

        except Exception as e:                            # speech is unintelligible
            print("Listening Failed, Say again..")
            ret = ":"
    else:
        a = 0
        print("local but listening...")
        model = Model(f"{path}\\Voice model\\vosk-model-small-en-us-0.15")
        recognizer = KaldiRecognizer(model, 16000)

        mic = pyaudio.PyAudio()
        stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
        stream.start_stream()

        while a < 50:
            data = stream.read(4096)
            if len(data) == 0:
                print("mic not working")

            if recognizer.AcceptWaveform(data):
                ret = recognizer.Result()
                print(f'User :{ret}')
            a+=1
    return ret
# speak('how are you sir')
# while True:
#     print(takecmd())

# speak("call is connected")


    
