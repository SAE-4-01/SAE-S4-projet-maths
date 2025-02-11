from math import sqrt

from app.src.engine.case import Depart,Arrive, Rond, Croix, Point, Etoile, Case
from app.src.engine.grille import Grille
class Solver:

    """
    Classe exploitant l'algorithme A*
    avec 3 types de calcul de l'heuristique
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

    def solve_grid_ville(grid: Grille) -> Grille:
        """
        Résout la grille en suivant l'algorithme Dijkstra
        :return: la grille résolue
        """
        # Initialisation des listes d'ouverture et de fermeture
        open_list: list[tuple[int, int, int, int]] = []  # Liste des cases à explorer
        close_list: list[tuple[int, int]] = []  # Liste des cases déjà explorées
        predecessors: dict[tuple[int, int], tuple[int, int]] = {}  # Préserve le chemin

        # Définir la case départ et la case arrivée sous forme de tuple
        depart = grid.get_case_location_start()
        arrive = grid.get_case_location_end()
        print(f"Départ : {depart}, Arrivée : {arrive}")

        # Corriger la création de tuple
        open_list.append((depart[0], depart[1], 0, Solver.get_heuristic_ville(depart, arrive)))

        existance_chemin = False
        # Boucle de résolution
        while open_list:
            print(f"Open liste actuelle{open_list}")
            print(f"Open close actuelle{close_list}")
            # Trouver la case avec la plus faible distance
            current_case = open_list.pop(0)

            # Ajouter la case actuelle à la liste fermée
            close_list.append((current_case[0], current_case[1]))

            # Vérifier si on est arrivé
            if (current_case[0],current_case[1]) == arrive:
                existance_chemin = True
                break
            # Ajouter les cases adjacentes à la liste d'ouverture
            for adjacent in grid.get_case_adjacentes(current_case[0], current_case[1]):
                # Le point n'est pas traité
                if adjacent not in close_list :
                    g = current_case[2] + 1
                    h = Solver.get_heuristic_ville(adjacent,arrive)
                    index_case_in_list = Solver.case_in_list(adjacent,open_list)
                    open_list = Solver.place_case_in_list((adjacent[0], adjacent[1], g, h), open_list,
                                                          index_case_in_list)
                    predecessors[adjacent] = (current_case[0], current_case[1]) # Enregistrer le prédécesseur

        if existance_chemin :
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
        else:
            print("Aucun chemin n'a pu être trouvé")
            return grid

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

    def case_in_list(case: tuple[int, int], liste_ouverte: list[tuple[int, int, int, int]]) -> int:
        """
        :param case: case à vérifier si elle est dans la liste ouverte
        :param liste_ouverte: liste ouverte dans laquelle il faut vérifier la présence de la case
        :return: l'index de la case dans la liste ouverte, -1 si elle n'est pas présente ou si la liste est vide
        """
        if not liste_ouverte:  # Vérifie si la liste est None ou vide
            return -1

        for i, c in enumerate(liste_ouverte):
            case_observe = (c[0], c[1])
            if case_observe == case:
                return i
        return -1

    def place_case_in_list(case : tuple[int, int, int, int], liste_ouverte : list(tuple[int, int, int, int]), remove_case_index : int) -> list(tuple[int, int, int, int]) :
        """
        :param case : case à placer dans la liste
        :param liste_ouverte : liste ouverte dans laquelle il faut placer la nouvelle case
        :param remove_case_index : index de la case à retirer dans la liste ouverte si elle est présente
        :return la liste ouverte mise à jour
        """
        print(f"ajout de la case {case}")
        if not liste_ouverte :
            liste_ouverte = []
            liste_ouverte.append(case)
            return liste_ouverte
        f_cible = case[2] + case [3]
        if remove_case_index != -1:
            # Si la nouvelle case déja présente est moins intéressante que l'ancienne
            if f_cible >= liste_ouverte[remove_case_index][2] + liste_ouverte[remove_case_index][3] :
                # La liste telle qu'elle est renvoyée
                return liste_ouverte
            # Sinon la case moins performante est retirée
            liste_ouverte.pop(remove_case_index)
        # Place la nouvelle case dans l'open list en fonction de son f
        i = 0
        while i < len(liste_ouverte):
            f_actuelle = liste_ouverte[i][2] + liste_ouverte[i][3]
            if f_cible < f_actuelle:
                # Insérer avant la case avec une priorité plus élevée
                liste_ouverte.insert(i, case)
                return liste_ouverte
            elif f_cible == f_actuelle:
                # Insérer juste après ou au même endroit selon la politique
                liste_ouverte.insert(i + 1, case)
                return liste_ouverte
            i += 1
        # Si aucune insertion ne s'est faite, ajouter à la fin
        liste_ouverte.append(case)
        return liste_ouverte

