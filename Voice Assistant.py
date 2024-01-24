# voice assistant task 1 for codealpha 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import winshell
import pyttsx3
import time
import datetime
from playsound import playsound
import os
from time import sleep
import pyjokes
from AppOpener import open
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
AssistantName =  "David"
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
# This Takes time and wishes at the starting with introduction
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("How may I help you?")
def takeCommand():
    # This takes microphone inputs from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said:  {query}\n")
    except Exception as e:
        # print("e")
        speak("I'm Sorry. I was Enable to Hear you, Say that again Please...")
        return "None"
    return query
if __name__== "__main__":
    wishMe()
    while (True):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)
        elif 'open linkedin' in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open("linkedin.com")
            speak("Opening linkedin")
            exit()    
        elif 'open youtube' in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open("youtube.com") 
            speak("Opening Youtube")
            exit()
        elif 'open Gmail' in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open("https://mail.google.com/mail/u/0/#inbox")
            speak("Opening Gmail")
            exit()
        elif 'open movies' in query:
            os.startfile(r'C:\Users\Dell\Videos\Movies')
            speak("Opening Movies")
            exit()
        elif 'open documents' in query:
            os.startfile(r'C:\Users\Dell\Documents')
            speak("Opening Documents")
            exit()
        elif 'Open Desktop' in query:
            os.startfile(r'C:\Users\Dell\Desktop')
            speak("Opening Desktop")
            exit()
        elif 'Open Downloads' in query:
            os.startfile(r'C:\Users\Dell\Downloads')
            speak("Opening Downloads")
            exit()
        elif 'open whatsapp' in query:
            open("whatsapp")
            speak("Opening whatsapp")
            exit()
        elif 'open telegram' in query:
            open("telegram desktop")
            speak("Opening telegram")
            exit()
        elif 'open Excel' in query:
            open("Excel")
            speak("Opening telegram")
            exit()
        elif 'open Word' in query:
            open("Word")
            speak("Opening telegram")
            exit()
        elif 'open chrome' in query or 'open browser' in query:
            open("google chrome")
            speak("Opening Chrome")
            exit()
        elif 'open Powershell' in query:
            open("Windows Powershell")
            speak("Opening Powershell")
            exit()
        elif 'open settings' in query:
            open("settings")
            speak("Opening settings")
            exit()
        elif 'open instagram' in query:
            open('instagram')
            speak("Opening Instagram")
            exit()
        elif 'exit' in query:
            speak("Have a Good Day")
            exit()        
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Makrand.")
            exit()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')    
            speak(f"Sir, the time is {strTime}")
            exit()
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much Minutes, I should stop from listening commands")
            a = int(takeCommand())
            time.sleep(a * 60)
            print(a)
            exit()
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(AssistantName)
            exit()
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin IS SUCCESSFULLY EMPTIED")
            exit()
        elif 'play music' in query or 'play song' in query:
            speak("Playing song")
            os.startfile('C:/Users\Dell\Music\Playlists\shivchhatrapati_song.mp3')
            exit()