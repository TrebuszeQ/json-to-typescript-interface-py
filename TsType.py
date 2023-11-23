class TsType:
    @staticmethod
    def get_ts_type(item):
        if ({
            "object": 1,
            "array": 2,
            "boolean": 3,
            "string": 4,
            "number": 5,
            "null": 6,
            "undefined": 7}
                .__contains__(item)):
            return True
        else:
            return False
