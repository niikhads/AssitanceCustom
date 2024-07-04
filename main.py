from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from pydub import AudioSegment
import webbrowser 




r = sr.Recognizer()

def speeding():
    in_path = 'answer.mp3'
    ex_path = 'speed.mp3'
    sound = AudioSegment.from_file(in_path)
    faster_sound = speed_swifter(sound, 1.1)
    faster_sound.export(ex_path, format="mp3")

def speed_swifter(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate

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
        speak("Hello, my friend")
    if "help me" in voice:
        speak("How can I help you?")
    if any(word in voice for word in ["thanks", "thank you"]):
        speak("You're welcome")
    if any(word in voice for word in ["goodbye", "good bye"]):
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
        speak(today_map.get(today, "Unknown day"))
    if "what time is it" in voice:
        selections = ["Saat indi: ", "Hemen baxiram: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selections)
        speak(selection + clock)
        
        
    if "google search" in voice:
        speak("what search I look for you?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} I'm listing the ones I could find on Google for you.".format(search))

def speak(text):
    tts = gTTS(text=text, lang="en", slow=False)
    file = "answer.mp3"
    tts.save(file)
    speeding()
    playsound("speed.mp3")
    playsound(file)
    os.remove(file)
    os.remove("speed.mp3")

speak("Hello. I am Azerbaijan Customs Service Voice Assistant. Please listen to the hymn.")
playsound("Ding.mp3")
#playsound("Himn.mp3")

while True:
    voice = record()
    if voice:
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)
