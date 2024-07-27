#Name: Long Hoang 
#Final Project 

import speech_recognition as sr #convert speech to text
import pyttsx3
from gtts import gTTS #convert text to speech
import os
#import platform  # detect the operating system
from playsound import playsound  # cross-platform audio playback


# Define available languages with full names and codes
languages = {
    '1': ('en', 'English'),
    '2': ('es', 'Spanish'),
    '3': ('fr', 'French'),
    '4': ('de', 'German'),
    # can add more languages if needed
}

#option to choose a list of available language
def select_language():

    print("Select language:")
    #print available language to choose from
    for key, (code, name) in languages.items():
        print(f"{key}: {name}")
    
    choice = input("Choose language (number): ")

    #default to English if invalid input
    return languages.get(choice, ('en', 'English'))[0]

#convert input text to speech (with chosen language) 
def text_to_speech(text, language):

    tts = gTTS(text=text, lang=language)

    filename = "output.mp3"
    tts.save(filename) #save file to play

    # play the audio file using playsound for cross-platform compatibility
    playsound(filename)

#capture speech and convert to text
def speech_to_text(language):

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # Recognize and print the speech as text using the specified language.
            text = recognizer.recognize_google(audio, language=language)
            print(f"You said: {text}")
        
        #catch exceptions
        except sr.WaitTimeoutError: #timed out error
            print("Listening timed out while waiting for phrase to start.")
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")

def main():
    #option to choose the langauge first
    language = select_language()
    
    #menu
    while True:
        print("\nMenu:")
        print("1. Text to Speech")
        print("2. Speech to Text")
        print("3. Change Language")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        #text to speech 
        if choice == '1':
            text = input("Enter the text to convert to speech: ")
            text_to_speech(text, language)

        #speech to text
        elif choice == '2':
            speech_to_text(language)

        #change language
        elif choice == '3':
            language = select_language()

        #exit menu --> exit program
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()