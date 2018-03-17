# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                Main
# FILE VERSION:             1.0
# DATE:                     17.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# Main file used to run Easy AHP Tool in terminal
# ======================================================================================================================

from src.view_rutting import ViewRutting

if __name__ == '__main__':
    view_rutting = ViewRutting()
    view_rutting.introView("./data/intro.txt")
    view_rutting.launchMenuView()