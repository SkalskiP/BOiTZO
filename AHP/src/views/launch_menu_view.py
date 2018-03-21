import curses

def launchMenuView(ruter):

    selection = -1
    option = 0

    while selection < 0:
        ruter.screen.clear()
        
        h = [0] * 5
        h[option] = curses.color_pair(1)

        ruter.screen.addstr(1, 4, "Please select an option...", curses.A_BOLD)
        ruter.screen.addstr(3, 4, "1 - Add alternatives", h[0])
        ruter.screen.addstr(4, 4, "2 - Build hierarchy of features", h[1])
        ruter.screen.addstr(5, 4, "3 - Save as JSON file", h[2])
        ruter.screen.addstr(6, 4, "4 - Load from JSON file", h[3])
        ruter.screen.addstr(8, 4, "5 - Exit ('q')", h[4])
        
        q = ruter.screen.getch()
        
        if q == curses.KEY_UP:
            option = (option - 1) % len(h)
        elif q == curses.KEY_DOWN:
            option = (option + 1) % len(h)
        elif q == ord('\n'):
            selection = option
            
        if selection == 0 :
            ruter.current_view = "add_alternatives_view"
        elif selection == 1 :
            ruter.current_view = "tree_node_view"
        elif selection == 2 :
            ruter.current_view = "insert_file_name"
        elif selection == 3 :
            ruter.current_view = "select_file_to_load"
        elif q == ord('q') or selection == len(h) -1 :
            ruter.running = False