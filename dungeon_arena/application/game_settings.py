from enum import Enum


class Difficulty(Enum):
    EASY = "EASY"
    DEFAULT = "DEFAULT"
    MEDIUM = "MEDIUM"
    HARD = "HARD"

class GameSettings:
    _instance = None
    _initialized = False

    def __init__(self):
        if self._initialized:
            return
        self.difficulty = Difficulty.DEFAULT
        self.sound_enabled = False
        self.theme = "Fire"
        self._initialized = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
