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
    def read_file(path):
        with open(path) as file:
            return file.read(-1)

    @staticmethod
    # tries to take path from the user
    def try_take_path():
        path = None

        try:
            path = input("Provide path to JSON file:\n")

            if path is None:
                print("Path is None.\n")

            else:
                print("Path " + path + " is invalid.\n")

        except ...:
            print("Input is wrong.\n")

        return path

    @staticmethod
    # tries to return converted root
    def try_convert(content):
        try:
            root = convert(content)
            return root

        except ReferenceError:
            print("Content is wrong.\n")

        except ...:
            print("Something went wrong.\n")

        return None

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
