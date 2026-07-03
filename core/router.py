"""
==========================================
            GHOST Router
==========================================
Routes user requests to the correct feature.
"""

from features.open_apps import app_opener
from core.speaker import speaker


class Router:

    def execute(self, intent, text):

        if intent == "OPEN_APP":

            success, message = app_opener.open(text)

            speaker.speak(message)

            return

        speaker.speak("Sorry, I don't know how to do that yet.")


router = Router()
