import datetime
from email.mime import audio
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon.")
    
    else:
        speak("ood evening")    

    speak("I am ROBO sir.. Please tell me how may i help you.. ")

def takeCommand():
    '''it take instruction from user and return the output'''
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :- {query}\n")    
    except Exception as e:
        # print(e)
        print("Say that Again Please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('madhurj1904@gmail.com','Madhur@#@#1904')
    server.sendmail('madhurj1904@gmail.com', to, content)
    server.close()        
        
if __name__ == "__main__":
    wishMe()    
    # while True:
    if 1:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia..")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")  
        
        elif 'open insta' in query:
            webbrowser.open("instagram.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")    
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
               
        elif 'play music' in query:
            music_dir = 'F:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%S:%M:%S")
            speak(f"sir, the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"        
            os.startfile(codepath)
            
        elif 'email to duffer'in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "komalmodak2000@gmail.com"
                sendEmail(to, content)
                speak("Email has been send")    
            except Exception as e:
                print(e)
                speak("sorry my Friend.. I am not Able to send this email")    