from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

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
            print("Assistant: Men sizi basa dusmedim")
        except sr.RequestError:
            print("Assistant: Sistem hal hazirda islemir")
        return voice
def response(voice):   
 if "hello" in voice :  # boyuk herf kicik herf diqqet
    speak("hello my friend")
 if "help me" in voice :
    speak("How can I help you?") 
 if "thanks" in voice or "thank you" in voice or "thanks you" in voice or "thank you very much" in voice:
    speak("thanks")
    
    
def speak(string):
    tts = gTTS(text=string, lang="en", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("salam nihad")

while True:  #davamli olaraq dinlemesi ucun
 voice = record()
 if voice != '':
    voice = voice.lower() # kicik herfle vermesi ucun yazildi ->
    print(voice.capitalize()) #kicik herfle versede cixisa boyuk yazir
    response(voice)


