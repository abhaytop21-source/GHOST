"""
==========================================
            GHOST Brain
==========================================
Analyzes user input and creates a Request.
"""

from core.commands import COMMANDS
from core.request import Request


class Brain:

    def detect(self, text: str) -> Request:

        text = text.lower().strip()

        request = Request(
            text=text
        )

        for intent, keywords in COMMANDS.items():

            for keyword in keywords:

                if keyword in text:

                    request.intent = intent

                    entity = text.replace(keyword, "").strip()

                    request.entity = entity if entity else None

                    return request

        return request


brain = Brain()