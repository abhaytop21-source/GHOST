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

        intent = brain.detect_intent(text)

        print(f"Intent: {intent}")

        router.execute(intent, text)


if __name__ == "__main__":
    main()