"""
==========================================
            GHOST AI Assistant
==========================================
"""

from core.listener import listener
from core.speaker import speaker
from core.brain import brain
from core.router import router


def main():

    speaker.speak("Hello Abhay. Ghost is online.")

    while True:

        audio = listener.record()

        text = listener.transcribe(audio)

        if not text:
            continue

        print(f"\nYou: {text}")

        command = brain.detect(text)

        print(command)

        router.execute(command)


if __name__ == "__main__":
    main()