"""
==========================================
            GHOST Logger
==========================================
Handles logging for the entire application.
"""

import logging
import os


class GhostLogger:

    def __init__(self):

        # Create logs folder if it doesn't exist
        os.makedirs("logs", exist_ok=True)

        logging.basicConfig(
            filename="logs/ghost.log",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S"
        )

    def info(self, message):
        logging.info(message)
        print(f"[INFO] {message}")

    def warning(self, message):
        logging.warning(message)
        print(f"[WARNING] {message}")

    def error(self, message):
        logging.error(message)
        print(f"[ERROR] {message}")


logger = GhostLogger()