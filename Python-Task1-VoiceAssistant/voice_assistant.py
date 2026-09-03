# ==========================================
# OIBSIP - Python Programming
# Task 1: Voice Assistant
# Beginner Tier
# ==========================================

import datetime
import webbrowser
import pyttsx3


# Initialize text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """Convert text into speech and display it."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def show_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def show_date():
    """Tell today's date."""
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {current_date}")


def open_website(command):
    """Open a website based on the command."""

    if "google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

    else:
        speak("Sorry, I don't know that website.")


def process_command(command):
    """Process the user's command."""

    command = command.lower().strip()

    if command in ["hello", "hi", "hey"]:
        speak("Hello! How can I help you?")

    elif "time" in command:
        show_time()

    elif "date" in command:
        show_date()

    elif "open google" in command:
        open_website("google")

    elif "open youtube" in command:
        open_website("youtube")

    elif "open github" in command:
        open_website("github")

    elif command in ["help", "what can you do"]:
        speak(
            "I can tell you the time and date, "
            "open Google, YouTube and GitHub, "
            "and respond to basic greetings."
        )

    elif command in ["bye", "exit", "quit", "stop"]:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry, I did not understand that command.")

    return True


def main():
    """Start the voice assistant."""

    speak("Hello! I am your Python voice assistant.")
    speak("Type a command. Type help to see what I can do.")

    running = True

    while running:
        command = input("\nYou: ")
        running = process_command(command)


if __name__ == "__main__":
    main()
