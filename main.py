import speech_recognition as sr
import os 
import webbrowser

def say(text):
    os.system(f"say {text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error occurred. Sorry from Alien X"

if __name__ == "__main__":
    print("Alien X")
    say("Hello, I am Alien X  ")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"],
                ["wikipedia", "https://www.wikipedia.com"],
                ["google", "https://www.google.com"],
                ["github", "https://github.com/Manthanwarte"],
                ["instagram", "https://www.instagram.com/enoughmanthan/"],
                ["linkedin", "https://www.linkedin.com/in/manthan-warte-696378311/"]]
        for site in sites:
            if f"Open {site[0]}" in query:
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            musicpath = "/Users/manthanwarte/Downloads/Aarzu - DjBaap.mp3"
            os.system(f"open '{musicpath}'")
            # say(query)

        if "open FaceTime" in query:
            os.system(f"open /System/Applications/FaceTime.app")

