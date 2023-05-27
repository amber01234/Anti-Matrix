import speech_recognition as sr
import pyttsx3
import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("enter your phone number")
a=input("enter your mobile number")
# speak("enter your phone number")
# print("ok, you are ")

if __name__ == "__main__":
     
        query = a
        if '8557989648' in query:
            query=query.replace("8557989648", "")
            results = "arshnoor singh"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)
        elif'8194865490' in query:
            query=query.replace("8194865490", "")
            results ="gurdeep kaur"
            speak("according to me you are ")
            speak(results)
            print("according to me you are", results)
        elif '9646152948' in query:
            query=query.replace("9646152948", "")
            results = "mohinder singh"
            speak("according to me you are")
            speak(results)    
            print("according to me you are",results)
        elif '8054301632' in query:
            query=query.replace("8054301632", "")
            results = "jagmeet kaur"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)  
        elif'7087501187' in query:
            query=query.replace("7087501187", "")
            results = "angad"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)
        elif'7589208080'in query:
            query=query.replace("7589208080", "")
            results = "Anubhav"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)     
        elif'9991163963' in query:
            query=query.replace("9991163963", "")
            results = "Bittu Chacha"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)    
        elif'8699371370'in query:
            query=query.replace("8699371370", "")
            results = "Divyanshi"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)
        elif'9896429194'in query:
            query=query.replace("9896429194", "")
            results = "Gagandeep Kaur"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)  
        elif'7837060935'in query:
            query=query.replace("7837060935", "")
            results = "Sarabjeet Singh"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)
        elif'8950650252'in query:
            query=query.replace("8950650252", "")
            results = "Harmeet Singh"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results) 
        elif'7717638881'in query:
            query=query.replace("77176638881", "")
            results = "Harsimranjot Singh"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)
        elif'4164020503'in query:
            query=query.replace("4164020503", "")
            results = "Jagjeet Singh"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results) 
        elif'8708541253'in query:
            query=query.replace("8708541253", "")
            results = "Gurpreet Kaur"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)
        elif'9728954218'in query:
            query=query.replace("9728954218", "")
            results = "Daljit Singh"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)
        elif'7719670516'in query:
            query=query.replace("7719610516", "")
            results = "Samar"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results)
        elif'8360744780'in query:
            query=query.replace("8360744780", "")
            results = "Shreya"
            speak("according to me you are")
            speak(results)
            print("according to me you are",results) 



speak("am i correct")
m=input("am i correct?")   

if __name__ == "__main__":
     
        query = m
        if'yes'in query:
            speak("i knew it i will be correct!")
            print("yeaaaaa!!")


                                          

             





    
    