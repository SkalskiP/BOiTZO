import curses
import json
from src.node import Node

def parse(obj):
    if type(obj) == Node:
        return { key: obj.__dict__[key] for key in ["name", "preferences", "children"]}
    else:
        return obj.__dict__
    
alternatives = []
root = Node()
current_node = root
    
def init_screen():
    # Initialize a new Windowobject which reprents the whole screen
    screen = curses.initscr()
    # Turn off the echo mode
    curses.noecho()             
    # Leave cursor invisible
    curses.curs_set(0)          
    curses.start_color()
    # Initialize a color-pair with RED as fg and WHITE as bg
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    screen.keypad(1)
    return screen

def close_screen(screen):
    screen.clear()
    curses.endwin()
    
def my_raw_input(window, r, c, prompt_string):
    curses.echo()
    window.addstr(r, c, prompt_string)
    window.refresh()
    input = window.getstr(r + 1, c)
    return input
    
def launch_menu_view():
    screen = init_screen()
    
    selection = -1
    option = 0

    while selection < 0:
        screen.clear()
        
        h = [0] * 4
        h[option] = curses.color_pair(1)

        screen.addstr(1, 4, "Please select an option...", curses.A_BOLD)
        screen.addstr(3, 4, "1 - Add alternatives", h[0])
        screen.addstr(4, 4, "2 - Build hierarchy of features", h[1])
        screen.addstr(5, 4, "3 - Get data", h[2])
        screen.addstr(6, 4, "4 - Exit ('q')", h[3])
        screen.refresh()
        
        q = screen.getch()
        
        if q == curses.KEY_UP:
            option = (option - 1) % len(h)
        elif q == curses.KEY_DOWN:
            option = (option + 1) % len(h)
        elif q == ord('\n'):
            selection = option
            
        if selection == 0 :
            close_screen(screen)
            add_alternatives_view()
        if selection == 1 :
            close_screen(screen)
            tree_node_view("view", True)
        if selection == 2 :
            data = {"alternatives": alternatives, "gole": root}
            
            with open('data.json', 'w') as outfile:
                # root_data = json.dumps(root, default=lambda o: { key: o.__dict__[key] for key in ["name", "preferences", "children", "alternatives", "gole"] }, indent = 4)
                data = {"alternatives": alternatives, "gole": root}
                json.dump(data, outfile, default=lambda o: parse(o), indent = 4)
            
            close_screen(screen)
            exit()
            
        elif q == ord('q') or selection == len(h) -1 :
            close_screen(screen)
            exit()
    
def add_alternatives_view():
    screen = init_screen()
    
    selection = -1
    option = 0
    
    while selection < 0:
        screen.clear()
        
        h = [0] * 2
        h[option] = curses.color_pair(1)
        
        if len(alternatives) == 0:
            screen.addstr(1, 4, "You have no alternatives yet...", curses.A_BOLD)
        else:
            screen.addstr(1, 4, "Alternatives: {}".format(", ".join(alternatives)), curses.A_BOLD)
        
        screen.addstr(3, 4, "1 - Add new alternative", h[0])
        screen.addstr(4, 4, "2 - Back ('q')", h[1])
        screen.refresh()
        
        q = screen.getch()
        
        if q == curses.KEY_UP:
            option = (option - 1) % len(h)
        elif q == curses.KEY_DOWN:
            option = (option + 1) % len(h)
        elif q == ord('\n'):
            selection = option
            
        if selection == 0 :
            close_screen(screen)
            read_alternative_view()
        elif q == ord('q') or selection == len(h) -1 :
            close_screen(screen)
            launch_menu_view()
    
def read_alternative_view():
    screen = init_screen()
    
    selection = -1
    option = 0
    
    while selection < 0:
        screen.clear()
        
        h = [0] * 2
        h[option] = curses.color_pair(1)
        
        if len(alternatives) == 0:
            screen.addstr(1, 4, "You have no alternatives yet...", curses.A_BOLD)
        else:
            screen.addstr(1, 4, "Alternatives: {}".format(", ".join(alternatives)), curses.A_BOLD)
        
        curses.echo()
        curses.curs_set(1)  
        
        s = screen.getstr(3, 4, 15).decode(encoding="utf-8")
        alternatives.append(s)
        close_screen(screen)
        add_alternatives_view()
        
