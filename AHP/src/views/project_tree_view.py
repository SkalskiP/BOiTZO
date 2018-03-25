# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                project_tree_view
# FILE VERSION:             1.0
# DATE:                     25.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains function used to create app view used to add alternatives for AHP model.
# ======================================================================================================================


import curses
import asciitree
from ..utils.file_utils import FileUtils
from ..utils.views_names import ViewsNames


def project_tree_view(router):
    router.screen.clear()

    router.screen.addstr(1, 4, "Features hierarchy tree:", curses.A_BOLD)

    data = FileUtils.get_brief_tree(router.root, router.alternatives)
    la = asciitree.LeftAligned()

    tree = la({router.root.name: data}).splitlines()

    for index, line in enumerate(tree):
        router.screen.addstr(index + 3, 4, line)

    q = router.screen.getch()

    router.current_view = ViewsNames.LUNCH_MENU
