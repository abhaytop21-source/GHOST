"""
==========================================
            GHOST Brain
==========================================
Detects intent and extracts entities.
"""

from core.commands import COMMANDS


class Brain:

    def detect(self, text):

        text = text.lower()

        result = {
            "intent": "UNKNOWN",
            "entity": None,
            "text": text
        }

        for intent, keywords in COMMANDS.items():

            for keyword in keywords:

                if keyword in text:

                    result["intent"] = intent

                    entity = text.replace(keyword, "").strip()

                    result["entity"] = entity

                    return result

        return result


brain = Brain()