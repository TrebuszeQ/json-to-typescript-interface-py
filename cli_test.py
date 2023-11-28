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

    def test_delegate_case_1(self):
        path = "/home/trebuszeq/Py/json-to-ts/test.json"

        truth = Cli.delegate_input("", root=self._root)

        print("output", str.__len__(output))
        print("path", path)
        self.assertEqual(path, output)




if __name__ == '__main__':
    unittest.main()
