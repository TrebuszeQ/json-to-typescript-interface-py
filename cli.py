import os
from converter import convert
from file_creator import FileCreator


# prints output and message
def print_options(options, message):
    c = 0

    print(message)
    for opt in options:
        print(str(c) + ". " + opt + ".")
        if c.__eq__(len(options) - 1):
            print()
        c += 1


# takes input and delegates output
def input_loop():
    input_str = ""
    input_int = 0
    path = None
    content = None
    root = None

    while input_int.__ne__(4):
        print_options([
            "Clear terminal",
            "Provide file path",
            "Convert",
            "Create files",
            "Exit"
        ], "Options:")

        try:
            input_str = input("Choose option:\n")
            input_int = int(input_str)

        except ValueError:
            input_int = -1

        finally:
            match input_int:

                case 0:
                    os.system("clear" if os.name == "posix" else "cls")

                case 1:
                    try:
                        path = input("Provide path to JSON file:\n")
                        if path is None:
                            print("Path is None.\n")
                        elif check_path(path) is True:
                            try:
                                content = read_file(path)
                            except ...:
                                print("File couldn't been read.")
                        else:
                            print("Path " + path + " is invalid.\n")
                    except ...:
                        print("Input is wrong.\n")

                case 2:
                    try:
                        root = convert(content)
                    except ReferenceError:
                        print("Content is wrong.\n")
                    except ...:
                        print("Something went wrong.\n")

                case 3:
                    if root is not None:
                        FileCreator.create_files(root)
                    else:
                        print("No JSON was converted.")

                case 4:
                    exit(1)

                case _:
                    print("Wrong input provided.\n")


def check_path(path):
    truth = False
    try:
        if os.path.exists(path):
            print("File doesn't exists.\n")
            truth = True

        if os.path.splitext(path)[1] != ".json":
            print("File is not a JSON file.\n")
            truth = False

    except ...:
        truth = False

    return truth


def read_file(path):
    with open(path) as file:
        content = file.read(-1)
        return content
