"""
==========================================
        GHOST Configuration File
==========================================
This file contains all configurable settings
used throughout the assistant.
"""

# ----------------------------------------
# Assistant Information
# ----------------------------------------

ASSISTANT_NAME = "Ghost"

OWNER_NAME = "Abhay"

VERSION = "1.0"

LANGUAGE = "en"

# ----------------------------------------
# Voice Settings
# ----------------------------------------

VOICE_RATE = 170      # Speaking speed

VOICE_VOLUME = 1.0    # Range: 0.0 - 1.0

VOICE_ID = 0          # 0 = Male | 1 = Female (depends on system)

# ----------------------------------------
# Wake Word (For Future)
# ----------------------------------------

WAKE_WORD = "hey ghost"

# ----------------------------------------
# Memory Files
# ----------------------------------------

CHAT_HISTORY_FILE = "memory/chat_history.txt"

NOTES_FILE = "memory/notes.txt"

USER_MEMORY_FILE = "memory/user_memory.json"

REMINDER_FILE = "memory/reminders.json"

# ----------------------------------------
# API Keys (We'll add later)
# ----------------------------------------

GEMINI_API_KEY = ""

OPENAI_API_KEY = ""