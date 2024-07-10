import vnt_engine
import wikipedia
import os
from googlesearch import search
def speak(audio_file):
    vnt_engine.speak(audio_file)


class search():
    def wiki(cmd):
        speak('Searching Wikipedia...')
        cmd = cmd.replace("who is", "")
        try:
            results = wikipedia.summary(cmd, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        except Exception as e:
            print("not found on wikipedia")
            speak(f'nothing found about {cmd}')
            
    class web():
        def gsearch(string):
            s = str(string)
            s = s.replace(' ','+')
            os.system(f'start chrome "https://www.google.com/search?q={s}" -incognito')
        def directsearch(string):
            s = str(string)
            s = s.replace(' ','+')
            if '.com' or '.in' or '.org' in string:
                os.system(f'start chrome "https://www.google.com/search?q={s}" -incognito')
            else:
                os.system(f'start chrome "https://www.google.com/search?q={s}"')
        def images(string):
            s = str(string)
            s = s.replace(' ','+')
            os.system(f'start chrome "https://www.google.com/search?q={s}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiBgf7Dnrb8AhWxTmwGHTCWCxMQ_AUoAnoECAEQBA&biw=1920&bih=93" -incognito')
        def yt(query):
            os.system(f'start chrome "https://www.youtube.com/results?search_query={query}" -incognito')

            
    def localSearch():
        os.system('localdata.exe')












