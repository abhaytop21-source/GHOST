"""
==========================================
            GHOST Request
==========================================
Represents a user's request after it has
been processed by the Brain.
"""

from dataclasses import dataclass


@dataclass
class Request:
    """
    Represents a processed user request.
    """

    intent: str = "UNKNOWN"
    entity: str | None = None
    text: str = ""
    confidence: float = 1.0
    source: str = "voice"