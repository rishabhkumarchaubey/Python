import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time


def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand...")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x) 
    engine.runAndWait()

if __name__ == '__main__':

    if "hey siri" in sptext().lower():
        while True :
                data1=sptext().lower()

                if "your name" in data1:
                    name = "my name is siri"
                    speechtx(name)
                elif "old are you" in data1:
                    age = "i am 20 years old"
                    speechtx(age)
                elif 'time' in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)
                elif 'youtube' in data1:
                    webbrowser.open("https://www.youtube.com/")
                elif 'gmail' in data1:
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                elif 'google' in data1:
                    webbrowser.open("https://www.google.co.in/")
                elif 'github' in data1:
                    webbrowser.open("https://github.com/")
                elif 'bhajan' in data1:
                    webbrowser.open("https://www.youtube.com/watch?v=DyJs8-DYWUk")
                elif 'joke' in data1:
                    joke_1 = pyjokes.get_joke(language="en",category="neutral")
                    speechtx(joke_1)
                elif 'song' in data1:
                    add ="D:\music"
                    listsong = os.listdir(add)
                    os.startfile(os.path.join(add,listsong[2]))
            
                elif "exit" in data1:
                    speechtx("thank you")
                    break

                time.sleep(5)

        
    else:
        print("thanks")
       
