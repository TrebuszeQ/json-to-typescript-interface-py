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
    # returns content of the read file
    def _read_file(path):
        with open(path) as file:
            return file.read(-1)

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

    # change
    # matches input value to an action
    # @staticmethod
    # def delegate_input(input_int, content, root):
    #     match input_int:
    #
    #         case 0:
    #             os.system("clear" if os.name == "posix" else "cls")
    #
    #         case 1:
    #             return Cli.check_path(Cli.try_take_path())
    #
    #         case 2:
    #             return Cli.try_convert(content)
    #
    #         case 3:
    #             if root is not None:
    #                 return FileCreator.create_files(root)
    #             else:
    #                 print("No JSON was converted.")
    #                 return None
    #
    #         case 4:
    #             exit(1)
    #
    #         case _:
    #             print("Wrong input provided.\n")
    #             return False

    @staticmethod
    # checks if path exists and is JSON file.
    def _check_path(path):
        truth = False
        try:
            if os.path.exists(path):
                truth = True

            else:
                print("File doesn't exists.\n")

            if os.path.splitext(path)[1] != ".json":
                truth = False

            else:
                print("File is not a JSON file.\n")

        except ...:
            truth = False
            print("Path is invalid\n")

        if truth:
            return path
        else:
            return False

    @staticmethod
    # tries to return converted root
    def try_convert():
        try:
            root = convert(Cli._read_file(Cli._check_path(Cli._try_take_path())))
            return root

        except ReferenceError:
            print("Content is wrong.\n")

        except ...:
            print("Something went wrong.\n")

        return None
