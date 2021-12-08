from string import ascii_uppercase
from random import sample
from quote import Quote


class Crypto():
    def __init__(self):
        self.quote_generator = Quote()
        self.original_ascii = ascii_uppercase
        self.mixed_ascii = ''.join(sample(list(self.original_ascii), len(self.original_ascii)))

        self.do_encoding = self.make_cipher(self.original_ascii, self.mixed_ascii)
        self.decoded_quote = self.quote_generator.get_random_quote()
        self.encoded_quote = self.do_encoding(self.decoded_quote)
        
    def make_cipher(self, original, mixed):
        def code_string(the_string):
            def code_letter(letter):
                if letter.isalpha():
                    return mixed[original.index(letter.upper())]
                return letter
            return ''.join(list(map(code_letter, the_string)))
        return code_string

c= Crypto()