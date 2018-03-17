# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                Node
# FILE VERSION:             1.0
# DATE:                     17.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains class used to create tree structure of AHP criterias 
# ======================================================================================================================

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
        
    def updatePreferences(self, preferences, alternatives_size = None):
        tmp_preferences = json.loads(preferences)
        
        if alternatives_size:
            if (len(tmp_preferences) == alternatives_size and len(tmp_preferences[0]) == alternatives_size):
                self.preferences = tmp_preferences
        else:
            if (len(self.children) == len(tmp_preferences) and len(self.children) == len(tmp_preferences[0])):
                self.preferences = tmp_preferences