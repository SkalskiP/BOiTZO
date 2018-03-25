# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                read_alternatives_view
# FILE VERSION:             1.0
# DATE:                     25.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains function used to create app view used to read name of alternative for AHP model.
# ======================================================================================================================


import curses
from ..utils.views_names import ViewsNames


def read_alternative_view(ruter):
        ruter.screen.clear()
        
        if len(ruter.alternatives) == 0:
            ruter.screen.addstr(1, 4, "You have no alternatives yet...", curses.A_BOLD)
        else:
            ruter.screen.addstr(1, 4, "Alternatives: {}".format(", ".join(ruter.alternatives)), curses.A_BOLD)
        
        s = ruter.read_text_from_user(3, 4)
        ruter.alternatives.append(s)

        ruter.current_view = ViewsNames.ADD_ALTERNATIVES
