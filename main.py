import battle_functions
import sys

def main():
    print("Type help for all commands, type exit to close")
    while True:
        user_input = input("")
        user_input = remove_special_chars(user_input).lower().split()
        first_word = user_input[0]
        if first_word == "help":
            print_available_functions()
        if first_word == "weakness":
            pass
        if first_word == "exit":
            sys.exit()
    

def print_available_functions() -> None:
    pass

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



if __name__ == '__main__':
    main()
    