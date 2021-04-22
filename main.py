import speech_recognition as sr
import pyttsx3
import datetime
import pyautogui
from playsound import playsound as ps
from time import sleep

listener = sr.Recognizer()
listener.dynamic_energy_threshold = False
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print(sr.Microphone.list_microphone_names())


def talk(text):
    engine.say(text)
    engine.runAndWait()

def Microphone():
    # Turn on Mic
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('m')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('m')

    # Play Sound
    ps('here.mp3')

    sleep(2)

    # Turn off Mic
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('m')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('m')


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source, phrase_time_limit=3)
            command = listener.recognize_google(voice, language="sv-SV")
            command = command.lower()
            return command
            if 'gustav' in command:
                print("oof")
                return 'gustav'
            else:
                return 'none'
                
    except:
        pass

def run_alexa():
    command = take_command()
    if command == 'gustav':
        Microphone()

    print(command)


while True:
    run_alexa()