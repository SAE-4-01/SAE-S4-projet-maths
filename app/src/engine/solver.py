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
        depart = grid.get_case_location_start()
        arrive = grid.get_case_location_end()
        print(f" depart est la case {depart[0], depart[1]}")
        print(f" arriver est la case {arrive[0], arrive[1] }")
        open_list.append(depart)  # Ajouter la case départ à la liste d'ouverture
        print("début du traitement")
        # Boucle de résolution
        while (not isinstance(grid.get_case(open_list[0][0],open_list[0][1]),Arrive)) or len(open_list) == 0:
            print(f" liste ouverte : |{open_list.__str__()} | Liste fermee : |{close_list.__str__()} |")
            # Trouver la case avec la plus faible distance à partir de la liste d'ouverture
            current_case = open_list[0]
            print(f" traitement de la case {current_case[0] , current_case[1]}")
            open_list.pop(0)


            # Ajouter les cases adjacentes à la liste d'ouverture
            for adjacent in grid.get_case_adjacentes(current_case[0], current_case[1]):
                if adjacent not in close_list and adjacent not in open_list:
                    print(f" ajout du sommet  {adjacent[0], adjacent[1]}")
                    open_list.append(adjacent)

            print(f" La case {current_case[0], current_case[1] } à été traité ")
            close_list.append(current_case)

        # Met à jour le contenu de la grille avec des cases étoile pour l'ensemble des points visités
        close_list.pop(0)
        for i in range (len(close_list)):
            grid.set_case(close_list[i][0], close_list[i][1], Etoile())
            print(f"La case {close_list[i][0], close_list[i][1]} à été marquée ")
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

