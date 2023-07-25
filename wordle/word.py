from unidecode import unidecode
from enum import Enum

class Result(Enum):
    NO_MATCH = 0
    EXACT_MATCH = 1
    PARTIAL_MATCH = 2

class Word:
    def __init__(self, value):
        self.value = value
        self.result = [Result.NO_MATCH, Result.NO_MATCH, Result.NO_MATCH, Result.NO_MATCH, Result.NO_MATCH]

    def is_correct_word(self, answer):
        return unidecode(self.value.upper()) == unidecode(answer.upper())

    def compare_and_return_colorized_text(self, answer):
        self._compare_exact(answer) #green
        self._compare_inexact(answer)  #yellow
        return self._get_colorized_text()

    def _compare_exact(self, answer):
        for i, (x, y) in enumerate(zip(answer, self.value)):
            if unidecode(x) == unidecode(y):
                self.result[i] = Result.EXACT_MATCH

    def _compare_inexact(self, answer):
        available_letters = [unidecode(answer[i]) for i, x in enumerate(self.result) if x == Result.NO_MATCH]

        for i, letter in enumerate(self.value):
            if (self.result[i] == Result.NO_MATCH) and (unidecode(letter) in available_letters):
                self.result[i] = Result.PARTIAL_MATCH
                available_letters.pop(available_letters.index(letter))

    def _get_colorized_text(self):
        colored_text = ""
        for result, letter in zip(self.result, self.value):
            if result == Result.EXACT_MATCH:
                colored_text += f"\033[42m{letter}"
            elif result == Result.PARTIAL_MATCH:
                colored_text += f"\033[103m{letter}"
            else:
                colored_text += f"\033[40m{letter}"
    
        colored_text += "\033[0m"
        return colored_text
