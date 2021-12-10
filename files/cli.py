from crypto import Crypto
from  colorama import Fore, init
from exceptions import EndGameException

init(autoreset=True)

class Cli():

    def __init__(self):
        self.crypto = Crypto()

    def display_encoded_quote(self):
        print(self.crypto.encoded_quote)

    def display_guessed_letters(self):
        print(Fore.GREEN + " ".join(self.crypto.original_ascii))
        print(" ".join(["\u2193" for i in range(26)]))
        print(Fore.GREEN + " " .join(self.crypto.alphabet_guessed), end='\n\n\n')

    def display_encoded_quote(self):
        print(Fore.GREEN + " ".join(self.crypto.encoded_quote))
        print(Fore.GREEN + " " .join(self.crypto.quote_guessed), end='\n\n\n')


c = Cli()
while (True):
    print("Welcome to the Cryptogrophers crypto canundrum, enter q to quit!!!")
    c.display_guessed_letters()
    c.display_encoded_quote()
    from_letter = input("Convert letter: ")
    if from_letter == 'q':
        raise EndGameException("Thanks for playing")
    to_letter = input("To letter: ")
    if to_letter == 'q':
        raise EndGameException("Thanks for playing")
    c.crypto.guess_letter(from_letter, to_letter)

