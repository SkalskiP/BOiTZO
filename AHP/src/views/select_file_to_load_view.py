from ..utils import Utils
import curses

def selectFileToLoad(ruter):
    
    selection = -1
    option = 0
    
    file_list = Utils.getFilesInDir();
    
    while selection < 0:
        ruter.screen.clear()
        
        ruter.screen.addstr(1, 4, "Select file you wish to open: ", curses.A_BOLD)
        
        h = [0] * (len(file_list) + 1)
        h[option] = curses.color_pair(1)
        
        for index, value in enumerate(file_list):
            ruter.screen.addstr(3 + index, 4, "{} - {}".format(index + 1, value), h[index])
                
        ruter.screen.addstr(3 + len(file_list) + 1, 4, "{} - Back ('q')".format(len(file_list) + 1), h[len(file_list)])
            
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
            
            root, alternatives = Utils.loadModelFromFile(file_list[selection])
            
            if root != None and alternatives != None:
                ruter.root = root
                ruter.alternatives = alternatives
                ruter.current_node = ruter.root
            
            ruter.current_view = "lunch_menu_view"