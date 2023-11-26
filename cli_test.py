import sys
import unittest
import io
from cli import print_options
from cli import input_loop


class TestMain(unittest.TestCase):

    # tests if print_options prints to the console
    def test_print_options(self):
        options = ["option1", "option2"]
        message = "message"

        buffer = io.StringIO()
        sys.stdout = buffer
        # execute output
        print_options(options, message)

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

    def test_input_loop_case_1(self):
        input_str = "1"
        input_int = 1
        pass


if __name__ == '__main__':
    unittest.main()
