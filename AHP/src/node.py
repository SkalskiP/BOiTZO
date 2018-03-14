class Node(object):
    def __init__(self):
        self.name = None
        self.preferences = []
        self.children = []
        self.parent = None

    def add_child(self, obj):
        self.children.append(obj)