def tree_node_view(mode = "view", start = False):
    screen = init_screen()
    
    selection = -1
    option = 0
    
    #if(start):
    #    current_node = root
    
    while selection < 0:
        screen.clear()
        
        marker = current_node
        
        if current_node.parent == None:
            screen.addstr(1, 4, "This is root of hierarchy tree", curses.A_BOLD)
        else:
            history = []
            
            while marker != None:
                history.insert(0, (marker.name if marker.name != None else "Anonim feature"))
                marker = marker.parent
                
            screen.addstr(1, 4, " > ".join(history), curses.A_BOLD)
        
        screen.addstr(3, 4, "Feature name: {}".format(current_node.name if current_node.name != None else ""))
        screen.addstr(4, 4, "Feature preferences: [{}]".format(", ".join(current_node.preferences) if current_node.preferences != [] else ""))
        
        sub_names = []
        for sub_feature in current_node.children:
            sub_names.append(sub_feature.name if sub_feature.name != None else "Anonim feature")
        
        screen.addstr(5, 4, "Sub-features: [{}]".format(", ".join(sub_names) if current_node.children != [] else ""))

        if mode == "view":
            
            h = [0] * 6
            h[option] = curses.color_pair(1)
            
            screen.addstr(7, 4, "1 - Edit feature name", h[0])
            screen.addstr(8, 4, "2 - Edit feature preferences", h[1])
            screen.addstr(9, 4, "3 - Add sub-features", h[2])
            
            screen.addstr(11, 4, "4 - Go to parent", h[3])
            
            screen.addstr(12, 4, "5 - Go to sub-feature", h[4])
            
            screen.addstr(14, 4, "6 - Back ('q')", h[5])
            
            screen.refresh()
        
            q = screen.getch()
            
            if q == curses.KEY_UP:
                option = (option - 1) % len(h)
            elif q == curses.KEY_DOWN:
                option = (option + 1) % len(h)
            elif q == ord('\n'):
                selection = option
                
            if selection == 0 :
                close_screen(screen)
                tree_node_view("edit_name")
            elif selection == 2 :
                close_screen(screen)
                tree_node_view("add_sub_feature")
            elif selection == 3:
                global current_node
                current_node = current_node.parent
                close_screen(screen)
                tree_node_view()
            elif selection == 4 :
                close_screen(screen)
                tree_node_view("sub_feature_view")
            elif q == ord('q') or selection == len(h) -1 :
                close_screen(screen)
                launch_menu_view()
                
        elif mode == "edit_name":
            
            screen.addstr(7, 4, "New feature name:")
            
            curses.echo()
            curses.curs_set(1)  
            
            s = screen.getstr(8, 4, 15).decode(encoding="utf-8")
            current_node.name = s
            close_screen(screen)
            tree_node_view()
            
        elif mode == "add_sub_feature":
            
            screen.addstr(7, 4, "Feature name:")
            
            curses.echo()
            curses.curs_set(1)  
            
            s = screen.getstr(8, 4, 15).decode(encoding="utf-8")
            
            tmp = Node()
            tmp.name = s
            tmp.parent = current_node
            current_node.children.append(tmp)
            close_screen(screen)
            tree_node_view()
            
        elif mode == "sub_feature_view":
            
            h = [0] * (len(current_node.children) + 1)
            h[option] = curses.color_pair(1)
            
            for index, value in enumerate(current_node.children):
                screen.addstr(7 + index, 4, "{} - {}".format(index + 1, value.name), h[index])
                
            screen.addstr(7 + len(current_node.children) + 1, 4, "{} - Back ('q')".format(len(current_node.children) + 1), h[len(current_node.children)])
            
            screen.refresh()
            q = screen.getch()
            
            if q == curses.KEY_UP:
                option = (option - 1) % len(h)
            elif q == curses.KEY_DOWN:
                option = (option + 1) % len(h)
            elif q == ord('\n'):
                selection = option
                global current_node
                current_node = current_node.children[option]
                close_screen(screen)
                tree_node_view()
                
            

            


    
    
if __name__ == '__main__':
    launch_menu_view()