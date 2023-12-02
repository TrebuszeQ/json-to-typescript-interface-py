import unittest
from TsClass import TsClass


class TsClassCase(unittest.TestCase):
    def setUp(self):
        self._root = TsClass("root", "object", "lololololol", None)
        self._path = "/poke_api.json"

    def test_is_ts_class(self):
        self.assertIsInstance(self._root, TsClass, "root is not instance of TsClass.")

    def test_has_get_value_method(self):
        self.assertIsNotNone(self._root.get_value(), "Method get_value is None.")


if __name__ == '__main__':
    unittest.main()

