from ..utils import Utils
import curses

def treeNodeView(ruter):
        
    selection = -1
    option = 0
        
    while selection < 0:
        ruter.screen.clear()
        
        marker = ruter.current_node
        
        if ruter.current_node.parent == None:
            ruter.screen.addstr(1, 4, "This is root of hierarchy tree", curses.A_BOLD)
        else:
            history = []
            
            while marker != None:
                history.insert(0, (marker.name if marker.name != None else "Anonim feature"))
                marker = marker.parent
                
            ruter.screen.addstr(1, 4, "Current brunch: " + " > ".join(history), curses.A_BOLD)
        
        ruter.screen.addstr(3, 4, "Feature name: {}".format(ruter.current_node.name if ruter.current_node.name != None else ""))
        
        ruter.screen.addstr(4, 4, "Feature preferences: {}".format(ruter.current_node.preferencesToString()))
        
        if ruter.current_node.isLief():
            ruter.screen.addstr(5, 4, "Sub-features: {}".format(ruter.current_node.children))
        else:
            sub_names = []
            for sub_feature in ruter.current_node.children:
                sub_names.append(sub_feature.name if sub_feature.name != None else "Anonim feature")
            ruter.screen.addstr(5, 4, "Sub-features: [{}]".format(", ".join(sub_names) if ruter.current_node.children != [] else ""))
        
        if ruter.current_view == "tree_node_view":
            
            h = [0] * 7
            h[option] = curses.color_pair(1)
            
            ruter.screen.addstr(7, 4, "1 - Edit feature name", h[0])
            ruter.screen.addstr(8, 4, "2 - Edit feature preferences", h[1])
            ruter.screen.addstr(9, 4, "3 - Add sub-features", h[2])
            
            if ruter.current_node.isLief():
                ruter.screen.addstr(10, 4, "4 - Set as tree brunch", h[3])
            else:
                ruter.screen.addstr(10, 4, "4 - Set as tree lief", h[3])
            
            ruter.screen.addstr(12, 4, "5 - Go to parent", h[4])
            ruter.screen.addstr(13, 4, "6 - Go to sub-feature", h[5])
            ruter.screen.addstr(15, 4, "7 - Back ('q')", h[6])
            
            q = ruter.screen.getch()
            
            if q == curses.KEY_UP:
                option = (option - 1) % len(h)
            elif q == curses.KEY_DOWN:
                option = (option + 1) % len(h)
            elif q == ord('\n'):
                selection = option
                
            if selection == 0 :
                ruter.current_view = "edit_name"
            elif selection == 1 :
                ruter.current_view = "edit_preferences"
            elif selection == 2 :
                ruter.current_view = "add_sub_feature"
            elif selection == 3:
                if ruter.current_node.isLief():
                    ruter.current_node.setAsBrunch()
                else:
                    ruter.current_node.setAsLief(alternatives_size = len(ruter.alternatives))
                ruter.current_view = "tree_node_view"
            elif selection == 4:
                if ruter.current_node.parent != None:
                    ruter.current_node = ruter.current_node.parent
                ruter.current_view = "tree_node_view"
            elif selection == 5 :
                ruter.current_view = "sub_feature_view"
            elif q == ord('q') or selection == len(h) -1 :
                ruter.current_view = "lunch_menu_view"
                
        elif ruter.current_view == "edit_name":
            
            ruter.screen.addstr(7, 4, "Set current feature name to:")
            
            s = ruter.readTextFromUser(9, 4)
            
            ruter.current_node.name = s
            ruter.current_view = "tree_node_view"
            
        elif ruter.current_view == "add_sub_feature":
            
            ruter.screen.addstr(7, 4, "Insert name of new feature:")
                            
            name = ruter.readTextFromUser(9, 4)
            ruter.current_node.addChildWithName(name)
            ruter.current_view = "tree_node_view"
            
        elif ruter.current_view == "insert_file_name":
            
            ruter.screen.addstr(7, 4, "Insert file name:")
                            
            name = ruter.readTextFromUser(9, 4)
            
            model = {"alternatives": ruter.alternatives, "gole": ruter.root}
            Utils.saveModelToFile(model, name + ".json")                
            ruter.current_view = "tree_node_view"
            
        elif ruter.current_view == "edit_preferences":
            
            ruter.screen.addstr(7, 4, "Insert preferences values in MATLAB notation:")
            ruter.screen.addstr(8, 4, "[If you don't want to change preferences values just press Enter]")
                            
            preferences = ruter.readTextFromUser(10, 4)
            if ruter.current_node.isLief():
                ruter.current_node.updatePreferences(preferences, len(ruter.alternatives))
            else:
                ruter.current_node.updatePreferences(preferences)
            ruter.current_view = "tree_node_view"
             
        elif ruter.current_view == "sub_feature_view":
            
            h = [0] * (len(ruter.current_node.children) + 1)
            h[option] = curses.color_pair(1)
            
            for index, value in enumerate(ruter.current_node.children):
                ruter.screen.addstr(7 + index, 4, "{} - {}".format(index + 1, value.name), h[index])
                
            ruter.screen.addstr(7 + len(ruter.current_node.children) + 1, 4, "{} - Back ('q')".format(len(ruter.current_node.children) + 1), h[len(ruter.current_node.children)])
            
            q = ruter.screen.getch()
            
            if q == curses.KEY_UP:
                option = (option - 1) % len(h)
            elif q == curses.KEY_DOWN:
                option = (option + 1) % len(h)
            elif q == ord('\n'):
                selection = option
                
            if q == ord('q') or selection == len(h) -1 :
                ruter.current_view = "lunch_menu_view"
            elif selection != -1:
                ruter.current_node = ruter.current_node.children[option]
                ruter.current_view = "tree_node_view"