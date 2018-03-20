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
from .utils import Utils

class ViewRutting(object):
    def __init__(self): 
        self.alternatives = []
        self.root = Node()
        self.current_node = self.root
        self.screen = self.initScreen()
        
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
        
    def readFromUser(self, row, column):
        
        self.screen.addstr(row, column, " >> ")
        
        curses.echo()
        curses.curs_set(1)  
        
        input_text = self.screen.getstr(row, column + 4, 100).decode(encoding="utf-8")
        
        curses.noecho()             
        curses.curs_set(0)
        
        return input_text
    
    def introView(self, name):
        
        with open(name) as f:
            content = f.readlines()
            
        for index, line in enumerate(content):
            self.screen.addstr(index + 1, 4, line)
            
        self.screen.getch()
        
    def launchMenuView(self):

        selection = -1
        option = 0
    
        while selection < 0:
            self.screen.clear()
            
            h = [0] * 5
            h[option] = curses.color_pair(1)
    
            self.screen.addstr(1, 4, "Please select an option...", curses.A_BOLD)
            self.screen.addstr(3, 4, "1 - Add alternatives", h[0])
            self.screen.addstr(4, 4, "2 - Build hierarchy of features", h[1])
            self.screen.addstr(5, 4, "3 - Save as JSON file", h[2])
            self.screen.addstr(6, 4, "4 - Load from JSON file", h[3])
            self.screen.addstr(8, 4, "5 - Exit ('q')", h[4])
            
            q = self.screen.getch()
            
            if q == curses.KEY_UP:
                option = (option - 1) % len(h)
            elif q == curses.KEY_DOWN:
                option = (option + 1) % len(h)
            elif q == ord('\n'):
                selection = option
                
            if selection == 0 :
                self.addAlternativesView()
            elif selection == 1 :
                self.treeNodeView("view")
            elif selection == 2 :
                self.treeNodeView("insert_file_name")
            elif selection == 3 :
                self.selectFileToLoad()
            elif q == ord('q') or selection == len(h) -1 :
                self.closeScreen()
        
    def addAlternativesView(self):
        
        selection = -1
        option = 0
        
        while selection < 0:
            self.screen.clear()
            
            h = [0] * 2
            h[option] = curses.color_pair(1)
            
            if len(self.alternatives) == 0:
                self.screen.addstr(1, 4, "You have no alternatives yet...", curses.A_BOLD)
            else:
                self.screen.addstr(1, 4, "Alternatives: {}".format(", ".join(self.alternatives)), curses.A_BOLD)
            
            self.screen.addstr(3, 4, "1 - Add new alternative", h[0])
            self.screen.addstr(4, 4, "2 - Back ('q')", h[1])
            
            q = self.screen.getch()
            
            if q == curses.KEY_UP:
                option = (option - 1) % len(h)
            elif q == curses.KEY_DOWN:
                option = (option + 1) % len(h)
            elif q == ord('\n'):
                selection = option
                
            if selection == 0 :
                self.readAlternativeView()
            elif q == ord('q') or selection == len(h) -1 :
                self.launchMenuView()
        
    def readAlternativeView(self):
        
        selection = -1
        option = 0
        
        while selection < 0:
            self.screen.clear()
            
            h = [0] * 2
            h[option] = curses.color_pair(1)
            
            if len(self.alternatives) == 0:
                self.screen.addstr(1, 4, "You have no alternatives yet...", curses.A_BOLD)
            else:
                self.screen.addstr(1, 4, "Alternatives: {}".format(", ".join(self.alternatives)), curses.A_BOLD)
            
            s = self.readFromUser(3, 4)
            self.alternatives.append(s)

            self.addAlternativesView()
            
    def selectFileToLoad(self):
        
        selection = -1
        option = 0
        
        file_list = Utils.getFilesInDir();
        
        while selection < 0:
            self.screen.clear()
            
            self.screen.addstr(1, 4, "Select file you wish to open: ", curses.A_BOLD)
            
            h = [0] * (len(file_list) + 1)
            h[option] = curses.color_pair(1)
            
            for index, value in enumerate(file_list):
                self.screen.addstr(3 + index, 4, "{} - {}".format(index + 1, value), h[index])
                    
            self.screen.addstr(3 + len(file_list) + 1, 4, "{} - Back ('q')".format(len(file_list) + 1), h[len(file_list)])
                
            q = self.screen.getch()
            
            if q == curses.KEY_UP:
                option = (option - 1) % len(h)
            elif q == curses.KEY_DOWN:
                option = (option + 1) % len(h)
            elif q == ord('\n'):
                selection = option
            
            if q == ord('q') or selection == len(h) -1 :
                self.launchMenuView()
            elif selection != -1:
                
                root, alternatives = Utils.loadModelFromFile(file_list[selection])
                
                if root != None and alternatives != None:
                    self.root = root
                    self.alternatives = alternatives
                    self.current_node = self.root
                
                self.launchMenuView()
            
    def treeNodeView(self, mode = "view"):
        
        selection = -1
        option = 0
            
        while selection < 0:
            self.screen.clear()
            
            marker = self.current_node
            
            if self.current_node.parent == None:
                self.screen.addstr(1, 4, "This is root of hierarchy tree", curses.A_BOLD)
            else:
                history = []
                
                while marker != None:
                    history.insert(0, (marker.name if marker.name != None else "Anonim feature"))
                    marker = marker.parent
                    
                self.screen.addstr(1, 4, "Current brunch: " + " > ".join(history), curses.A_BOLD)
            
            self.screen.addstr(3, 4, "Feature name: {}".format(self.current_node.name if self.current_node.name != None else ""))
            
            self.screen.addstr(4, 4, "Feature preferences: {}".format(self.current_node.preferencesToString()))
            
            if self.current_node.isLief():
                self.screen.addstr(5, 4, "Sub-features: {}".format(self.current_node.children))
            else:
                sub_names = []
                for sub_feature in self.current_node.children:
                    sub_names.append(sub_feature.name if sub_feature.name != None else "Anonim feature")
                self.screen.addstr(5, 4, "Sub-features: [{}]".format(", ".join(sub_names) if self.current_node.children != [] else ""))
            
            if mode == "view":
                
                h = [0] * 7
                h[option] = curses.color_pair(1)
                
                self.screen.addstr(7, 4, "1 - Edit feature name", h[0])
                self.screen.addstr(8, 4, "2 - Edit feature preferences", h[1])
                self.screen.addstr(9, 4, "3 - Add sub-features", h[2])
                
                if self.current_node.isLief():
                    self.screen.addstr(10, 4, "4 - Set as tree brunch", h[3])
                else:
                    self.screen.addstr(10, 4, "4 - Set as tree lief", h[3])
                
                self.screen.addstr(12, 4, "5 - Go to parent", h[4])
                self.screen.addstr(13, 4, "6 - Go to sub-feature", h[5])
                self.screen.addstr(15, 4, "7 - Back ('q')", h[6])
                
                q = self.screen.getch()
                
                if q == curses.KEY_UP:
                    option = (option - 1) % len(h)
                elif q == curses.KEY_DOWN:
                    option = (option + 1) % len(h)
                elif q == ord('\n'):
                    selection = option
                    
                if selection == 0 :
                    self.treeNodeView("edit_name")
                elif selection == 1 :
                    self.treeNodeView("edit_preferences")
                elif selection == 2 :
                    self.treeNodeView("add_sub_feature")
                elif selection == 3:
                    if self.current_node.isLief():
                        self.current_node.setAsBrunch()
                    else:
                        self.current_node.setAsLief(alternatives_size = len(self.alternatives))
                    self.treeNodeView()
                elif selection == 4:
                    if self.current_node.parent != None:
                        self.current_node = self.current_node.parent
                    self.treeNodeView()
                elif selection == 5 :
                    self.treeNodeView("sub_feature_view")
                elif q == ord('q') or selection == len(h) -1 :
                    self.launchMenuView()
                    
            elif mode == "edit_name":
                
                self.screen.addstr(7, 4, "Set current feature name to:")
                
                s = self.readFromUser(9, 4)
                
                self.current_node.name = s
                self.treeNodeView()
                
            elif mode == "add_sub_feature":
                
                self.screen.addstr(7, 4, "Insert name of new feature:")
                                
                name = self.readFromUser(9, 4)
                self.current_node.addChildWithName(name)
                self.treeNodeView()
                
            elif mode == "insert_file_name":
                
                self.screen.addstr(7, 4, "Insert file name:")
                                
                name = self.readFromUser(9, 4)
                self.current_node.addChildWithName(name)
                
                model = {"alternatives": self.alternatives, "gole": self.root}
                Utils.saveModelToFile(model, name + ".json")                
                self.treeNodeView()
                
            elif mode == "edit_preferences":
                
                self.screen.addstr(7, 4, "Insert preferences values in MATLAB notation:")
                self.screen.addstr(8, 4, "[If you don't want to change preferences values just press Enter]")
                                
                preferences = self.readFromUser(10, 4)
                if self.current_node.isLief():
                    self.current_node.updatePreferences(preferences, len(self.alternatives))
                else:
                    self.current_node.updatePreferences(preferences)
                self.treeNodeView()
                 
            elif mode == "sub_feature_view":
                
                h = [0] * (len(self.current_node.children) + 1)
                h[option] = curses.color_pair(1)
                
                for index, value in enumerate(self.current_node.children):
                    self.screen.addstr(7 + index, 4, "{} - {}".format(index + 1, value.name), h[index])
                    
                self.screen.addstr(7 + len(self.current_node.children) + 1, 4, "{} - Back ('q')".format(len(self.current_node.children) + 1), h[len(self.current_node.children)])
                
                q = self.screen.getch()
                
                if q == curses.KEY_UP:
                    option = (option - 1) % len(h)
                elif q == curses.KEY_DOWN:
                    option = (option + 1) % len(h)
                elif q == ord('\n'):
                    selection = option
                    
                if q == ord('q') or selection == len(h) -1 :
                    self.launchMenuView()
                elif selection != -1:
                    self.current_node = self.current_node.children[option]
                    self.treeNodeView()