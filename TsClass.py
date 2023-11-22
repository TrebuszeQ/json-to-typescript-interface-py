class TsClass:
    child = None
    children = None

    def __init__(self, class_name, dtype, value, parent):
        self.data_type = dtype
        self.parent = parent
        self.class_name = class_name
        self.value = value
        self.initial_value = value

    def set_parent(self, member):
        if self.parent is None:
            self.parent = member

    def get_parent(self):
        return self.parent

    def set_child(self, child):
        if child is None: self.child = child
        elif child is not None and self.children is None:
            self.init_children(child)
        elif child is not None and self.children is not None:
            self.append_children(child)

    def init_children(self, child):


    def append_children(self, child):

