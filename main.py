import os
from converter import convert


def input_loop():
    input_str = ""
    input_int = 0
    path = None
    while input_int != 3:
        print("Options:")
        print("0. Clear terminal.")
        print("1. Provide file path.")
        print("2. Convert.")
        print("3. Exit.\n")
        try:
            input_str = input("Choose option:\n")
            input_int = int(input_str)
        except ValueError:
            input_int = -1
        finally:
            match input_int:
                # exception immune handling
                case 0:
                    try:
                        os.system("cls")

                    except ...:
                        os.system("clear")
                    break

                case 1:
                    try:
                        path = input("Provide path to JSON file:\n")

                    except ...:
                        print("Input is wrong.\n")
                    break

                case 2:
                    if check_path(path):
                        try:
                            content = read_file(path)
                            convert(content)

                        except FileNotFoundError:
                            print("File doesn't exists.\n")

                        except ReferenceError:
                            print("File is not a JSON file.\n")

                        except ...:
                            print("Something went wrong.\n")

                    elif path is None:
                        print("Path is invalid.\n")
                    break

                case 3:
                    exit(1)

                case _:
                    print("Wrong input provided.\n")


def check_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError
    elif not os.path.splitext(path):
        raise ReferenceError
    return True


def read_file(path):
    with open(path) as file:
        content = file.read(-1)
        return content


input_loop()
