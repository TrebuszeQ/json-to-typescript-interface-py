import os
from converter import convert
from file_creator import FileCreator


class Cli:
    # prints output and message
    @staticmethod
    def print_options(options, message):
        c = 0

        print(message)
        for opt in options:
            print(str(c) + ". " + opt + ".")
            if c.__eq__(len(options) - 1):
                print()
            c += 1

    @staticmethod
    # tries to take path from the user
    def _try_take_path():
        path = None

        try:
            path = input("Provide path to JSON file:\n")

            if path is None:
                print("Path is None.\n")

        except ...:
            print("Path " + path + " is invalid.\n")

        return path

    @staticmethod
    # returns content of the read file
    def _read_file(path):
        with open(path) as file:
            return file.read(-1)

    @staticmethod
    # checks if path exists and is JSON file.
    def _check_path(path):
        truth = False
        try:
            if os.path.exists(path):
                truth = True
                if os.path.splitext(path)[1].__ne__(".json"):
                    truth = False
                    print("File is not a JSON file.\n")

            else:
                print("File doesn't exists.\n")

        except ...:
            truth = False
            print("Path is invalid\n")

        if truth:
            return path
        else:
            return False

    @staticmethod
    # tries to return converted root
    def try_convert(path):
        content: str
        if path is None:
            content = Cli._read_file(Cli._check_path(Cli._try_take_path())).replace(" ", "")

        elif path is not None:
            content = Cli._read_file(path).replace(" ", "")

        truth = True
        root = None
        try:
            root = convert(content)

        except ReferenceError or BaseException:
            print("Content is wrong.\n")
            truth = True

        except ...:
            print("Something went wrong.\n")
            truth = True

        if truth:
            return root
        return None
