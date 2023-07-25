import csv
import random
from game import Game
from utils import get_text

words_en = []
with open("./words-en.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
       words_en = words_en + row

words_fr = []
with open("./words-fr.csv", "r") as file_fr:
    csvreader = csv.reader(file_fr)
    for row in csvreader:
       words_fr = words_fr + row

class MainLoop:
    def __init__(self):
        self.current_game = None
        self._default_language = None
        self.games_finished = 0
        self.games_won = 0
        return
    
    def start(self):
        self._set_default_language()
        while True:
            self.current_game = Game(self._get_random_word(), self.default_language)
            self.current_game.start()
            if self.current_game.done == True:
                self._handle_game_done()

    @property
    def default_language(self):
        return self._default_language
  
    @default_language.setter
    def default_language(self, value):
        if (value == 'E'):
            self._default_language = 'en'
        else:
            self._default_language = 'fr'

    def _set_default_language(self):
        lg_input = input('E for english / F pour français: ')
        if (lg_input.upper() != 'E' and lg_input.upper() != 'F'):
            self._set_default_language()
        else:
            self.default_language = lg_input

    def _get_random_word(self):
        if self.default_language == 'en':
            return random.choice(words_en)
        else:
            return random.choice(words_fr)

    def _handle_game_done(self):
        self._adjust_score()
        self._print_score()
        start_new_game = input(get_text('play_again', self.default_language))
        if start_new_game.upper() == 'Y' or start_new_game.upper() == 'O':
            self.current_game = Game(self._get_random_word(), self.default_language)
        else:
            quit()

    def _adjust_score(self):
        self.games_finished += 1
        if self.current_game.won:
            self.games_won += 1

    def _print_score(self):
        print(get_text('score', self.default_language, [str(self.games_finished), str(self.games_won)]))
        success_rate = round((self.games_won / self.games_finished) * 100)
        print(get_text('score_percent', self.default_language, [str(success_rate)]))