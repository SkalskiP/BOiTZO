# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                ranking_calculator_utils
# FILE VERSION:             1.0
# DATE:                     05.04.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains set of static methods responsible for calculating AHP ranking values different ways
# ======================================================================================================================

import numpy as np
from scipy import linalg as la


class RankingCalculator:

    @staticmethod
    def get_eig_ranking(dictionary, verbose=False):
        preferences_array = np.array(dictionary.preferences)
        e_vals, e_vecs = la.eig(preferences_array)
        max_eigv_index = np.argmax(e_vals, axis=0)
        ranking = e_vecs[:, max_eigv_index].real
        ranking = ranking / ranking.sum()

        if verbose:
            print(dictionary.name)
            print("Ranking:")
            print(ranking)

        if dictionary.children == "alternatives":
            return ranking
        else:
            children_ranking = \
                np.array([RankingCalculator.get_eig_ranking(child, verbose) for child in dictionary.children])
            return ranking @ children_ranking

    @staticmethod
    def get_geom_ranking(dictionary, verbose=False):
        preferences_array = np.array(dictionary.preferences)
        ranking = np.power(np.prod(preferences_array, axis=1), 1 / preferences_array.shape[1])
        ranking = ranking / ranking.sum()

        if verbose:
            print(dictionary.name)
            print("Ranking:")
            print(ranking)

        if dictionary.children == "alternatives":
            return ranking
        else:
            children_ranking = \
                np.array([RankingCalculator.get_geom_ranking(child, verbose) for child in dictionary.children])
            return ranking @ children_ranking

    @staticmethod
    def get_norm_cols_ranking(dictionary, verbose=False):
        preferences_array = np.array(dictionary.preferences)
        ranking = np.mean(preferences_array / preferences_array.sum(axis=0)[None, :], axis=1)

        if verbose:
            print(dictionary.name)
            print("Ranking:")
            print(ranking)

        if dictionary.children == "alternatives":
            return ranking
        else:
            children_ranking = \
                np.array([RankingCalculator.get_norm_cols_ranking(child, verbose) for child in dictionary.children])
            return ranking @ children_ranking
