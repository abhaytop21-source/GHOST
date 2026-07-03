"""
==========================================
            GHOST Brain
==========================================
Detects the user's intent.
"""

from core.commands import COMMANDS


class Brain:

    def detect_intent(self, text):

        text = text.lower()

        for intent, keywords in COMMANDS.items():

            for keyword in keywords:

                if keyword in text:

                    return intent

        return "UNKNOWN"


brain = Brain()