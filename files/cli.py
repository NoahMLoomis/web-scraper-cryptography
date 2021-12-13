from crypto import Crypto
from time import perf_counter
from colorama import Fore, init
from exceptions import EndGameException, InvalidLetterGuessException, FixingQuoteException

init(autoreset=True)


class Cli():

    def __init__(self):
        self.restart_game()
        self.start_time = perf_counter()
        self.end_time = 0

    def display_encoded_quote(self):
        print(self.crypto.encoded_quote)

    def display_guessed_letters(self):
        print(Fore.GREEN + " ".join(self.crypto.original_ascii))
        print(" ".join(["\u2193" for i in range(26)]))
        print(Fore.GREEN + " " .join(self.crypto.alphabet_guessed), end='\n\n\n')

    def display_encoded_quote(self):
        print(Fore.GREEN + " ".join(self.crypto.encoded_quote))
        print(Fore.GREEN + " " .join(self.crypto.quote_guessed), end='\n\n\n')

    def handle_input(self, letters):
        if letters.lower().strip() == 'quit':
            self.end_time = perf_counter()
            raise EndGameException(
                f"Thanks for playing, time was {self.end_time - self.start_time}")
        elif letters.lower().strip() == 'fix':
            self.crypto.fix_guessed_quote()
            raise FixingQuoteException("Fixing quote")
        elif letters.lower().strip() == 'hint':
            if self.crypto.hint_count >= 1:
                print("Do hint here")

    def is_command(self, letters):
        if letters.lower().strip() == "quit" and letters.lower().strip() == "hint" and letters.lower().strip() == "fix":
            return True
        return False

    def display_help_menu(self):
        print("""
              Commands:
                quit - quit
                hint - hint (only 1)
                fix - fix mistakes
              """)

    def restart_game(self):
        self.crypto = Crypto()


cli = Cli()
print("""Welcome to the Cryptographers crypto conundrum, enter q to quit!!!""")
cli.display_help_menu()
while (True):

    cli.display_guessed_letters()
    cli.display_encoded_quote()

    try:
        from_letter = input("Convert letter: ")
        cli.handle_input(from_letter)

        to_letter = input("To letter: ")
        cli.handle_input(to_letter)

        if not cli.is_command(from_letter) and not cli.is_command(to_letter):
            cli.crypto.guess_letter(from_letter, to_letter)
    except FixingQuoteException as e:
        print(f'{Fore.BLUE}{e}')
    except InvalidLetterGuessException as e:
        print(f'{Fore.RED}{e}')
    except EndGameException as e:
        print(f'{Fore.BLUE}{e}')
        cli.display_guessed_letters()
        cli.display_encoded_quote()
        if cli.crypto.is_game_won():
            play_again = input(f'{Fore.GREEN}You won!!! Play again [y/n]?')
            if play_again.upper() == "Y" or play_again.strip() == "":
                cli.restart_game()
            else:
                print(f'{Fore.BLUE}Thanks for playing :)')
                break
        else:
            print(f'{Fore.RED}You didn\'t guess everything right')
