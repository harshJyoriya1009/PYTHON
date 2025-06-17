import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio


recognizer= sr.Recognizer()
engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
   if "open google" in c.lower():
    webbrowser.open("https://google.com")

   elif "open youtube" in c.lower():
       webbrowser.open("https://youtube.com")
   
   elif "open linkedin" in c.lower():
       webbrowser.open("https://linkedin.com")

if __name__ == "__main__":
    speak("Opening Jarvis")

    while True:
        r=sr.Recognizer()
        


        try:
            with sr.Microphone() as source:
                print("Say something")
                audio= r.listen(source, timeout=2, phrase_time_limit=1)
            word= r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes sir")

                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis activated..")
                    audio= r.listen(source)
                    command= r.recognize_google(audio)

                    processCommand(command)


        
        except Exception as e:
            print("Jarvis error; {}".format(e)) 

# YTC
