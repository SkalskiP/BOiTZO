import json

class Node(object):
    def __init__(self):
        self.name = None
        self.preferences = []
        self.children = []
        self.parent = None
        
    def isLief(self):
        return(type(self.children) is not list)
        
    def setAsLief(self, alternatives_size):
        self.children = "alternatives"
        self.buildBlankPreferences(alternatives_size)
        
    def setAsBrunch(self):
        self.children = []
        self.preferences = []
        
    def addChildWithName(self, name):
        if not self.isLief():
            child = Node()
            child.name = name
            child.parent = self
            self.children.append(child)
            self.buildBlankPreferences(len(self.children))
        
    def buildBlankPreferences(self, size):
        self.preferences = []
        for i in range(size):
            self.preferences.append([0] * size)
            
    def preferencesToString(self):
        return(json.dumps(self.preferences))