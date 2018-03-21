import curses

def addAlternativesView(ruter):
        
    selection = -1
    option = 0
    
    while selection < 0:
        ruter.screen.clear()
        
        h = [0] * 2
        h[option] = curses.color_pair(1)
        
        if len(ruter.alternatives) == 0:
            ruter.screen.addstr(1, 4, "You have no alternatives yet...", curses.A_BOLD)
        else:
            ruter.screen.addstr(1, 4, "Alternatives: {}".format(", ".join(ruter.alternatives)), curses.A_BOLD)
        
        ruter.screen.addstr(3, 4, "1 - Add new alternative", h[0])
        ruter.screen.addstr(4, 4, "2 - Back ('q')", h[1])
        
        q = ruter.screen.getch()
        
        if q == curses.KEY_UP:
            option = (option - 1) % len(h)
        elif q == curses.KEY_DOWN:
            option = (option + 1) % len(h)
        elif q == ord('\n'):
            selection = option
            
        if selection == 0 :
            ruter.current_view = "read_alternative_view"
        elif q == ord('q') or selection == len(h) -1 :
            ruter.current_view = "lunch_menu_view"