# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                add_alternatives_view
# FILE VERSION:             1.0
# DATE:                     25.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains function used to create app view used to add alternatives for AHP model.
# ======================================================================================================================


import curses
from ..utils.views_names import ViewsNames


def add_alternatives_view(router):
        
    selection = -1
    option = 0
    
    while selection < 0:
        router.screen.clear()
        
        h = [0] * 2
        h[option] = curses.color_pair(1)
        
        if len(router.alternatives) == 0:
            router.screen.addstr(1, 4, "You have no alternatives yet...", curses.A_BOLD)
        else:
            router.screen.addstr(1, 4, "Alternatives: {}".format(", ".join(router.alternatives)), curses.A_BOLD)
        
        router.screen.addstr(3, 4, "1 - Add new alternative", h[0])
        router.screen.addstr(4, 4, "2 - Back ('q')", h[1])
        
        q = router.screen.getch()
        
        if q == curses.KEY_UP:
            option = (option - 1) % len(h)
        elif q == curses.KEY_DOWN:
            option = (option + 1) % len(h)
        elif q == ord('\n'):
            selection = option
            
        if selection == 0:
            router.current_view = ViewsNames.READ_ALTERNATIVES
        elif q == ord('q') or selection == len(h) - 1:
            router.current_view = ViewsNames.LUNCH_MENU
