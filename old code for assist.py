

## old coad of assistant
'''
if f'hey {name["me"]}' in cmd:                           ## recognizes user when he 
        speak('yes boss, I am Listening')
    if cmd in usergreet:                            ### greets user according to user greeting
        speak('absolutely fine sir, all functions are performing pretty well, how about you')
        gcmd = takecmd().lower()
        if 'I am fine' or 'absolutly fine' or 'fabulus' in gcmd:
            speak('thats nice to here, so whats the new plans for today')
            g2cmd = takecmd().lower()
            if 'free today' or 'no tasks' or 'relaxing' or 'tired' in g2cmd:
                speak('I think listening some music is better')
                g3cmd = takecmd().lower()
                if 'okay' or 'play some music' or 'play music' in g3cmd:
                    audioplay.music()
                else:
                    speak('okay sir, let me know if you need some help')
        if 'not fine' or 'in trouble' or 'need help' in gcmd:
            speak('let me know if you need some help')
    if 'turn off yourself' or 'bye' in cmd:          ## turn itself off
        speak("{'okay, let me know if you need help")
        # exit()
    if 'code 10' in cmd:                             ### overriding method
        speak('override accepted')
    if 'who is' or 'who were' in cmd:                 ## tells info about someone
        if 'who is' in cmd:
            cmd.replace('who is','')
            searchall.search.wiki(cmd)
        elif 'who were' in cmd:
            cmd.replace('who were','')
            searchall.search.wiki(cmd)
    if ('how much battery is left') in cmd:         ## tells about battery level
        speak(f'sir battery is {hardware_control.hardinfo.battery.charge()} percent left')
    if 'adjust brightness' in cmd:              ## adjusts brightness with levels from 1 to 10
        bri = cmd.replace('adjust brightness at level','')
        if 'ten' in bri:
            bri = 10
        bri = int(bri)
        def brig(num):
            num = num*10
            return num
        num = brig(bri)
        hardware_control.adjust.brightness(num)
        speak(f'brightness level is adjusted at level {bri}')
    if 'search about' or 'search'or'search image of' or 'search images of' in cmd:        ## 
        if 'search about' in cmd:
            s = cmd.replace('search about ','')
            # to search
            searchall.search.web.gsearch(s)
            speak(f"here are the search results of {s}")
        elif 'search image of' or 'search images of' in cmd:
            s = cmd.replace('search image of ' or 'search images of','')
            searchall.search.web.images(s)
            speak(f"here are the search results of {s}")
        elif 'search images of' in cmd:
            s = cmd.replace('search images of','')
            searchall.search.web.images(s)
            speak(f"here are the search results of {s}")
        elif 'search' in cmd:
            s = cmd.replace('search ','')
            searchall.search.web.directsearch(s)
            speak(f"here are the search results of {s}")

'''