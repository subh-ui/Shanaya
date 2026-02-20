import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import os

# text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Wishing
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning Subhrajeet!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Subhrajeet!")
    else:
        speak("Good Evening Subhrajeet!")

    speak("I am Shanaya.")


# Wake word system
def listen_for_wake_word():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Waiting for wake word...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 0.8
        r.energy_threshold = 300

        audio = r.listen(source)

    try:
        trigger = r.recognize_google(audio, language='en-IN').lower()
        print(f"Heard: {trigger}")

        if "hey shanaya" in trigger or "hi shanaya" in trigger:
            return True

    except Exception:
        pass

    return False


# Command Listener
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 0.8
        r.energy_threshold = 300

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")

    except Exception:
        print("Say that again please...")
        return None

    return query


# Open any website by voice
def open_website(query):
    try:
        words = query.split()

        if "open" in words:
            idx = words.index("open")
            if idx + 1 < len(words):
                site = words[idx + 1]
            else:
                speak("Please tell the website name")
                return
        else:
            return

        if not site.startswith("http"):
            if "." not in site:
                site += ".com"
            url = "https://www." + site
        else:
            url = site

        speak(f"Opening {site}")
        webbrowser.open(url)

    except Exception as e:
        print(e)
        speak("Sorry, I could not open the website")

# Google search by voice
def search_google(query):
    try:
        speak("Searching Google")

        trigger_words = [
            "search google",
            "google search",
            "search for",
            "search"
        ]

        search_term = query
        for word in trigger_words:
            search_term = search_term.replace(word, "")

        search_term = search_term.strip()

        if not search_term:
            speak("What should I search?")
            search_term = takeCommand()
            if search_term is None:
                return

        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(url)

    except Exception as e:
        print(e)
        speak("Sorry, I could not search Google")  

# Main Function
if __name__ == "__main__":
    wishMe()

    while True:
        if listen_for_wake_word():
            speak("Yes Subhrajeet, I am listening")

            # Active Mode
            while True:
                query = takeCommand()
                if query is None:
                    continue

                query = query.lower()

                # Sleep command
                if 'go to sleep' in query or 'stop listening' in query:
                    speak("Going to sleep")
                    break

                # Wikipedia
                elif 'wikipedia' in query:
                    speak("Searching Wikipedia")
                    search_query = query.replace("wikipedia", "")
                    results = wikipedia.summary(search_query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                
                elif 'search google' in query or 'google search' in query:
                    search_google(query)

                elif 'open github' in query:
                    webbrowser.open("https://github.com/subh-ui")

                elif 'open' in query:
                    open_website(query)

                elif 'play music' in query:
                    music_dir = 'C:\\Playlist\\Party Songs'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Sir, The time is {strTime}")
                    speak(f"Sir, The time is {strTime}")

                elif "open code" in query:
                    codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                