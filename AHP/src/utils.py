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
from os import listdir
from os.path import isfile, join
import json

class Utils(object):
    
    @staticmethod
    def parseToDict(o):
        if type(o) == Node:
            return { key: o.__dict__[key] for key in ["name", "preferences", "children"]}
        else:
            return o.__dict__
        
    @staticmethod
    def saveModelToFile(model, filename, directory = "output"):
        with open(directory + "/" + filename, 'w') as outfile:  
            json.dump(model, outfile, default = lambda o: Utils.parseToDict(o), indent = 4)
            
    @staticmethod
    def getFilesInDir(directory = "output"):
        return [f for f in listdir(directory) if isfile(join(directory, f))]
    
    @staticmethod
    def getNode(dictionary, parent = None):
        new_node = Node()
        new_node.name = dictionary["name"]
        new_node.preferences = dictionary["preferences"]
        new_node.parent = parent
        
        if(dictionary["children"] == "alternatives"):
            new_node.children = dictionary["children"]
        else:
            new_node.children = [Utils.getNode(child, new_node) for child in dictionary["children"]]
            
        return new_node
    
    @staticmethod
    def loadModelFromFile(filename, directory = "output"):
        try:
            model_data = open(directory + "/" + filename).read()
            model_json = json.loads(model_data)        
            root = Utils.getNode(model_json["gole"])        
        except:
            return None, None    
        else:
            return root, model_json["alternatives"]