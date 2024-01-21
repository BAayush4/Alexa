import pyautogui
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import imdb
import requests
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("GOOD MORNING sir")
    elif(hour>=12 and hour<18):
        speak("GOOD AFTERNOON sir")
    else:
        speak("GOOD EVENING sir")
    speak("I am ALEXA, please tell me how may i help you")
def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("bauraiayush733@gmail.com","tuym duso zebu imwh")
    server.sendmail("bauraiayush733@gmail.com",to,content)
    server.close()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.phrase_threshold=0.4
        #r.energy_threshold=300
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please..")
        return "None"
    return query
wishme()
#takeCommand()
while True:
    query=takeCommand().lower()
    if 'wikipedia' in query:
        speak('searching wikipedia sir..')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=5)
        speak("according to wikipedia ")
        print(results)
        speak(results)
        break
    elif 'play music' in query:
        music='E:\\Songs'
        songs=os.listdir(music)
        print(songs)
        os.startfile(os.path.join(music,songs[1]))
        break
    elif 'open sentimental analysis' in query:
        print("Opening sentimental analysis")
        speak("Opening sentimental analysis")
        webbrowser.open("https://whisper-app-tucyryscthv5fmvty78zi7.streamlit.app/")
        break
    elif 'open code' in query:
        path="C:\Microsoft VS Code\Code.exe"
        os.startfile(path)
        break
    elif 'the weather' in query:
        webbrowser.open("https://www.accuweather.com/en/in/dehradun/191339/weather-forecast/191339")
        break
    elif 'open youtube' in query:
        print("opening youtube..")
        speak("opening youtube sir")
        webbrowser.open("https://www.youtube.com/")
        #break
    elif 'close youtube' in query:
        print("closing YouTube...")
        speak("closing YouTube sir")
        pyautogui.hotkey('ctrl', 'w')
    elif 'open google' in query:
        print("opening Google...")
        speak("opening google for you sir")
        webbrowser.open("https://www.google.com/")
        #break
    elif 'close google' in query:
        print("closing Google...")
        speak("closing Google for you sir")
        pyautogui.hotkey('ctrl', 'w')
    elif 'current date and time' in query:
        time=datetime.datetime.now().strftime("%H:%M:%S")
        date=datetime.datetime.now().strftime("%d:%m:%Y")
        print(date)
        print(time)
        speak(f"Sir The date is- {date}")
        speak(f"and the time is- {time}")
        break
    elif 'send mail' in query:
        try:
            speak('what should i say')
            content=takeCommand()
            li = ['anusingh8421@gmail.com','bauraiayush733@gmail.com']
            length=len(li)
            for i in range (length):
                to=li[i]
                sendmail(to,content)
            print("mail sent successfully!")
            speak("mail has been sent successfully!")
            break
        except Exception as e:
            print(e)
            speak("There has been an error in sending the mail!")
            break
    elif 'search movie' in query:
        moviesdb = imdb.IMDb()
        speak("What is the title of the movie you want to search sir")
        movie_title=takeCommand()
        movies = moviesdb.search_movie(movie_title)
        for movie in movies:
            info=movie.getID()
            movie = moviesdb.get_movie(info)
            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            plot = movie['plot outline']
            if year < int(datetime.datetime.now().strftime("%Y")):
                print(f'{title} was released in {year} has IMDB rating of {rating}.\nThe plot summary of movie is{plot}')
                speak(f'{title}was released in {year} has IMDB rating of {rating}The plot summary of movie is{plot}')
            else:
                print(f'{title}will release in {year} has IMDB rating of {rating}.\nThe plot summary of movie is{plot}')
                speak(f'{title}will release in {year} has IMDB rating of {rating}.The plot summary of movie is{plot}')
        break
    elif 'store information' in query:
        speak("What do you want to store sir?")
        content=takeCommand();
        f = open("E:/test.txt", "w")   #file object
        f.writelines(content);
        f.close()
        print("Content successfully saved in specified location sir")
        speak("Content successfully saved in specified location sir")
        break
    elif 'alexa stop' in query:
        break