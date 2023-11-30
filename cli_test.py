import sys
import unittest
import io
from cli import Cli
from TsClass import TsClass


class TestMain(unittest.TestCase):
    def setUp(self):
        self._root = TsClass("root", "object", "lololololol", None)

    # tests if print_options prints to the console
    def test_print_options(self):
        options = ["option1", "option2"]
        message = "message"

        buffer = io.StringIO()
        sys.stdout = buffer
        # execute output
        Cli.print_options(options, message)

        output = buffer.getvalue()

        truth = False

        if output.__contains__(message):
            truth = True

        c = 0
        for opt in options:
            if not output.__contains__(str(c) + ". " + opt + ".\n"):
                truth = False
            c += 1

        self.assertTrue(truth)

    def test_read_file(self, path: str):
        exist = "/home/trebuszeq/Py/json-to-ts"
        wrong_path = "nopath"
        good_path = "/home/trebuszeq/Py/json-to-ts/test.json"





if __name__ == '__main__':
    unittest.main()
