# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                ViewsNames
# FILE VERSION:             1.0
# DATE:                     25.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains enum that is holding names of all views used in project
# ======================================================================================================================


from enum import Enum


class ViewsNames(Enum):
    INTRO = 1
    LUNCH_MENU = 2
    ADD_ALTERNATIVES = 3
    READ_ALTERNATIVES = 4
    SELECT_FILE_TO_LOAD = 5
    TREE_NODE = 6
    INSERT_FILE_NAME = 7
    EDIT_NODE_NAME = 8
    EDIT_PREFERENCES = 9
    ADD_SUB_FEATURE = 10
    SHOW_SUB_FEATURE = 11
    SHOW_PROJECT_TREE = 12
