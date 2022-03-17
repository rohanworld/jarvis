import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

print("Welcome Mr.Stark")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Mr.Stark")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Mr.Stark")
    else:
        speak("Good Evening Mr.Stark")
    speak("I am Jarvis, at your service sir")
    speak("Type Below what you want me to do")


def conv(inp):
    return inp.lower()


def takeCommand():
    while True:
        userInp = input("Rohan: ")
        ans = conv(userInp)
        if 'wiki' in ans or 'wikipedia' in ans:
            try:
                ans = ans.replace("wiki", "")
                speak("Searching Wikipedia...")
                wikiResult = wikipedia.summary(ans, sentences=3)
                speak("According to Wikipedia, ")
                speak(wikiResult)
            except Exception as e:
                speak("Sorry Sir, I cant reach wikipedia at the moment")
        elif 'search fb' in ans or 'search facebook' in ans or 'searchfacebook' in ans or 'searchfb' in ans:
            try:
                ans = ans.replace("search fb", "")
                ans = ans.replace("searchfb", "")
                ans = ans.replace("search facebook", "")
                ans = ans.replace("searchfacebook", "")
                webbrowser.open_new_tab(
                    f"https://www.facebook.com/search/top/?q={ans}")
                speak(f"Searching Facebook for the username{ans}...")
            except Exception as e:
                speak("Sorry Sir, I cant reach facebook at the moment")
        elif 'open youtube' in ans:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Opening YouTube...")
        elif 'open zerodha' in ans or 'open kite' in ans or 'zerodha' in ans or 'kite' in ans or 'invest' in ans or 'market' in ans:
            webbrowser.open_new_tab("https://kite.zerodha.com/")
            speak("Opening your Investment Portal...")
        elif 'open fb' in ans or 'open facebook' in ans or 'fb' in ans:
            webbrowser.open_new_tab("https://www.fb.com")
            speak("Opening FaceBook...")
        elif 'open insta' in ans or 'open instagram' in ans or 'openig' in ans:
            webbrowser.open_new_tab("https://www.instagram.com")
            speak("Opening Instagram...")
        elif 'open google' in ans:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Opening Google...")
        elif 'google' in ans:
            ans = ans.replace("google", "")
            webbrowser.open_new_tab(
                f"https://www.google.com/search?q={ans}&oq={ans}&aqs=chrome..69i57j35i39i362l6j69i59j35i39l2.700j0j15&sourceid=chrome&ie=UTF-8")
            speak(f"Searching for {ans} in Google ...")
        elif 'searchyt' in ans or 'search youtube' in ans or 'search yt' in ans:
            ans = ans.replace("search youtube", "")
            ans = ans.replace("searchyt", "")
            ans = ans.replace("search yt", "")
            webbrowser.open_new_tab(
                f"https://www.youtube.com/results?search_query={ans}")
            speak(f"Searching for {ans} in YouTube ...")

        elif 'open stackoverflow' in ans or 'stackoverflow' in ans or 'sf' in ans:
            webbrowser.open_new_tab("https://www.stackoverflow.com")
            speak("Opening StackOverflow...")
        elif 'open github' in ans or 'github' in ans:
            webbrowser.open_new_tab("https://www.github.com")
            speak("Opening GitHub...")
        elif 'open whatsapp' in ans or 'whatsapp' in ans or 'whatsapp web' in ans:
            webbrowser.open_new_tab("https://web.whatsapp.com")
            speak("Opening WhatsApp web...")
        elif 'play' in ans or 'music' in ans:
            webbrowser.open_new_tab(
                "https://www.youtube.com/watch?v=aWPrqvwBjko&list=RDaWPrqvwBjko&start_radio=1")
            speak("Playing Song on youtube...")
        elif 'song' in ans:
            song_dir = 'D:\\SONGS'
            songs = os.listdir(song_dir)
            ans = ans.replace("song", "")
            os.startfile(os.path.join(song_dir, songs[int(ans)]))
            speak("Playing Song...")
        elif 'video' in ans:
            vid_dir = 'D:\\VIDEOS'
            vids = os.listdir(vid_dir)
            ans = ans.replace("video", "")
            os.startfile(os.path.join(vid_dir, vids[int(ans)]))
            speak("Playing Video on VLC Player now...")
        elif 'movie' in ans or 'kannada' in ans:
            kmov_dir = 'D:\\MOVIES\\KANNADA'
            kmovs = os.listdir(kmov_dir)
            ans = ans.replace("kannada", "")
            os.startfile(os.path.join(kmov_dir, kmovs[int(ans)]))
            speak("Playing Kannada Movie on VLC Player now...")
        elif 'hindi' in ans:
            hmov_dir = 'D:\\MOVIES\\HINDHI'
            hmovs = os.listdir(hmov_dir)
            ans = ans.replace("hindi", "")
            ans = ans.replace("hindhi", "")
            os.startfile(os.path.join(hmov_dir, hmovs[int(ans)]))
            speak("Playing Hindhi Movie on VLC Player now...")
        elif 'maja' in ans or 'talkies' in ans:
            maja_dir = 'D:\\MOVIES\\MAJA TALKIES'
            majas = os.listdir(maja_dir)
            ans = ans.replace("maja", "")
            ans = ans.replace("talkies", "")
            os.startfile(os.path.join(maja_dir, majas[int(ans)]))
            speak("Playing Maja Talkies on VLC Player now...")
        elif 'time' in ans:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Current Time is: {strTime}")
        elif 'exit' in ans or 'close' in ans or 'powerdown' in ans or 'shutdown' in ans or 'shut' in ans:
            speak("Shutting Down...")
            print("Jarvis - Power Down")
            return
        else:
            speak("I am Afraid, Mr.Stark. I cant process that request")


if __name__ == "__main__":
    wishMe()
    takeCommand()
