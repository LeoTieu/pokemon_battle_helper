import battle_functions
import sys
from os import system

clear_words = ("clear", "clr", "c")
weakness_words = ("w", "weak", "weakness")

def main():
    print("Type help for all commands, type exit to close")
    while True:
        user_input = input("")
        user_input = remove_special_chars(user_input).lower().split()
        first_word = user_input[0]
        if first_word == "help":
            if len(user_input) == 1:
                print_new_line()
                print_available_functions()
            else:
                print("Not available right now")

        elif first_word in weakness_words:
            print_new_line()
            battle_functions.print_coverage_for_pokemon(user_input[1])

        elif first_word in clear_words:
            system('cls')
            print("Type help for all commands, type exit to close")

        elif first_word == "exit":
            sys.exit()
            
        else:
            print_new_line()
            print("command not found")


def print_available_functions() -> None:
    print("Commands available are:")
    print("help, clear, weakness")
    print("To know what a function does, type 'help + command'")

def remove_special_chars(input_string: str) -> str:
    """Removes special characters from a given string
    A bit slow in theory but fast in practice.
    """
    normal_chars = set("abcdefghijklmnopqrstuvwxyz ")
    clean_string = ""

    for char in input_string:
        if char in normal_chars:
            clean_string += char
    return clean_string


def print_new_line() -> None:
    '''Prints a new line in terminal'''
    print("")


if __name__ == '__main__':
    main()
