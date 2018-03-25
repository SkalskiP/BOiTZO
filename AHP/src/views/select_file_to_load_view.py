from ..util.file_utils import FileUtils
import curses


def select_file_to_load(router):
    selection = -1
    option = 0

    file_list = FileUtils.get_files_in_dir()

    while selection < 0:
        router.screen.clear()

        router.screen.addstr(1, 4, "Select file you wish to open: ", curses.A_BOLD)

        h = [0] * (len(file_list) + 1)
        h[option] = curses.color_pair(1)

        for index, value in enumerate(file_list):
            router.screen.addstr(3 + index, 4, "{} - {}".format(index + 1, value), h[index])

        router.screen.addstr(3 + len(file_list) + 1, 4, "{} - Back ('q')".format(len(file_list) + 1), h[len(file_list)])

        q = router.screen.getch()

        if q == curses.KEY_UP:
            option = (option - 1) % len(h)
        elif q == curses.KEY_DOWN:
            option = (option + 1) % len(h)
        elif q == ord('\n'):
            selection = option

        if q == ord('q') or selection == len(h) - 1:
            router.current_view = "lunch_menu_view"
        elif selection != -1:

            root, alternatives = FileUtils.load_model_from_file(file_list[selection])

            if root is not None and alternatives is not None:
                router.root = root
                router.alternatives = alternatives
                router.current_node = router.root

            router.current_view = "lunch_menu_view"
