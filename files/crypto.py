from string import ascii_uppercase
from random import sample, choice
from exceptions import InvalidLetterGuessException, EndGameException
from quote import Quote


class Crypto():
    def __init__(self):
        self.quote_generator = Quote()
        self.hint_count = 0
        self.alphabet_guessed = ['_' for i in range(26)]
        self.original_ascii = ascii_uppercase
        self.mixed_ascii = ''.join(
            sample(list(self.original_ascii), len(self.original_ascii)))

        self.do_encoding = self.make_cipher(
            self.original_ascii, self.mixed_ascii)
        self.decoded_quote = self.quote_generator.get_random_quote()
        self.encoded_quote = self.do_encoding(self.decoded_quote)
        self.decoded_quote = 'dk'
        self.encoded_quote = ['D', 'K']

        # self.quote_dict = {test_list[i]: 0 for i in range(len(test_list))}
        self.quote_dict = {
            self.encoded_quote[i]: 0 for i in range(len(self.encoded_quote))}
        self.quote_guessed = []
        for letter in self.encoded_quote:
            if letter.isalpha():
                self.quote_guessed.append("_")
            else:
                self.quote_guessed.append(" ")

    def change_guessed_alphabet(self, from_letter, to_letter):
        if to_letter.strip() == "":
            self.alphabet_guessed[ascii_uppercase.index(
                from_letter.upper())] = "_"
        else:
            self.alphabet_guessed[ascii_uppercase.index(
                from_letter.upper())] = to_letter.upper()

    def change_guessed_quote(self, from_letter, to_letter):
        letters_to_change = []
        for i in range(len(self.encoded_quote)):
            if self.encoded_quote[i] == from_letter.upper():
                letters_to_change.append(i)
        for i in letters_to_change:
            if to_letter.strip() == "":
                self.quote_guessed[i] = "_"
            else:
                self.quote_guessed[i] = to_letter.upper()

    def fix_guessed_quote(self):
        for i in range(len(self.encoded_quote)):
            if self.quote_guessed[i].isalpha():
                self.quote_guessed[i] = self.decoded_quote[i].upper()
                self.change_guessed_alphabet(self.quote_guessed[i], self.decoded_quote[i])

    def is_letter_in_code(self, from_letter):
        if from_letter.upper() not in self.quote_dict:
            raise InvalidLetterGuessException(
                f'{from_letter.upper()} is not a a valid letter')

    def guess_letter(self, from_letter, to_letter):
        self.is_letter_in_code(from_letter)
        self.change_guessed_alphabet(from_letter, to_letter)
        self.change_guessed_quote(from_letter, to_letter)
        self.is_game_over()

    def make_cipher(self, original, mixed):
        def code_string(the_string):
            def code_letter(letter):
                if letter.isalpha():
                    return mixed[original.index(letter.upper())]
                return letter
            return ''.join(list(map(code_letter, the_string)))
        return code_string

    def get_quote_letters(self):
        return [self.encoded_quote[i] for i in range(len(self.encoded_quote)) if self.encoded_quote[i].isalpha()]

    # Try to improve this, not very robust
    def is_game_over(self):
        if "_" not in self.quote_guessed:
            raise EndGameException("Game is over")

    def is_game_won(self):
        t = "".join(self.quote_guessed).upper()
        if "".join(self.quote_guessed).upper() == self.decoded_quote.upper():
            return True
        return False
