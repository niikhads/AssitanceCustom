from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="en-EN")
        except sr.UnknownValueError:
            print("Assistant: I didn't understand you")
        except sr.RequestError:
            print("Assistant: The system is not working at the moment")
        return voice

def response(voice):
    if "hello" in voice:
        speak("Hello my friend")
    if "help me" in voice:
        speak("How can I help you?")
    if "thanks" in voice or "thank you" in voice or "thanks you" in voice or "thank you very much" in voice:
        speak("You're welcome")
    if "good bye" in voice or "goodbye" in voice:
        speak("Goodbye")
        exit()
    if "what day is today" in voice:
        today = time.strftime("%A")
        today_map = {
            "Monday": "Bazar Ertesi",
            "Tuesday": "Cersenbe",
            "Wednesday": "Cersenbe axsami",
            "Thursday": "Cume axsami",
            "Friday": "Cume",
            "Saturday": "Senbe",
            "Sunday": "Bazar"
        }
        speak(today_map.get(today, today))

    if "what time is it" in voice :
        selection = ["Saat indi : ", "Hemen baxiram : "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)


def speak(text):
    tts = gTTS(text=text, lang="en", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Salam. Men Azerbaycan Gomruk Assistani. Zehmet olmasa himni dinleyin")
playsound("Ding.mp3")
#playsound("Himn.mp3")

while True:
    voice = record()
    if voice:
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)
