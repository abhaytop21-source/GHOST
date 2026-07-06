"""
==========================================
        GHOST AI Platform
==========================================
Main Entry Point
"""

from core.listener import listener
from core.speaker import speaker
from core.brain import brain
from core.router import router
from core.logger import logger


class Ghost:

    def __init__(self):

        logger.info("Starting GHOST...")

        speaker.speak("Hello Abhay. Ghost is online.")

    def run(self):

        while True:

            audio = listener.record()

            text = listener.transcribe(audio)

            if not text:
                continue

            logger.info(f"User: {text}")

            request = brain.detect(text)

            logger.info(f"Intent: {request.intent}")

            router.execute(request)


if __name__ == "__main__":

    ghost = Ghost()

    ghost.run()