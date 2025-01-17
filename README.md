# File Organizer-Task 1

This script helps you organize files in a specified folder by grouping them into subdirectories based on their file extensions. 

## Features

- Automatically detects and categorizes files based on their extensions.
- Creates new directories for each file type if they don't already exist.
- Moves files into their respective directories.

## Prerequisites

- Python 3.x
- `os` and `shutil` modules (these are built-in modules in Python and don't require any additional installation)

## Usage

1. Clone the repository or download the script to your local machine.
2. Open a terminal or command prompt.
3. Run the script by executing the following command:
    ```sh
    python organize_files.py
    ```
4. Enter the path of the folder you want to organize when prompted.

## Example

```sh
Enter the folder path to organize: /path/to/your/folder


# Voice-Controlled Personal Assistant-Task 2

This script is a voice-controlled personal assistant that can perform a variety of tasks based on your voice commands.

## Features

- **Greet the User:** Greets the user based on the current time.
- **Voice Recognition:** Uses speech recognition to understand user commands.
- **Email Functionality:** Sends emails using Gmail.
- **Web Browsing:** Opens websites based on user requests.
- **Music Playback:** Plays music on Spotify.
- **Time Information:** Provides the current time.
- **Wikipedia Search:** Retrieves information from Wikipedia.
- **Weather Information:** Fetches the current weather for a specified city.
- **Volume Control:** Mutes, unmutes, increases, and decreases system volume.
- **Jokes:** Tells a random joke.
- **Current Affairs:** Provides the latest news headlines.

## Prerequisites

- Python 3.x
- `pyttsx3` module
- `speech_recognition` module
- `datetime` module
- `wikipedia` module
- `webbrowser` module
- `os` module
- `smtplib` module
- `json` module
- `requests` module

## Installation

1. Clone the repository or download the script to your local machine.
2. Install the required Python modules by running:
    ```sh
    pip install pyttsx3 speechrecognition wikipedia requests
    ```

## Usage

1. Run the script by executing the following command:
    ```sh
    python voice_assistant.py
    ```
2. Follow the voice prompts to interact with the assistant.

## Configuration

- For email functionality, create a `config.json` file with your email credentials:
    ```json
    {
        "email_address": "your-email@gmail.com",
        "email_password": "your-email-password"
    }
    ```
- Replace the OpenWeatherMap and NewsAPI keys with your own API keys in the script.

## Example Commands

- "Open YouTube"
- "Play music"
- "Tell me the time"
- "Search Wikipedia for Python programming"
- "What's the weather in Delhi?"
- "Mute the volume"
- "Tell me a joke"
- "What are the current affairs?"


