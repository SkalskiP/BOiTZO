# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                Main
# FILE VERSION:             1.0
# DATE:                     17.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# Main file used to run Easy AHP Tool in terminal
# ======================================================================================================================

from src.view_routing import ViewRutting


if __name__ == '__main__':
    view_routing = ViewRutting()
    view_routing.run_app()
