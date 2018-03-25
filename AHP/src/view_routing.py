# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                view_rutting
# FILE VERSION:             1.0
# DATE:                     17.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains class responsible for rutting views of terminal application.
# ======================================================================================================================

import curses
from .node import Node
from .views.intro_view import intro_view
from .views.add_alternatives_view import add_alternatives_view
from .views.launch_menu_view import launch_menu_view
from .views.select_file_to_load_view import select_file_to_load
from .views.read_alternative_view import read_alternative_view
from .views.tree_node_view import tree_node_view
from .utils.views_names import ViewsNames


class ViewRutting:
    def __init__(self): 
        self.alternatives = []
        self.root = Node()
        self.current_node = self.root
        self.screen = self.init_screen()
        self.running = True
        self.current_view = ViewsNames.INTRO
        self.views = {
            ViewsNames.INTRO: intro_view,
            ViewsNames.LUNCH_MENU: launch_menu_view,
            ViewsNames.ADD_ALTERNATIVES: add_alternatives_view,
            ViewsNames.READ_ALTERNATIVES: read_alternative_view,
            ViewsNames.SELECT_FILE_TO_LOAD: select_file_to_load,
            ViewsNames.TREE_NODE: tree_node_view,
            ViewsNames.INSERT_FILE_NAME: tree_node_view,
            ViewsNames.EDIT_NODE_NAME: tree_node_view,
            ViewsNames.EDIT_PREFERENCES: tree_node_view,
            ViewsNames.ADD_SUB_FEATURE: tree_node_view,
            ViewsNames.SHOW_SUB_FEATURE: tree_node_view
        }
            
    def run_app(self):
        while self.running:
            self.views[self.current_view](self)
        self.close_screen()

    @staticmethod
    def init_screen():
        screen = curses.initscr()
        curses.noecho()             
        curses.curs_set(0)          
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        screen.keypad(1)
        
        return screen
        
    def close_screen(self):
        self.screen.clear()
        curses.endwin()
        exit()
        
    def read_text_from_user(self, row, column):
        
        self.screen.addstr(row, column, " >> ")
        
        curses.echo()
        curses.curs_set(1)  
        
        input_text = self.screen.getstr(row, column + 4, 100).decode(encoding="utf-8")
        
        curses.noecho()             
        curses.curs_set(0)
        
        return input_text      