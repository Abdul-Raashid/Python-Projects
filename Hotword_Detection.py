import os
import speech_recognition as sr

listener = sr.Recognizer()



def take_command():
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    print(command)
        except:
            pass
        return command

while True:
    wake_Up=take_command()

    if 'wake up' in wake_Up:
     os.startfile('D:\\SEM-4\\program files\\Projects\\Alexa.py')
    else:
       print("Nothing.....")