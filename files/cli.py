from crypto import Crypto
from time import perf_counter
from colorama import Fore, init
from exceptions import EndGameException, InvalidLetterGuessException, FixingQuoteException, GiveHintException, QuitGameException

init(autoreset=True)


class Cli():

    def __init__(self):
        self.restart_game()
        self.start_time = perf_counter()
        self.end_time = 0

    def display_guessed_letters(self):
        print(Fore.BLUE + " ".join(self.crypto.original_ascii))
        print(" ".join(["\u2193" for i in range(26)]))
        print(Fore.BLUE + " " .join(self.crypto.alphabet_guessed), end='\n\n\n')

    def display_encoded_quote(self):
        # The following line is for testing, to see what your quote is as you're decoding it
        # print(" ".join(self.crypto.decoded_quote))
        print(Fore.GREEN + " ".join(self.crypto.encoded_quote))
        print(Fore.GREEN + " " .join(self.crypto.quote_guessed), end='\n\n\n')

    def handle_input(self, letters):
        if letters.lower().strip() == 'quit':
            raise QuitGameException()
        elif letters.lower().strip() == '!':
            self.crypto.fix_guessed_quote()
            raise FixingQuoteException("Fixing quote")
        elif letters.lower().strip() == '?':
            if self.crypto.hint_count >= 1:
                raise InvalidLetterGuessException(
                    "Only one hint is allowed per game")
            self.crypto.get_hint()
            raise GiveHintException("Hint given")

    def is_command(self, letter):
        if letter.lower().strip() == "quit" or letter.lower().strip() == "?" or letter.lower().strip() == "!":
            return True
        return False

    def get_time(self):
        return self.end_time - self.start_time

    def display_help_menu(self):
        print("""
              Commands:
                quit - quit
                ? - hint (only 1)
                ! - fix mistakes
              """)

    def restart_game(self):
        self.crypto = Crypto()

if __name__ == "__main__":
    cli = Cli()
    print("\nWelcome to the Cryptographers crypto conundrum, enter q to quit!!!")
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

        except (FixingQuoteException, GiveHintException) as e:
            print(f'{Fore.BLUE}{e}')
        except InvalidLetterGuessException as e:
            print(f'{Fore.RED}{e}')

        except QuitGameException:
            cli.end_time = perf_counter()
            play_again = input(
                f'{Fore.GREEN}Time was {cli.get_time():0.2f} seconds Play again? (Default is n) [y/n] ')
            if play_again.upper() == "N" or play_again.strip() == "":
                print(f'{Fore.BLUE}Thanks for playing :)')
                break
            else:
                cli.restart_game()
        except EndGameException as e:
            print(f'{Fore.BLUE}{e}')
            cli.display_guessed_letters()
            cli.display_encoded_quote()

            cli.end_time = perf_counter()
            if cli.crypto.is_game_won():
                print(f"The quote was: {cli.crypto.decoded_quote}")
                play_again = input(
                    f'{Fore.GREEN}You won!!! It took you {cli.get_time():0.2f} seconds. Play again? (Default is y) [y/n] ')
                print(f"The quote was {cli.crypto.decoded_quote}")
                if play_again.upper() == "Y" or play_again.strip() == "":
                    cli.restart_game()
                else:
                    print(f'{Fore.BLUE}Thanks for playing :)')
                    break
            else:
                print(f'{Fore.RED}You didn\'t guess everything right')
