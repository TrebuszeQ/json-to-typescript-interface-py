import sys
import unittest
import io
from unittest.mock import patch
# my
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

    @patch(target='builtins.input', side_effect=["/home/trebuszeq/Py/json-to-ts/test.json"])
    def test_try_take_path_valid(self, mock_input):
        path = Cli._try_take_path()
        self.assertEqual(path, "/home/trebuszeq/Py/json-to-ts/test.json")

    @patch(target="builtins.input", side_effect=["/invalid/path"])
    def test_try_take_path_invalid(self, mock_input):
        path = Cli._try_take_path()
        self.assertEqual(path, "/invalid/path")

    def test_read_file_w_valid_path(self, test_path="/home/trebuszeq/Py/json-to-ts/test.json"):
        content: str
        with open(test_path) as file:
            content = file.read(-1)

        content2 = Cli._read_file(test_path)
        self.assertEqual(content2, content)

    def test_try_check_path_valid(self, test_path="/home/trebuszeq/Py/json-to-ts/test.json"):
        result = Cli._check_path(test_path)
        self.assertEqual(result, test_path)

    def test_try_check_path_invalid(self, test_path="invalid_path"):
        result = Cli._check_path(test_path)
        self.assertFalse(result)

    def test_try_check_path_no_json(self, test_path="/home/trebuszeq/Py/json-to-ts"):
        result = Cli._check_path(test_path)
        self.assertFalse(result)

    def test_try_convert_valid_path(self, test_path="/home/trebuszeq/Py/json-to-ts/test.json"):
        result = Cli.try_convert(path=test_path)
        self.assertIsInstance(result, TsClass)


if __name__ == '__main__':
    unittest.main()
