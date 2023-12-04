class TsClass:
    __data_type = None
    __class_name = None
    __value = None
    __initial_value = None
    __child = None
    __children = None
    __parent = None

    def __init__(self, class_name, dtype, value, parent):
        self.__data_type = dtype
        self.__parent = parent
        self.__class_name = class_name
        self.__value = value
        self.__initial_value = value

    def set_parent(self, member):
        if self.__parent is None:
            self.__parent = member

    def get_parent(self):
        return self.__parent

    def set_child(self, child):
        if child is None:
            self.__child: TsClass = child
        elif child is not None and self.__children is None:
            self.init_children(child)
        elif child is not None and self.__children is not None:
            self.append_children(child)

    def init_children(self, child):
        self.__children: list[TsClass] = list(child)

    def append_children(self, child):
        self.__children.__add__(child)

    def get_child(self):
        return self.__child

    def get_cname(self):
        return self.__class_name

    def set_cname(self, name):
        self.__class_name = self.__clear_name(name)

    @staticmethod
    def __clear_name(name: str):
        chars = ['\\', '}', ']', '{', '[', '"', ':']
        new_name = ""
        truth: bool = True
        for char in name:
            for sym in chars:
                if char.__eq__(sym):
                    truth = False
            if truth:
                new_name.__add__(char)
            truth = True
        return new_name

    def get_dtype(self):
        return self.__data_type

    def set_dtype(self, dtype):
        self.__data_type = dtype


    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_initial_value(self):
        return self.__initial_value

    def set_initial_value(self, value):
        self.__initial_value = value

    def is_child_present(self, class_name):
        class_name = self.__clear_name(class_name)
        if self.__children.__ne__(None) and len(self.__children).__gt__(0):
            for indice in self.__children:
                if indice.__class_name.__eq__(class_name):
                    return True
        return False
