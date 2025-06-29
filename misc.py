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
