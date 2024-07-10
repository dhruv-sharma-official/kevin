## outsource imports
import os


import datetime
import speech_recognition as sr
import googlesearch
from googlesearch import search
import audioplay
# import psutil
## supportive imports
import vnt_engine
import hardware_control 
import searchall
from vosk import Model,KaldiRecognizer
import pyaudio



path = os.getcwd()
#### all imported modules  ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
### master name
name = {
    'me':'kevin',
    'user':'Dhruv',
}

# defining local database
localdata = {
    'father':{'name':'ajay kumar sharma','dob':'01/07/1969','occupation':'reservation supervisor'},
    'mother':{'name':'pratibha sharma','dob':'01/07/1969','occupation':'clerk in saraswati mandir'}
}

def numfind(inp):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    find = False
    num = ""
    for i in inp:
        if i in numbers:
            num += i
            find = True
    if find == True:
        return int(num)
    else:
        return inp  
                
### defining needed functioning lists  ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
time = [datetime.datetime.now().hour, datetime.datetime.now().minute]
noonGreet = ['Good Morning', 'Good Afternoon', 'Good Evening', 'Good Night']
friendGreet = ['Hi', 'Hello']
elderGreet = ['namastey','pranaam','dhoag']
bhaktiGreet = ['jai shree ram','ram ram','jai siya ram','radhe radhe']
Months = ['January', 'February', 'March', 'April', 'May', 'june','July', 'August', 'September', 'October', 'November', 'December']
usergreet = ['how are you','whats up', 'hey buddy','whats going on', 'are you fine','you okay','Good Morning', 'Good Afternoon', 'Good Evening', 'Good Night']  

# defining quick use functions  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def speak(audio_file):  # defining speak function
    vnt_engine.speak(audio_file)
    print(audio_file)
    
# def takecmd():
#     inp = input('command here:')
#     return inp
def takecmd():         ## user voice input
    try:
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
    except:
        print("offline but listening...")
        model = Model(f"{path}\\Voice model\\vosk-model-small-en-us-0.15")
        recognizer = KaldiRecognizer(model, 16000)

        mic = pyaudio.PyAudio()
        stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
        stream.start_stream()

        while True:
            data = stream.read(4096)
            if len(data) == 0:
                print("mic not working")
                break
            if recognizer.AcceptWaveform(data):
                ret = recognizer.Result()
                print(f'User :{ret}')
    return ret

def noonTime():
    try:
        if time[0] >= 00 and time[0] < 12:
            return noonGreet[0]
        elif time[0] >= 12 and time[0] < 15:
            return noonGreet[1]
        elif time[0] >= 15 or time[0] < 00:
            return noonGreet[2]
    except Exception as e:
        return friendGreet[1]

def greet():
    speak(f'{noonTime()} {name["user"]}, the time is {time[0]} hours {time[1]} minutes')
    
    
def onStart():
    greet()
    if hardware_control.hardinfo.battery.charge() <= 50:
        hardware_control.adjust.brightness(60)
        speak('brightness level is initiated to 60 percent as the battery is less than 50')
    elif hardware_control.hardinfo.battery.charge() >= 51 and hardware_control.hardinfo.battery.charge() <= 80:
        hardware_control.adjust.brightness(70)
        speak('brightness level is initiated to 70 percent as the battery is less than 80')
    elif hardware_control.hardinfo.battery.charge() >= 81 and hardware_control.hardinfo.battery.charge() <= 100:
        hardware_control.adjust.brightness(80)
        speak('brightness level is initiated to 80 percent as the battery is more than 80')
    speak('all systems configured and online')

rec = {
    "greet":["hello","hi","hey"],
    'question':['what','why','where','how','when','whom','which','who'],
    'ask':['tell me','let me know','speak'],
    'order':['do','adjust','search'],
    'quantity':['much','many'],
}

def lister(inp):
    a = 0
    b = 0
    words = []
    strin = ''
    inp = inp + ' '                   ## adding extra space to inset last word
    for i in range(len(inp)):          ## for loop to repeat code according to input length
        if inp[a] == " ":              ## saparating words using spaces bwn them
            b = b+1                     ## changing value of b to saparate one word from another
            words.insert(b, strin)      ## inserting value inside strin in list
            strin = ''                  ## deleting previous string so that new one can be inserted
        else:
            strin = strin + inp[a]     ## storing characters one by one inside a variable
        a = a +1                        ## changing index value of user slices to take every char saparetly  ## changing value of a so that next character could be readed
    return words

