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

    def open(self, app_name):

        app_name = app_name.lower().strip()

        if app_name in self.apps:

            try:

                subprocess.Popen(self.apps[app_name])

                return True, f"Opening {app_name}"

            except Exception as e:

                return False, str(e)

        return False, f"I couldn't find {app_name}."


app_opener = AppOpener()