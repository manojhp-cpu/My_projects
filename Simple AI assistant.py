import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import pyjokes


#initialization or creating an instance
listener=sr.Recognizer()
microphone=sr.Microphone()
engine=pyttsx3.init()
current_rate=engine.getProperty('rate')
newrate=current_rate-70
engine.setProperty('rate',newrate)


def talking(text):

    engine.say(text)
    engine.runAndWait()


def reply(text1):
    engine.say(text1)

    engine.runAndWait()

#command taking from user
def command_talking():
    try:
        with microphone as source:
            print('Listening....')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'robo' in command:
                command=command.replace('robo','')
                print(command)
    except:
        print('not Recognized')
    return command


def run_AI():
    command=command_talking()
    if 'play' in command:
        song=command.replace('play','')
        talking('ok i will playing'+song)
        pywhatkit.playonyt(song)
    elif 'hello' in command:
        talking('Hi nice to meet You')
    elif 'you' in command:
        talking('I am your personal assistant')
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talking('Current Time is'+time)
    elif'about' and 'who' in command:
        details=command.replace('about','')
        info=wikipedia.summary(details,10)
        print(info)
        talking(info)
    elif 'joke' in command:
        funny=pyjokes.get_joke()
        print(funny)
        talking(funny)
    elif 'is it funny' in command:
        pass


#calling the functions
reply('Hi i am A I assistant')
reply('what can i help you')
run_AI()



