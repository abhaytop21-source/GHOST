"""
==========================================
            GHOST Router
==========================================
Routes a Request to the correct plugin.
"""

from core.speaker import speaker
from core.logger import logger

from core.request import Request

from features.open_apps import app_opener


class Router:

    def execute(self, request: Request):

        logger.info(f"Routing Intent -> {request.intent}")

        if request.intent == "OPEN_APP":

            success, message = app_opener.open(request.entity)

            if success:
                logger.info(message)
            else:
                logger.warning(message)

            speaker.speak(message)

            return

        speaker.speak("Sorry, I don't know that command yet.")


router = Router()