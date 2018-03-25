import curses


def read_alternative_view(ruter):
        ruter.screen.clear()
        
        if len(ruter.alternatives) == 0:
            ruter.screen.addstr(1, 4, "You have no alternatives yet...", curses.A_BOLD)
        else:
            ruter.screen.addstr(1, 4, "Alternatives: {}".format(", ".join(ruter.alternatives)), curses.A_BOLD)
        
        s = ruter.read_text_from_user(3, 4)
        ruter.alternatives.append(s)

        ruter.current_view = "add_alternatives_view"
