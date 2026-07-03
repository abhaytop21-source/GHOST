"""
==========================================
            GHOST Router
==========================================
Routes user requests to the correct feature.
"""

from features.open_apps import app_opener
from core.speaker import speaker


class Router:

    def execute(self, command):

        intent = command["intent"]
        entity = command["entity"]

        if intent == "OPEN_APP":

            success, message = app_opener.open(entity)
            speaker.speak(message)
            return

        speaker.speak("Sorry, I don't know that command yet.")


router = Router()