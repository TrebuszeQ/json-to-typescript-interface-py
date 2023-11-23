import TsClass as ts_class
import TsType as ts_type
import os

print("JSON to Ts class converter.\n")


def input_loop():
    input_str = ""
    input_int = 0
    path = None
    while input_int != 3:
        print("Options:")
        print("0. Clear terminal.")
        print("1. Provide file path.")
        print("2. Start.")
        print("3. Exit.")
        try:
            input_int = int(input_str)
        except ValueError:
            input_int = -1
        finally:
            match input_int:
                case 0:
                    try:
                        os.system("clear")
                    except:
                        os.system("cls")
                    break

                case 1:
                    try:
                        path = input("Provide path to JSON file.")
                    except:
                        print("Something went wrong.")
                    break

                case 2:
                    if path is not None:
                        try:
                            convert(path)

                        except FileNotFoundError:
                            print("File doesn't exists.")
                        except ReferenceError:
                            print("File is not a JSON file.")
                        except:
                            print("Something went wrong")

                    elif path is None:
                        print("Path is invalid.")
                    break

                case 3:
                    return

                case _:
                    print("Wrong option")


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


def convert(path):
    content = None
    if check_path(path):
        content = read_file(path)
    root = ts_class.TsClass("root", ts_type.TsType.ts_types["object"])
    x = ts_type.TsType.get_ts_types()
    if content is not None:
        del content
    return
