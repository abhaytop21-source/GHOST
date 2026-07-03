"""
==========================================
        GHOST Open Applications
==========================================
Opens desktop applications.
"""

import subprocess
import platform


class AppOpener:

    def __init__(self):

        self.apps = {
            "notepad": "notepad",
            "calculator": "calc",
            "paint": "mspaint",
            "cmd": "cmd"
        }

    def open(self, text):

        text = text.lower()

        for app_name, command in self.apps.items():

            if app_name in text:

                try:
                    subprocess.Popen(command)

                    return True, f"Opening {app_name}"

                except Exception as e:

                    return False, str(e)

        return False, "Application not found."


app_opener = AppOpener()