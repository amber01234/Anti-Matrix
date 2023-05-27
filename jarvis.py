import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import cv2
import os
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sir') 
    elif hour>=12 and hour<18:
        speak('Good Afternoon sir')
    else:
        speak('Good Evening sir')    

    speak('I am jarvis your virtual assistant, how can i help you')   
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 5
        audio = r.listen(source)
       


    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f"User said:{query}\n")

    except Exception as e:
        print('plese say that again sir')
        return "None"
    return query  
       
a=int(time.strftime('%Y'))
b=int(time.strftime('%H'))
c=int(time.strftime('%M'))
d=int(time.strftime('%S'))
e=time.strftime('%H:%M:%S')
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if takeCommand()==ord("s"): break
   #executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            if cv2.waitKey(10)==ord("a"):
                break

        elif 'open YouTube' in query:
            speak("opening")
            webbrowser.open_new_tab("https:\\www.youtube.com")

        elif'open google' in query:
            speak("opening")
            print("opening......")    
            webbrowser.open_new_tab("https:\\www.google.com")
            if cv2.waitKey(10)==ord("a"):break
        elif'open instagram'in query:
            speak("opening")
            print("opening....")    
            webbrowser.open_new_tab("https:\\www.instagram.com")

        elif'open whatsapp'in query:
            speak("opening")
            print("opening...")
            webbrowser.open_new_tab("https://web.whatsapp.com")
   
        elif'music'in query:
            speak('playing')
            music_dir='C://Program Files//music'
            songs=os.listdir(music_dir)    
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif'jarvis'in query:
            speak('yes sir')
        elif'who are you'in query:
            speak('I am Jarvis and I am made by Arshnoor Singh')
            print("I am Jarvis and I am made by Arshnoor Singh")  
        elif 'Who is Arshnoor'in query:
            speak('Arshnoor is that person who made me')      
            print("Arshnoor is that person who made me")
        elif'who am I'in query:
            speak('you are the person who will give command to me')  
        elif'who made you'in query:
            speak('Arshnoor Singh made me')   
        elif'hello'in query:speak('hello sir')
        elif'do not call me sir'in query:
            speak("ok so what would you like me to call you")
            a=input()
            speak('Hi')
            speak(a)
        elif'what are you doing'in query:
            speak('nothing special')
            speak('what are you doing sir')
            b=input(takeCommand())
            speak('so you are doing')
            speak(b)
        elif'how are you'in query:
            speak("fine how about you")
        elif 'not fine'in query:
            speak('oh my god why,what happened')
        elif'nothing happened'in query:
            speak('please sir . sorry')
            speak(a)
            speak('tell me')
            d=input(takeCommand())
            speak('its ok just chill')
        elif'fine'in query:
            speak('nice')    
        elif'what time is it'in query:
            speak(e)    
            print(e)
        elif'which year is going on'in query:
            print(a)    
            speak(a)



    
    
                      




        





