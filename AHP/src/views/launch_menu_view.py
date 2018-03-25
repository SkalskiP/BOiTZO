import curses
from ..util.views_names import ViewsNames


def launch_menu_view(router):
    selection = -1
    option = 0

    while selection < 0:
        router.screen.clear()

        h = [0] * 5
        h[option] = curses.color_pair(1)

        router.screen.addstr(1, 4, "Please select an option...", curses.A_BOLD)
        router.screen.addstr(3, 4, "1 - Add alternatives", h[0])
        router.screen.addstr(4, 4, "2 - Build hierarchy of features", h[1])
        router.screen.addstr(5, 4, "3 - Save as JSON file", h[2])
        router.screen.addstr(6, 4, "4 - Load from JSON file", h[3])
        router.screen.addstr(8, 4, "5 - Exit ('q')", h[4])

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
            router.current_view = ViewsNames.INSERT_FILE_NAME
        elif selection == 3:
            router.current_view = ViewsNames.SELECT_FILE_TO_LOAD
        elif q == ord('q') or selection == len(h) - 1:
            router.running = False
