# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                ViewRutting
# FILE VERSION:             1.0
# DATE:                     17.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains class responsible for rutting views of terminal aplication
# ======================================================================================================================

import curses
from .node import Node
from .views.intro_view import introView
from .views.add_alternatives_view import addAlternativesView
from .views.launch_menu_view import launchMenuView
from .views.select_file_to_load_view import selectFileToLoad
from .views.read_alternative_view import readAlternativeView
from .views.tree_node_view import treeNodeView

class ViewRutting(object):
    def __init__(self): 
        self.alternatives = []
        self.root = Node()
        self.current_node = self.root
        self.screen = self.initScreen()
        self.running = True
        self.current_view = "lunch_menu_view"
        self.views = {
            "intro_view": introView,
            "lunch_menu_view": launchMenuView,
            "add_alternatives_view": addAlternativesView,
            "read_alternative_view": readAlternativeView,
            "select_file_to_load": selectFileToLoad,
            "tree_node_view": treeNodeView,
            "insert_file_name": treeNodeView,
            "edit_name": treeNodeView,
            "edit_preferences": treeNodeView,
            "add_sub_feature": treeNodeView,
            "sub_feature_view": treeNodeView
        }
            
    def runApp(self):
        while(self.running):
            self.views[self.current_view](self)
        self.closeScreen()
        
    def initScreen(self):
        screen = curses.initscr()
        curses.noecho()             
        curses.curs_set(0)          
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        screen.keypad(1)
        
        return screen
        
    def closeScreen(self):
        self.screen.clear()
        curses.endwin()
        exit()
        
    def readTextFromUser(self, row, column):
        
        self.screen.addstr(row, column, " >> ")
        
        curses.echo()
        curses.curs_set(1)  
        
        input_text = self.screen.getstr(row, column + 4, 100).decode(encoding="utf-8")
        
        curses.noecho()             
        curses.curs_set(0)
        
        return input_text      