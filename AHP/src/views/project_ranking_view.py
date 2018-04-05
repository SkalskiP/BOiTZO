# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                project_ranking_view
# FILE VERSION:             1.0
# DATE:                     05.04.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains function used to create app view used to view calculated rankings.
# ======================================================================================================================

import curses
from ..utils.views_names import ViewsNames
from ..utils.ranking_calculator_utils import RankingCalculator
from ..utils.table_utils import Table


def project_ranking_view(router):
    router.screen.clear()

    n_alternatives = len(router.alternatives)

    router.screen.addstr(1, 4, "Calculated rankings:", curses.A_BOLD)

    if router.root.validate_tree(n_alternatives):

        table = Table(router.screen, 3, 4)
        eig_ranking = RankingCalculator.get_eig_ranking(router.root).tolist()
        geom_ranking = RankingCalculator.get_geom_ranking(router.root).tolist()
        norm_cols_ranking = RankingCalculator.get_norm_cols_ranking(router.root).tolist()

        table.add_column("Alternatives", router.alternatives, 25)
        table.add_column("Eigenvector", eig_ranking, 25)
        table.add_column("Geometric mean", geom_ranking, 25)
        table.add_column("Normalized columns", norm_cols_ranking, 25)
        table.draw_table()

    else:
        router.screen.addstr(3, 4, "Sorry. Structure of your AHP tree contains serious errors.")
        router.screen.addstr(4, 4, "Correct these errors to perform calculations.")

    q = router.screen.getch()

    router.current_view = ViewsNames.LUNCH_MENU