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
        with open(filename, 'w') as outfile:  
            json.dump(model, outfile, default=lambda o: Utils.parseToDict(o), indent = 4)