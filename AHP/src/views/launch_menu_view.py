# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                launch_menu_view
# FILE VERSION:             1.0
# DATE:                     25.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains function used to create main app view.
# ======================================================================================================================


import curses
from ..utils.views_names import ViewsNames


def launch_menu_view(router):
    selection = -1
    option = 0

    while selection < 0:
        router.screen.clear()

        h = [0] * 6
        h[option] = curses.color_pair(1)

        router.screen.addstr(1, 4, "Please select an option...", curses.A_BOLD)
        router.screen.addstr(3, 4, "1 - Add alternatives", h[0])
        router.screen.addstr(4, 4, "2 - Build hierarchy of features", h[1])
        router.screen.addstr(5, 4, "2 - View features hierarchy tree", h[2])
        router.screen.addstr(6, 4, "3 - Save as JSON file", h[3])
        router.screen.addstr(7, 4, "4 - Load from JSON file", h[4])
        router.screen.addstr(9, 4, "5 - Exit ('q')", h[5])

        q = router.screen.getch()

        if q == curses.KEY_UP:
            option = (option - 1) % len(h)
        elif q == curses.KEY_DOWN:
            option = (option + 1) % len(h)
        elif q == ord('\n'):
            selection = option

        if selection == 0:
            router.current_view = ViewsNames.ADD_ALTERNATIVES
        elif selection == 1:
            router.current_view = ViewsNames.TREE_NODE
        elif selection == 2:
            router.current_view = ViewsNames.SHOW_PROJECT_TREE
        elif selection == 3:
            router.current_view = ViewsNames.INSERT_FILE_NAME
        elif selection == 4:
            router.current_view = ViewsNames.SELECT_FILE_TO_LOAD
        elif q == ord('q') or selection == len(h) - 1:
            router.running = False
