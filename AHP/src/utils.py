from .node import Node

class Utils(object):
    
    @staticmethod
    def parseToDict(o):
        if type(o) == Node:
            return { key: o.__dict__[key] for key in ["name", "preferences", "children"]}
        else:
            return o.__dict__