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


class Node:
    def __init__(self):
        self.name = None
        self.preferences = []
        self.children = []
        self.parent = None

    def is_lief(self):
        return type(self.children) is not list

    def set_as_lief(self, alternatives_size):
        self.children = "alternatives"
        self.build_blank_preferences(alternatives_size)

    def set_as_brunch(self):
        self.children = []
        self.preferences = []

    def add_child_with_name(self, name):
        if not self.is_lief():
            child = Node()
            child.name = name
            child.parent = self
            self.children.append(child)
            self.build_blank_preferences(len(self.children))

    def build_blank_preferences(self, size):
        self.preferences = []
        for i in range(size):
            self.preferences.append([0] * size)

    def preferences_to_string(self):
        return json.dumps(self.preferences)

    def update_preferences(self, preferences, alternatives_size=None):
        try:
            tmp_preferences = json.loads(preferences)
        except:
            return
        else:
            if alternatives_size:
                if len(tmp_preferences) == alternatives_size and len(tmp_preferences[0]) == alternatives_size:
                    self.preferences = tmp_preferences
            else:
                if len(self.children) == len(tmp_preferences) and len(self.children) == len(tmp_preferences[0]):
                    self.preferences = tmp_preferences
