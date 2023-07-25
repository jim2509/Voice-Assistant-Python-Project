import datetime
import speech_recognition as sr
import pyttsx3
import pyjokes
import wikipedia
import webbrowser

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the speaker
engine = pyttsx3.init()


# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to get voice command
def get_command():
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}\n")
    except Exception as e:
        print('Say that again please...')
        return "None"
    return command.lower()


def assistant(command):
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace('wikipedia', '')
        results = wikipedia.summary(command, sentences=2)
        speak('According to Wikipedia')
        print(results)
        speak(results)

    elif 'open youtube' in command:
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'joke' in command:
        speak(pyjokes.get_joke())

    elif 'quit' in command or 'exit' in command:
        speak("Okay, quitting now. Have a nice day!")
        exit()

    


if __name__ == "__main__":
    speak("Hello, I'm your voice assistant. How can I help you today?")
    while True:
        command = get_command()
        assistant(command)
