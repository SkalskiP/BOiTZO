# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                file_utils
# FILE VERSION:             1.0
# DATE:                     17.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains set of static methods responsible for parsing tree structure to JSON as well as saving it to file
# ======================================================================================================================

from src.node import Node
from os import listdir
from os.path import isfile, join
import json
from collections import OrderedDict as OD


class FileUtils:

    @staticmethod
    def parse_to_dict(o):
        if type(o) == Node:
            return {key: o.__dict__[key] for key in ["name", "preferences", "children"]}
        else:
            return o.__dict__

    @staticmethod
    def save_model_to_file(model, filename, directory="output"):
        with open(directory + "/" + filename, 'w') as outfile:
            json.dump(model, outfile, default=lambda o: FileUtils.parse_to_dict(o), indent=4)

    @staticmethod
    def get_files_in_dir(directory="output"):
        return [f for f in listdir(directory) if isfile(join(directory, f))]

    @staticmethod
    def get_node(dictionary, parent=None):
        new_node = Node()
        new_node.name = dictionary["name"]
        new_node.preferences = dictionary["preferences"]
        new_node.parent = parent

        if dictionary["children"] == "alternatives":
            new_node.children = dictionary["children"]
        else:
            new_node.children = [FileUtils.get_node(child, new_node) for child in dictionary["children"]]

        return new_node

    @staticmethod
    def get_brief_tree(root, alternatives):
        if root.children == "alternatives":
            return OD([(alternative, {}) for alternative in alternatives])
        else:
            return OD([(child.name, FileUtils.get_brief_tree(child, alternatives)) for child in root.children])

    @staticmethod
    def load_model_from_file(filename, directory="output"):
        try:
            model_data = open(directory + "/" + filename).read()
            model_json = json.loads(model_data)
            root = FileUtils.get_node(model_json["goal"])
        except:
            return None, None
        else:
            return root, model_json["alternatives"]
