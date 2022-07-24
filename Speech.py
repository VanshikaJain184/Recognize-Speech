
import speech_recognition as sr
# import wikipedia
import webbrowser

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Just Listening your command...")
        r.pause_threshhold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing what you said...")
        query=r.recognize_google(audio,language='en-in')
        print("You said: ",query)
        return query
    
    except Exception as e:
        #print(e)
        print("Sorry to listen and understand! Please say it again.")
        return "None"


myinput=takeCommand().lower()

if 'open youtube' in myinput:
    webbrowser.open('youtube.com')
if 'open google' in myinput:
    webbrowser.open('google.com')
