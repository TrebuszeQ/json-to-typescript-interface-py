class TsType:
    @staticmethod
    def get_type(string: str):
        string = string.lower()
        types = {
            "object",
            "array",
            "boolean",
            "string",
            "number",
            "null",
            "undefined"
        }
        if types.__contains__(string):
            return string
        else:
            return "undefined"


