# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                Utils
# FILE VERSION:             1.0
# DATE:                     17.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains set of static methods responsible for parsing tree structure to JSON as well as saving it to file
# ======================================================================================================================

from .node import Node
import json

class Utils(object):
    
    @staticmethod
    def parseToDict(o):
        if type(o) == Node:
            return { key: o.__dict__[key] for key in ["name", "preferences", "children"]}
        else:
            return o.__dict__
        
    @staticmethod
    def saveModelToFile(model, filename):
        with open("output/" + filename, 'w') as outfile:  
            json.dump(model, outfile, default = lambda o: Utils.parseToDict(o), indent = 4)