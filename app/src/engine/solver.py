from math import sqrt

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

    def solve_grid_dijkstra(grid: Grille) -> Grille:
        """
        Résout la grille en suivant l'algorithme Dijkstra
        :return: la grille résolue
        """
        # Initialisation des listes d'ouverture et de fermeture
        open_list: list[tuple[int, int]] = []  # Liste des cases à explorer
        close_list: list[tuple[int, int]] = []  # Liste des cases déjà explorées
        predecessors: dict[tuple[int, int], tuple[int, int]] = {}  # Préserve le chemin

        # Définir la case départ et la case arrivée sous forme de tuple
        depart = grid.get_case_location_start()
        arrive = grid.get_case_location_end()
        print(f"Départ : {depart}, Arrivée : {arrive}")
        open_list.append(depart)  # Ajouter la case départ à la liste d'ouverture

        existance_chemin = False
        # Boucle de résolution
        while open_list:
            # Trouver la case avec la plus faible distance
            current_case = open_list.pop(0)

            # Ajouter la case actuelle à la liste fermée
            close_list.append(current_case)

            # Vérifier si on est arrivé
            if current_case == arrive:
                existance_chemin = True
                break

            # Ajouter les cases adjacentes à la liste d'ouverture
            for adjacent in grid.get_case_adjacentes(current_case[0], current_case[1]):
                if adjacent not in close_list and adjacent not in open_list:
                    open_list.append(adjacent)
                    predecessors[adjacent] = current_case  # Enregistrer le prédécesseur
        if existance_chemin:

            close_list.pop(0)
            close_list.pop(-1)
            # Marquer les cases visitées avec des étoiles
            for case in close_list:
                grid.set_case(case[0], case[1], Etoile())

            # Retracer le chemin optimal en suivant les prédécesseurs
            path = []
            current = arrive
            while current != depart:
                path.append(current)
                current = predecessors.get(current, depart)  # Remonter au prédécesseur
            path.reverse()  # Le chemin est construit à l'envers

            # Marquer le chemin optimal avec des points
            path.pop(-1)
            for case in path:
                grid.set_case(case[0], case[1], Point())  # Utiliser une classe Point pour marquer
            print("Un chemin à été trouvé")
            print(grid.__str__())
            return grid
        else :
            print("Aucun chemin n'a pu être trouvé")
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

