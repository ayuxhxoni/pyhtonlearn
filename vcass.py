from tracemalloc import stop
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia 
import pyjokes
import microphone
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 178)
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source,duration=1)
        print('listening...')
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
            print(command)
        except:
            print("sorry, could not recognise")
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'hello love' in command:
        talk('what do u want me to do')
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with my developer')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'stop' in command:
            talk('ok we will meet some other time!')
        else:
            talk('please say the command again')
        while True:
            run_alexa()
    else:
        talk('')
        
run_alexa()