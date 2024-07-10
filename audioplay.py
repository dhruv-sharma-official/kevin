
# from playsound import playsound
import vnt_engine
import speech_recognition as sr
import os, fnmatch
import searchall

def speak(audio_file):
    vnt_engine.speak(audio_file)

def findit(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        # listen for the first phrase and extract it into audio data
        audio = r.listen(source)
    try: 
        # recognize speech using Google Speech Recognition
        # print("You said " + r.recognize_google(audio, language='en-in'))
        ret = r.recognize_google(audio, language='en-in')

    except Exception as e:                            # speech is unintelligible
        print("Could not understand audio")
        ret = "None"
    return ret

# def music():
#     speak('which music do you want to play')
#     mus = takecmd().lower()

#     if 'None' or 'none' or '[]' in str(findit(f'*{mus}*',f'{os.getcwd()}\\Music\\')):
#         speak("can't here it clearly, will you please try again")

#     else:
#         try:
#             song = str(findit(f'*{mus}*',f'{os.getcwd()}\\Music\\'))
#             str(song)
#             song = song.replace('[','')
#             song = song.replace(']','')
#             song = song.replace("'",'')
#             speak(f'okay sir playing {mus}')
#             # song = song.replace('\\\\','\\')
#             playsound(f'{song}')
#             print(str(song))
#         except Exception as e:
#             speak(f'sir {mus} is not in our playlist, would you like to play it online')
#             repl = takecmd().lower()
#             if 'okay' or 'sure' or 'yes' or 'play it' in repl:
#                 speak("searching")
#                 searchall.search.web.yt(mus)
#                 speak(f'here are some search results for {mus}')
#                 print(repl)
#             elif 'no' or "don't do that" or 'leave it' in repl:
#                 speak('okay sir, let me know if you need some more help')
    


# music()
# song = str(findit(f'*{}*', f'{os.getcwd()}/Music/'))
# print(song.replace('[' and ']', ''))


# def find_all(name, path):
#     result = []
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             result.append(os.path.join(root, name))
#     return result

# def find(name, path):   
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             print('ok')
#             return os.path.join(root, name)
# print(find('Musafir*', 'D:\\Code\\Music\\'))
# mus = 'listen'
# print(str(findit(f'*{mus}*',f'{os.getcwd()}\\Music\\')))
# playsound('D:\\Code\\Music\\Just Listen - Sidhu Moose Wala (Slowed & Reverb).mp3')
# mus = 'listen'
# song = str(findit(f'*{mus}*',f'{os.getcwd()}\\Music\\'))
# song = str(song)
# song.replace(song[0],'')
# song.replace(song[1],'')
# song.replace(song[-1],'')
# song.replace(song[-2],'')
# song.replace('\\\\','\\')
# # playsound(f'{song}')
# f = open('D:\\Code\\file.txt', 'r+')
# # f.write(song)
# song2 = f.readline()
# f.close()
# song2 = "['D:\\Code\\Musafir.mp3']"
# song2 = song2.replace('D','')
# song2.replace(']','')
# song2.replace("'",'')

# print(type(song2))
# print(song2)