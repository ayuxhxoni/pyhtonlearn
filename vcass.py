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
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    print(sr.Microphone.list_microphone_names())
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
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with Ayush soni')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        talk('ohk maa chuda')
    else:
        talk('please say the command again')
    while True:
        run_alexa()
run_alexa()