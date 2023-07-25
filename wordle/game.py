from word import Word
from utils import get_text

class Game:
    def __init__(self, answer, language):
        self.answer = answer
        self.done = False
        self.number_of_guesses = 0
        self.language = language
        self.won = False

    def start(self):
        print(get_text('welcome', self.language))
        #print(self.answer) #uncomment for cheating purposes
        self._guess()

    def _guess(self):
        guess = input(get_text('guess', self.language))
        if len(guess) != 5:
            print(get_text('error_5_letters', self.language))
            self._guess()
        else: 
            word = Word(guess)
            self._check_word(word)        

    def _check_word(self, word):
        if (word.is_correct_word(self.answer)):
            print(get_text('win', self.language))
            self.won = True
            self.done = True
        else:
            print(word.compare_and_return_colorized_text(self.answer))
            self.number_of_guesses += 1
            self._check_game_done()
            if self.done == False:
                self._guess()

    def _check_game_done(self):
        if self.number_of_guesses > 5:
            print(get_text('lose', self.language) + self.answer)
            self.done = True
