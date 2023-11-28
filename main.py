import os
from cli import Cli
from file_creator import FileCreator
import enum


# tries to take number of option
def try_take_option():
    try:
        input_str = input("Choose option:\n")
        input_int = int(input_str)

    except ValueError:
        input_int = -1

    return input_int


# main program
def main():
    input_str = ""
    input_int = 0
    content = None
    root = None
    result = None

    # probably needs to be converted to class
    options = {
        "Clear terminal": lambda: os.system("clear" if os.name == "posix" else "cls"),
        "Provide file path": lambda: Cli.check_path(Cli.try_take_path()),
        "Convert": lambda content_in: Cli.try_convert(content_in),
        "Create files": lambda obj: FileCreator.create_files(obj),
        "Exit": lambda: exit(1)
    }

    while input_int.__ne__(options.__sizeof__() - 1):
        Cli.print_options(options.keys(), "Options:")

        option = try_take_option()

        if option.__eq__(-1):
            print("Wrong input")
        lol = repr(options.values())
        lol[2]
        options.values()


main()
