"""
==========================================
            GHOST AI Assistant
==========================================
Main Program
"""

from core.listener import listener
from core.speaker import speaker
from core.brain import brain

from features.open_apps import app_opener


def execute(intent, text):

    if intent == "OPEN_APP":

        success, message = app_opener.open(text)

        speaker.speak(message)

    else:

        speaker.speak("Sorry, I don't know how to do that yet.")


def main():

    speaker.speak("Hello Abhay. Ghost is online.")

    while True:

        audio = listener.record()

        text = listener.transcribe(audio)

        if not text:
            continue

        intent = brain.detect_intent(text)

        print(f"Intent -> {intent}")

        execute(intent, text)


if __name__ == "__main__":
    main()