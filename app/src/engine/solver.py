from math import sqrt
from typing import List, Tuple

from app.src.engine.case import Depart,Arrive, Rond, Croix, Point, Etoile, Case
from app.src.engine.grille import Grille
class Solver:

    """
    Classe exploitant l'algorithme A*
    avec 3 types de calcul de l'heristique
    - Dijkstra
    - Ville ou quadrillage
    - Pythagore
    """

    from typing import List, Tuple

    def solve_grid_dijkstra(grid: Grille) -> Grille:
        """
        Résout la grille en suivant l'algorithme A* avec une heuristique nulle
        :return: la grille résolue
        """
        # Initialisation des listes d'ouverture et de fermeture
        open_list: List[Tuple[int, int]] = []  # Liste des cases à explorer
        close_list: List[Tuple[int, int]] = []  # Liste des cases déjà explorées

        # Définir la case départ et la case arrivée sous forme de tuple
        depart = grid.get_case_location(Depart)
        arrive = grid.get_case_location(Arrive)

        open_list.append(depart)  # Ajouter la case départ à la liste d'ouverture

        # Boucle de résolution
        while arrive not in open_list:
            # Trouver la case avec la plus faible distance à partir de la liste d'ouverture
            current_case = open_list[0]
            open_list.remove(current_case)
            close_list.append(current_case)

            # Ajouter les cases adjacentes à la liste d'ouverture
            for adjacent in grid.get_case_adjacentes(current_case[0], current_case[1]):
                if adjacent not in close_list and adjacent not in open_list:
                    open_list.append(adjacent)

        # Met à jour le contenu de la grille avec des cases points
        for col, lig in close_list:
            grid.set_case(col, lig, Etoile())

        return grid

    def solve_grid_ville(grid : Grille) -> Grille :
        """
        """
        return Grille()
    def solve_grid_pythagore(grid : Grille) -> Grille :
        """
        """
        return Grille()

    def get_heuristic_ville(case : tuple[int,int], case_arriver : tuple[int,int]) -> int:
        """
        :return: la distance de Manhattan entre la case évaluée et la case arrivée
        """
        distance_l = abs(case[0] - case_arriver[0])
        distance_h = abs(case[1] - case_arriver[1])
        return distance_l + distance_h

    def get_heuristic_pythagore(case : tuple[int,int], case_arriver : tuple[int,int]) -> float:
        """
        :return: la distance euclidienne entre la case évaluée et la case arrivée
        """
        distance_l = abs(case[0] - case_arriver[0])
        distance_h = abs(case[1] - case_arriver[1])
        return sqrt(distance_l**2+distance_h**2)

