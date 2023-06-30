import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import json
import datetime
import google



google.api_key = "AIzaSyBaCGJOkR27FQIgtl26tZ1SLj_z2nRvlHQ"
{
    "api_key": "AIzaSyBaCGJOkR27FQIgtl26tZ1SLj_z2nRvlHQ",
    "engine": "bard" 
}


creds_file = os.path.join(os.getcwd(), "credentials.json")

with open(creds_file, "r") as f:
    creds = json.load(f)

engine = pyttsx3.init()

r = sr.Recognizer()

websites = {
    "github.com": "https://github.com",
    "stackoverflow.com": "https://stackoverflow.com",
    "youtube.com": "https://www.youtube.com",
    "discord.com": "https://discord.com",
    "google.com": "https://www.google.com",
    "reddit.com": "https://www.reddit.com",
    "instagram.com": "https://www.instagram.com",
    "replit.com": "https://replit.com",
    "linkedin.com": "https://www.linkedin.com",

}


def open_website(url):
    webbrowser.open_new_tab(url)

def generate_response(prompt):
    response = google.Completion.create(
        engine=google.engine,
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
    )
    text = response.choices[0].text.strip()
    return text

def speak(message):
    print(message)

def main():
    while True:
        prompt = input("Enter your prompt: ")
        response = generate_response(prompt)
        speak(response)

def speak(message):
    engine.say(message)
    engine.runAndWait()


def wish_me():
    now = datetime.datetime.now()
    hour = now.hour
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you?")


def main():
    
    wish_me()

    while True:
       
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

       
        query = ""
        try:
            query = r.recognize_google(audio)
            print("You said:", query)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            continue
        except sr.RequestError:
            print("Sorry, my speech service is down right now.")
            continue

        
        if "open" in query:
            for site in websites:
                if site in query:
                    open_website(websites[site])
                    speak("Opening " + site)
                    break
            else:
                speak("Sorry, I don't know that website.")
        else:
            
            
            prompt = "User: " + query + "\nAI:"
            response = generate_response(prompt)
            print("AI:", response)
            speak(response)

if __name__ == "__main__":
    main()