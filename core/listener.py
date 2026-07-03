"""
==========================================
            GHOST Listener
==========================================
Records audio and converts it to text.
"""

import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel


class Listener:

    def __init__(self):
        self.sample_rate = 16000
        self.duration = 5

        print("Loading Whisper model... (first time may take a minute)")
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )
        print("Whisper loaded successfully.")

    def record(self, filename="voice.wav"):

        print("🎤 Listening...")

        audio = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        write(filename, self.sample_rate, audio)

        print("✅ Recording saved.")

        return filename

    def transcribe(self, filename):

        print("🧠 Understanding...")

        segments, info = self.model.transcribe(filename)

        text = ""

        for segment in segments:
            text += segment.text

        text = text.strip()

        print(f"You said: {text}")

        return text


listener = Listener()