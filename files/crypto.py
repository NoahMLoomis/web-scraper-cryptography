from string import ascii_uppercase
from random import sample
from exceptions import InvalidLetterGuessException
from quote import Quote


class Crypto():
    def __init__(self):
        self.quote_generator = Quote()
        test_list = ['D', 'O', 'G', ' ', 'I', 'S', ' ', 'F', 'A', 'T']
        self.alphabet_guessed = ['_' for i in range(26)]
        self.original_ascii = ascii_uppercase
        self.mixed_ascii = ''.join(
            sample(list(self.original_ascii), len(self.original_ascii)))

        self.do_encoding = self.make_cipher(
            self.original_ascii, self.mixed_ascii)
        self.decoded_quote = self.quote_generator.get_random_quote()
        self.encoded_quote = self.do_encoding(self.decoded_quote)
        # self.quote_dict = {test_list[i]: 0 for i in range(len(test_list))}
        self.quote_dict = {self.encoded_quote[i]: 0 for i in range(len(self.encoded_quote))}
        self.quote_guessed = []
        for letter in self.encoded_quote:
            if letter.isalpha():
                self.quote_guessed.append("_")
            else:
                self.quote_guessed.append(" ")

    def change_guessed_alphabet(self, from_letter, to_letter):
        self.alphabet_guessed[ascii_uppercase.index(
            from_letter.upper())] = to_letter.upper()

    def change_guessed_quote(self, from_letter, to_letter):
        letters_to_change = []
        for i in range(len(self.encoded_quote)):
            if self.encoded_quote[i] == from_letter.upper():
                letters_to_change.append(i)
        print(letters_to_change)
        
        for i in letters_to_change:
            self.quote_guessed[i] = to_letter.upper()
    def guess_letter(self, from_letter, to_letter):
        if from_letter.upper() not in self.quote_dict:
            raise InvalidLetterGuessException(
                f'{from_letter.upper()} is not a a valid letter')
        self.change_guessed_alphabet(from_letter, to_letter)
        self.change_guessed_quote(from_letter, to_letter)

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
