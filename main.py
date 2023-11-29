import os
from cli import Cli
from file_creator import FileCreator
from TsClass import TsClass


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
    path = None
    content = None
    root = None

    # probably needs to be converted to class
    options = {
        "Clear terminal": (lambda: os.system("clear" if os.name == "posix" else "cls")),
        "Convert": (lambda: Cli.try_convert()),
        "Create files": (lambda: FileCreator.create_files(root)),
        "Exit": (lambda: exit(1))
    }

    while input_int.__ne__(options.__sizeof__() - 1):
        Cli.print_options(options.keys(), "Options:")

        option = try_take_option()
        c = 0

        for key in options.keys():
            if option.__eq__(c):
                result = options.__getitem__(key)()
                if type(result) is TsClass:
                    root = result
            c += 1


if __name__.__eq__("__main__"):
    main()
