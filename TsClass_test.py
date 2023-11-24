import unittest
from TsClass import TsClass


class MyTestCase(unittest.TestCase):
    _root = TsClass("root", "object", "lololololol", None)


    def is_ts_class(self):
        if isinstance(self._root, TsClass).__eq__(False):
            return False
        #here


    def has_get_value_method(self):
        try:
            value = self._root.get_value()
            print(value)
            if value is None:
                raise Exception("value is None")
        except Exception as e:
            print(e)
            return False
        return True


if __name__ == '__main__':
    unittest.main()
    test = MyTestCase()
    if MyTestCase.is_ts_class().__eq__(False)
    MyTestCase.has_get_value_method()