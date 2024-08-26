import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import json
import requests
import time

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  


# Function to speak the provided text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to greet the user based on the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Please tell me how may I help you?")


# Function to listen and recognize the user's voice command
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Please try again.")
        speak("Sorry, I did not understand that. Please try again.")
        return "None"
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        speak("Sorry, my speech service is down.")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred. Please try again.")
        return "None"
    
    return query.lower()


def sendEmail(to, content):
    try:
        # Read email credentials from a config file
        with open('config.json') as config_file:
            config = json.load(config_file)
        
        email_address = config['email_address']
        email_password = config['email_password']

        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        # Login to the server
        server.login(email_address, email_password)

        # Send the email
        server.sendmail(email_address, to, content)
        server.close()
        
        speak("Email has been sent!")
    except smtplib.SMTPAuthenticationError:
        speak("Failed to authenticate with the email server. Please check your email and password.")
    except smtplib.SMTPException as e:
        speak(f"SMTP error occurred: {e}")
    except Exception as e:
        speak(f"An error occurred: {e}")


# Function to open a website
def openWebsite(query):
    if 'youtube' in query:
        webbrowser.open("youtube.com")
    elif 'google' in query:
        webbrowser.open("google.com")
    elif 'stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'geeksforgeeks' in query:
        webbrowser.open("geeksforgeeks.com")
    else:
        speak("Which website would you like to open?")
        site = takeCommand().lower()
        webbrowser.open(f"https://{site}.com")


# Function to play music
import webbrowser

def playMusic():
    try:
        speak("Do you want to play a specific song, playlist, or just open Spotify?")
        command = takeCommand().lower()
        
        if 'playlist' in command:
            speak("Please provide the name of the playlist you want to play.")
            playlist = takeCommand().lower()
            webbrowser.open(f"https://open.spotify.com/search/{playlist}")
            speak(f"Playing the playlist {playlist} on Spotify.")
        
        elif 'song' in command:
            speak("Please provide the name of the song you want to play.")
            song = takeCommand().lower()
            webbrowser.open(f"https://open.spotify.com/search/{song}")
            speak(f"Playing the song {song} on Spotify.")
        
        else:
            webbrowser.open("https://open.spotify.com")
            speak("Opening Spotify.")

    except Exception as e:
        print(e)
        speak("Sorry, I couldn't open Spotify.")



# Function to provide the current time
def tellTime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")


# Function to search Wikipedia
def searchWikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError:
        speak("Your query was too ambiguous. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find a page matching your query.")
    except Exception as e:
        print(e)
        speak("An error occurred while searching Wikipedia.")


# Function to get weather information
def getWeather(city):
    try:
        api_key = "e9f2466b73f8a2f4df2cf6d0aff3ba58"  # Replace with your OpenWeatherMap API key
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            weather_description = weather["description"]
            speak(f"The temperature in {city} is {temperature} degrees Celsius with {weather_description}.")
        else:
            speak("City not found.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't fetch the weather information right now.")

# Function to control system volume
def controlVolume(action):
    try:
        if action == "mute":
            os.system("nircmd.exe mutesysvolume 1")
            speak("System volume muted.")
        elif action == "unmute":
            os.system("nircmd.exe mutesysvolume 0")
            speak("System volume unmuted.")
        elif action == "increase":
            os.system("nircmd.exe changesysvolume 5000")
            speak("Increasing system volume.")
        elif action == "decrease":
            os.system("nircmd.exe changesysvolume -5000")
            speak("Decreasing system volume.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't control the volume.")


# Function to tell a joke
def tellJoke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? Because it had a virus!",
        "Why was the math book sad? It had too many problems."
    ]
    speak(jokes[int(datetime.datetime.now().second) % len(jokes)])


# Function to get current affairs
def getCurrentAffairs():
    try:
        api_key = "877a88151224475ca201e1f62878813e"  # Replace with your NewsAPI key
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
        response = requests.get(url)
        news_data = response.json()
        
        if news_data['status'] == 'ok':
            articles = news_data['articles']
            speak("Here are the top news headlines.")
            for i, article in enumerate(articles[:5]):
                speak(f"Headline {i + 1}: {article['title']}")
        else:
            speak("I couldn't fetch the news at this moment.")
    except Exception as e:
        print(e)
        speak("An error occurred while fetching the news.")



# Function to handle commands
def processCommand(query):
    if 'wikipedia' in query:
        searchWikipedia(query)
    elif 'open' in query:
        openWebsite(query)
    elif 'play music' in query:
        playMusic()
    elif 'the time' in query:
        tellTime()
    elif 'weather' in query:
        speak("Please tell me the city name.")
        city = takeCommand().lower()
        getWeather(city)
    elif 'mute' in query:
        controlVolume("mute")
    elif 'unmute' in query:
        controlVolume("unmute")
    elif 'increase volume' in query:
        controlVolume("increase")
    elif 'decrease volume' in query:
        controlVolume("decrease")
    elif 'tell me a joke' in query:
        tellJoke()
    elif 'current affairs' in query or 'news' in query:
        getCurrentAffairs()
    elif 'email to' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "recipient@gmail.com"  # Replace with actual email or use a dictionary for multiple recipients
            sendEmail(to, content)
        except Exception as e:
            print(e)
            speak("Sorry, I am not able to send the email at this moment.")
    else:
        speak("I am not sure how to handle that request.")


# Main function
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if query != "None":
            processCommand(query)
        if 'exit' in query or 'quit' in query:
            speak("Goodbye. Have a great day!")
            break
