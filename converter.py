from TsClass import TsClass
from TsType import TsType


def get_field_name(value: str, closing: int):
    field_name = value[0:closing]
    field_name_cleared = ""
    opening = 0
    for char in field_name:
        match char:
            case "{", "[", ",", "}", "]":
                opening += 1

            case _:
                field_name_cleared += char

    return field_name_cleared, opening


def find_desired(desired: str, value: str):
    char = desired[0]
    c = 0
    for char2 in value:
        if char.__eq__(char2):
            return c
        c += 1
    return str.__len__(value)


def ret_data_type(type_string: str, field_name: str, value: str, opening: int) -> list:
    data_type = TsType.get_type("null")
    truth = True
    closing_new = -2

    if str.__len__(type_string) > 0:
        c = 0
        while truth or c.__le__(str.__len__(field_name)):
            char = type_string[c]
            match char:
                case '[':
                    data_type = TsType.get_type("array")
                    closing_new = find_desired("]", value)
                    break

                case "{":
                    data_type = TsType.get_type("object")
                    closing_new = find_desired("}", value)
                    break

                case "f", "t":
                    if type_string.__contains__("true") or type_string.__contains__("false"):
                        data_type = TsType.get_type("boolean")
                    else:
                        data_type = TsType.get_type("string")
                    break

                case "n":
                    if type_string.__contains__("null"):
                        data_type = TsType.get_type("null")
                    else:
                        data_type = TsType.get_type("string")
                    break

                case _:
                    if str.isdigit(char):
                        data_type = TsType.get_type("number")
                        break
                    elif str.isalpha(char):
                        data_type = TsType.get_type("string")
                        break
                    else:
                        TsType.get_type("undefined")
            c += 1
        opening += c
    return [data_type, closing_new, opening]


def get_closing(char: chr, value: str):
    closing = None
    try:
        closing = value.index(char)

    except ...:
        closing = str.__len__(value)

    finally:
        if closing <= 0:
            closing = str.__len__(value)

    return closing


def get_new_val(value, opening, previous_object):
    new_val = previous_object.get_value()
    if value is None:
        trim_end = str.__len__(new_val) - opening - 1
        trim_start = opening + 1
        new_val = new_val[trim_start: abs(trim_end)]

    else:
        trim_end = str.__len__(new_val) - str.__len__(value) - opening
        trim_start = str.__len__(value) + opening
        new_val = new_val[trim_start, abs(trim_end)]

    return new_val


def is_field_name_none(field_name):
    if field_name is None:
        set_value(None)


def set_value(value):
    return value


def change_current_object_value(value, current_object):
    current_object.set_value(value)


def is_argument_none(arg):
    if arg is None:
        return True
    else:
        return False


# todo
def set_objects(data_type, trim_end, current_object, field_name):
    if data_type.__eq__(TsType.get_type("object")) or data_type.__eq__(TsType.get_type("array")):

        if trim_end > 0:
            value = set_value(value[opening: abs(trim_end)])
        else:
            value = set_value(None)

        # side effect
        current_object.set_child(TsClass(field_name, data_type, value, current_object))

        previous_object, current_object = current_object, TsClass(field_name, data_type, value, current_object)

        # side effect
        current_object.set_parent(previous_object)

        # side effect
        previous_object.set_value(get_new_val(value, opening, previous_object))
    else:
        trim_end = str.__len__(value) - closing_new - 1
        if trim_end < 0:
            value = set_value(None)
        else:
            value = set_value(value[(closing_new + 1):abs(trim_end)])

        # side effect
        change_current_object_value(value, current_object)

        # side effect
        current_object.set_child(TsClass(field_name, data_type, value[0:abs(closing)], current_object))


# todo
def traverse_over_value(value):
    while value is not None and str.__len__(value).__gt__(0):
        closing = get_closing(":", value)

        if closing <= 0:
            # side effect
            change_current_object_value(set_value(None), current_object)
            break

        field_name, opening = get_field_name(current_object.get_value(), closing)

        if is_argument_none(field_name).__eq__(True):
            # side effect
            change_current_object_value(set_value(None), current_object)
            break

        if current_object.is_child_present(field_name):
            # side effect
            change_current_object_value(None, current_object)
            break

        trim_end = str.__len__(value) - closing - 1
        # side effect
        change_current_object_value(set_value(value[(closing + 1):abs(trim_end)]), current_object)

        data_type, closing_new, opening = ret_data_type(value[0:abs(get_closing(",", value))], field_name,
                                                        current_object.get_value(), opening)

        if closing_new.__eq__(-2):
            closing_new = find_desired(",", value)

        trim_end = closing_new - opening
        set_objects(trim_end, )


# todo
def switch_objects_recursive(current_object, previous_object):
    if is_argument_none(current_object).__eq__(True):
        traverse_over_value(set_value(current_object.get_value()))

        current_object = previous_object

        if is_argument_none(current_object).__eq__(True):
            return current_object

        else:
            switch_objects_recursive(current_object, current_object.get_parent())


# too broad scope
def convert(content):

    current_object = TsClass("root", TsType.get_type("object"), content, None)
    previous_object = None

    while True:
        if is_argument_none(current_object).__eq__(True):
            value = set_value(current_object.get_value())

            while value is not None and str.__len__(value).__gt__(0):
                closing = get_closing(":", value)

                if closing <= 0:
                    # side effect
                    change_current_object_value(set_value(None), current_object)
                    break

                field_name, opening = get_field_name(current_object.get_value(), closing)

                if is_argument_none(field_name).__eq__(True):
                    # side effect
                    change_current_object_value(set_value(None), current_object)
                    break

                if current_object.is_child_present(field_name):
                    # side effect
                    change_current_object_value(None, current_object)
                    break

                trim_end = str.__len__(value) - closing - 1
                # side effect
                change_current_object_value(set_value(value[(closing + 1):abs(trim_end)]), current_object)

                data_type, closing_new, opening = ret_data_type(value[0:abs(get_closing(",", value))], field_name, current_object.get_value(), opening)

                if closing_new.__eq__(-2):
                    closing_new = find_desired(",", value)

                if data_type.__eq__(TsType.get_type("object")) or data_type.__eq__(TsType.get_type("array")):
                    trim_end = closing_new - opening
                    if trim_end > 0:
                        value = set_value(value[opening: abs(trim_end)])
                    else:
                        value = set_value(None)

                    # side effect
                    current_object.set_child(TsClass(field_name, data_type, value, current_object))

                    previous_object, current_object = current_object, TsClass(field_name, data_type, value, current_object)

                    # side effect
                    current_object.set_parent(previous_object)

                    # side effect
                    previous_object.set_value(get_new_val(value, opening, previous_object))
                else:
                    trim_end = str.__len__(value) - closing_new - 1
                    if trim_end < 0:
                        value = set_value(None)
                    else:
                        value = set_value(value[(closing_new + 1):abs(trim_end)])
                    # side effect
                    change_current_object_value(value, current_object)
                    # side effect
                    current_object.set_child(TsClass(field_name, data_type, value[0:abs(closing)], current_object))

        current_object = previous_object

        if current_object is None:
            break
        previous_object = current_object.get_parent()

    if content is not None:
        del content

    return current_object
