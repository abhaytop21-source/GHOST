"""
==========================================
            GHOST Speaker
==========================================
Converts text into speech.
"""

import pyttsx3

from core.config import (
    ASSISTANT_NAME,
    VOICE_RATE,
    VOICE_VOLUME,
    VOICE_ID
)


class Speaker:

    def __init__(self):
        self.engine = pyttsx3.init()

        voices = self.engine.getProperty("voices")

        if len(voices) > VOICE_ID:
            self.engine.setProperty("voice", voices[VOICE_ID].id)

        self.engine.setProperty("rate", VOICE_RATE)
        self.engine.setProperty("volume", VOICE_VOLUME)

    def speak(self, text):
        print(f"{ASSISTANT_NAME}: {text}")

        self.engine.say(text)
        self.engine.runAndWait()


speaker = Speaker()