def recognize(cmd):
    print(cmd)
    if ((f'{name["me"]}') or (f'hi {name["me"]}')) in cmd:                   ## recognizes user when he says hey
        speak('yes boss, I am Listening')
    if cmd in usergreet:                            ### greets user according to user greeting
        if cmd in noonGreet:
            if time[0] < 15 and time[0] > 00:
                speak(f'{noonTime}, today is a great day to do something, so whats the new plans for today')
            elif time[0] > 15 and time[0] < 20:
                speak(f'{noonTime}, we have still some remaining hours of today, so whats the plans')
            else:
                speak(f'{noonTime}, today was a great day as expected, with some sweet and bitter moments, so we will still work or you are going to sleep')
                cmd = takecmd().lower()
                if ('we will work' or 'work' or 'some tasks left' or 'pending work') in cmd:
                    speak('okay sir let me know if you need some help')
        speak('absolutely fine sir, all functions are performing pretty well, how about you')
        gcmd = takecmd().lower()
        if ('I am fine' or 'absolutly fine' or 'fabulus') in gcmd:
            speak('thats nice to here, so whats the new plans for today')
            g2cmd = takecmd().lower()
            if ('free today' or 'no tasks' or 'relaxing' or 'tired') in g2cmd:
                speak('I think listening some music is better')
                g3cmd = takecmd().lower()
                if ('okay' or 'play some music' or 'play music') in g3cmd:
                    audioplay.music()
                else:
                    speak('okay sir, let me know if you need some help')
        if 'not fine' or 'in trouble' or 'need help' in gcmd:
            speak('let me know if you need some help')
    if ('turn off yourself' or 'bye') in cmd:          ## turn itself off
        speak("{'okay, let me know if you need help")
        exit()
    if ('tell me the time' or 'whats the time now' or 'speak time') in cmd: ## tells user exact time
        speak(f'sir, the time is {time[0]} hours {time[1]} minutes')
        print(f"Time: {time[0]}:{time[1]}")
    if 'command override' in cmd:                             ### overriding method
        speak('override accepted, voice command activated')
    if 'who is' in cmd or 'who were' in cmd:                 ## tells info about someone
        if 'who is' in cmd:
            cmd.replace('who is','')
            searchall.search.wiki(cmd)
        elif 'who were' in cmd:
            cmd.replace('who were','')
            searchall.search.wiki(cmd)
    if 'how much battery is left' in cmd:         ## tells about battery level
        speak(f'sir battery is {hardware_control.hardinfo.battery.charge()} percent left')
    if 'adjust'and'brightness' in cmd or 'increase'and'brightness' in cmd or 'decrease'and'brightness' in cmd:              ## adjusts brightness with levels from 1 to 10
        percent = False
        level = False
        if ('percent' in cmd or '%' in cmd):
            percent = True
        if ('level' in cmd):
            level = True
        # bri = cmd.replace('adjust brightness at level','')

        try:
            if percent == True:
                bri = numfind(cmd)
                hardware_control.adjust.brightness(bri ,'percent')
                
            if level == True:
                bri = numfind(cmd) * 10
                hardware_control.adjust.brightness(bri ,'level')
                
            else:
                if 'ten' in bri:
                    bri = 10
                else:
                    bri = numfind(cmd)
                num = bri * 10
                hardware_control.adjust.brightness(num,'level')
        except Exception as e:
            speak("I don't understand on which level you want me to adjust the brightness")
        
    if ('search about' or 'search' in cmd):
        if 'search about' in cmd:
            s = cmd.replace('search about ','')
            # to search
            searchall.search.web.gsearch(s)
            speak(f"here are the search results of {s}")
        elif 'show image of' or 'search image of' in cmd:
            if 'search image of' in cmd:
                s = cmd.replace('search image of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
            elif 'show image of' in cmd:
                s = cmd.replace('show image of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")

        elif 'show images of' or 'search images of' in cmd:
            if 'search images of' in cmd:
                s = cmd.replace('search images of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
            elif 'show images of' in cmd:
                s = cmd.replace('show images of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
        elif 'search' in cmd:
            s = cmd.replace('search ','')
            searchall.search.web.directsearch(s)
            speak(f"here are the search results of {s}")
            
    if ('search image of' in cmd):
        if 'search about' in cmd:
            s = cmd.replace('search about ','')
            # to search
            searchall.search.web.gsearch(s)
            speak(f"here are the search results of {s}")
        elif 'show image of' or 'search image of' in cmd:
            if 'search image of' in cmd:
                s = cmd.replace('search image of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
            elif 'show image of' in cmd:
                s = cmd.replace('show image of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")

        elif 'show images of' or 'search images of' in cmd:
            if 'search images of' in cmd:
                s = cmd.replace('search images of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
            elif 'show images of' in cmd:
                s = cmd.replace('show images of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
        elif 'search' in cmd:
            s = cmd.replace('search ','')
            searchall.search.web.directsearch(s)
            speak(f"here are the search results of {s}")
            
    if ('search images of' in cmd):
        if 'search about' in cmd:
            s = cmd.replace('search about ','')
            # to search
            searchall.search.web.gsearch(s)
            speak(f"here are the search results of {s}")
        elif 'show image of' or 'search image of' in cmd:
            if 'search image of' in cmd:
                s = cmd.replace('search image of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
            elif 'show image of' in cmd:
                s = cmd.replace('show image of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")

        elif 'show images of' or 'search images of' in cmd:
            if 'search images of' in cmd:
                s = cmd.replace('search images of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
            elif 'show images of' in cmd:
                s = cmd.replace('show images of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
        elif 'search' in cmd:
            s = cmd.replace('search ','')
            searchall.search.web.directsearch(s)
            speak(f"here are the search results of {s}")
            
    if ('show image of' in cmd):
        if 'search about' in cmd:
            s = cmd.replace('search about ','')
            # to search
            searchall.search.web.gsearch(s)
            speak(f"here are the search results of {s}")
        elif 'show image of' or 'search image of' in cmd:
            if 'search image of' in cmd:
                s = cmd.replace('search image of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
            elif 'show image of' in cmd:
                s = cmd.replace('show image of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
        elif 'show images of' or 'search images of' in cmd:
            if 'search images of' in cmd:
                s = cmd.replace('search images of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
            elif 'show images of' in cmd:
                s = cmd.replace('show images of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
        elif 'search' in cmd:
            s = cmd.replace('search ','')
            searchall.search.web.directsearch(s)
            speak(f"here are the search results of {s}")
            
    if ('show images of' in cmd):        ## search 
        if 'search about' in cmd:
            s = cmd.replace('search about ','')
            # to search
            searchall.search.web.gsearch(s)
            speak(f"here are the search results of {s}")
        elif 'show image of' or 'search image of' in cmd:
            if 'search image of' in cmd:
                s = cmd.replace('search image of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
            elif 'show image of' in cmd:
                s = cmd.replace('show image of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")

        elif 'show images of' or 'search images of' in cmd:
            if 'search images of' in cmd:
                s = cmd.replace('search images of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
            elif 'show images of' in cmd:
                s = cmd.replace('show images of ','')
                searchall.search.web.images(s)
                speak(f"here are the search results of {s}")
        elif 'search' in cmd:
            s = cmd.replace('search ','')
            searchall.search.web.directsearch(s)
            speak(f"here are the search results of {s}")
        


#######                 we have to make a dictionary of meanings with the similar words of them to compare with the list we got

# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[  recognizing starts from here  ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
    

# old execution code
# if __name__ == "__main__": ## program execution starts from here ,, in breif __name__ = (value will be __main__ if the same file is executed, and if the file is imported into another file the value of __name__ will be the name of the current file) in simple words it will execute the code inside this statement if the same file is executed and if the file is imported in another file, then the code inside this statement will not be executed, because at that time the value of __name__ (system defined variable) will be the name of the current file (in case of import) but if the same file is executed then the value will be __main__

#     onStart()
#     while True:
#         # cmd = input('command from user: ')## takecmd().lower()
#         cmd = takecmd()
#         recognize(lister(cmd))

#         if (f'hey {name["me"]}') in cmd:                   ## recognizes user when he says hey
#             speak('yes boss, I am Listening')
#         if cmd in usergreet:                            ### greets user according to user greeting
#             if cmd in noonGreet:
#                 if time[0] < 15 and time[0] > 00:
#                     speak(f'{noonTime}, today is a great day to do something, so whats the new plans for today')
#                 elif time[0] > 15 and time[0] < 20:
#                     speak(f'{noonTime}, we have still some remaining hours of today, so whats the plans')
#                 else:
#                     speak(f'{noonTime}, today was a great day as expected, with some sweet and bitter moments, so we will still work or you are going to sleep')
#                     ncmd = takecmd().lower()
#                     if ('we will work' or 'work' or 'some tasks left' or 'pending work') in cmd:
#                         speak('okay sir let me know if you need some help')
#             speak('absolutely fine sir, all functions are performing pretty well, how about you')
#             gcmd = takecmd().lower()
#             if ('I am fine' or 'absolutly fine' or 'fabulus') in gcmd:
#                 speak('thats nice to here, so whats the new plans for today')
#                 g2cmd = takecmd().lower()
#                 if 'free today' or 'no tasks' or 'relaxing' or 'tired' in g2cmd:
#                     speak('I think listening some music is better')
#                     g3cmd = takecmd().lower()
#                     if 'okay' or 'play some music' or 'play music' in g3cmd:
#                         audioplay.music()
#                     else:
#                         speak('okay sir, let me know if you need some help')
#             if 'not fine' or 'in trouble' or 'need help' in gcmd:
#                 speak('let me know if you need some help')
#         if ('turn off yourself' or 'bye') in cmd:          ## turn itself off
#             speak("{'okay, let me know if you need help")
#             exit()
#         if ('tell me the time' or 'whats the time now' or 'speak time') in cmd: ## tells user exact time
#             speak(f'sir, the time is {time[0]} hours {time[1]} minutes')
#         if 'command override' in cmd:                             ### overriding method
#             speak('override accepted, voice command activated')
#         if ('who is' or 'who were') in cmd:                 ## tells info about someone
#             if 'who is' in cmd:
#                 cmd.replace('who is','')
#                 searchall.search.wiki(cmd)
#             elif 'who were' in cmd:
#                 cmd.replace('who were','')
#                 searchall.search.wiki(cmd)
#         if ('how much battery is left') in cmd:         ## tells about battery level
#             speak(f'sir battery is {hardware_control.hardinfo.battery.charge()} percent left')
#         if 'adjust brightness' in cmd:              ## adjusts brightness with levels from 1 to 10
#             bri = cmd.replace('adjust brightness at level','')
#             if 'ten' in bri:
#                 bri = 10
#             bri = int(bri)
#             def brig(num):
#                 num = num*10
#                 return num
#             num = brig(bri)
#             hardware_control.adjust.brightness(num)
#             speak(f'brightness level is adjusted at level {bri}')
#         if 'search about' or 'search' or 'search image of' or 'search images of' or 'show image of' or 'show images of' in cmd:        ## 
#             if 'search about' in cmd:
#                 s = cmd.replace('search about ','')
#                 # to search
#                 searchall.search.web.gsearch(s)
#                 speak(f"here are the search results of {s}")
#             elif 'show image of' or 'search image of' in cmd:
#                 if 'search image of' in cmd:
#                     s = cmd.replace('search image of ','')
#                     searchall.search.web.images(s)
#                     speak(f"here are the search results of {s}")
#                 elif 'show image of' in cmd:
#                     s = cmd.replace('show image of ','')
#                     searchall.search.web.images(s)
#                     speak(f"here are the search results of {s}")

#             elif 'show images of' or 'search images of' in cmd:
#                 if 'search images of' in cmd:
#                     s = cmd.replace('search images of ','')
#                     searchall.search.web.images(s)
#                     speak(f"here are the search results of {s}")
#                 elif 'show images of' in cmd:
#                     s = cmd.replace('show images of ','')
#                     searchall.search.web.images(s)
#                     speak(f"here are the search results of {s}")
#             elif 'search' in cmd:
#                 s = cmd.replace('search ','')
#                 searchall.search.web.directsearch(s)
#                 speak(f"here are the search results of {s}")
if __name__ == "__main__":
    print("checking successful all dependencies satisfied!")