from math import sqrt

from app.src.engine.case import Depart,Arrive, Rond, Croix, Point, Etoile, Case
from app.src.engine.grille import Grille
import time
class Solver:

    """
    Classe exploitant l'algorithme A*
    avec 3 types de calcul de l'heuristique
    - Dijkstra
    - Ville ou quadrillage
    - Pythagore
    """

    def solve_grid(grid: Grille, method: str) -> tuple[Grille,int,int,int,bool]:
        """
        Résout la grille en suivant l'algorithme spécifié (Dijkstra, ville ou pythagore).
        Place des objets Point() sur le chemin le plus court trouvé.

        :param grid: La grille à résoudre
        :param method: La méthode à utiliser ('dijkstra', 'ville', 'pythagore')
        :return: La grille résolue, le nombre de case visité, le temps d'éxécution et la longueur du chemin
        """
        # Initialisation des listes d'ouverture et de fermeture
        open_list = []  # Liste des cases à explorer
        close_list = []  # Liste des cases déjà explorées
        parents = {}  # Dictionnaire des prédécesseurs

        # Définir la case départ et la case arrivée sous forme de tuple
        depart = grid.get_case_location_start()
        arrive = grid.get_case_location_end()

        # Initialiser la liste ouverte en fonction de la méthode
        if method == 'dijkstra':
            open_list.append((depart[0], depart[1], 0))  # (x, y, g)
        elif method == 'ville':
            open_list.append((depart[0], depart[1], 0, Solver.get_heuristic_ville(depart, arrive)))  # (x, y, g, h)
        elif method == 'pythagore':
            open_list.append((depart[0], depart[1], 0, Solver.get_heuristic_pythagore(depart, arrive)))  # (x, y, g, h)
        else:
            raise ValueError("Méthode inconnue: choisissez parmi 'dijkstra', 'ville' ou 'pythagore'.")

        existance_chemin = False
        start_time = time.time()
        # Boucle de résolution
        while open_list:
            #Traitement de la case en début de liste
            current_case = open_list.pop(0)

            # Ajouter la case actuelle à la liste fermée
            close_list.append((current_case[0], current_case[1]))

            # Vérifier si on est arrivé
            if (current_case[0], current_case[1]) == arrive:
                existance_chemin = True
                break

            # Ajouter les cases adjacentes à la liste d'ouverture
            for adjacent in grid.get_case_adjacentes(current_case[0], current_case[1]):
                if adjacent not in close_list:
                    g = current_case[2] + 1

                    if method == 'dijkstra':
                        h = 0  # Pas d'heuristique pour Dijkstra
                    elif method == 'ville':
                        h = Solver.get_heuristic_ville(adjacent, arrive)
                    elif method == 'pythagore':
                        h = Solver.get_heuristic_pythagore(adjacent, arrive)
                        print(f"{Solver.get_heuristic_pythagore(adjacent, arrive)} vs {Solver.get_heuristic_ville(adjacent, arrive)}")

                    index_case_in_list = Solver.case_in_list(adjacent, open_list)

                    if index_case_in_list == -1:  # Si la case n'est pas dans la liste ouverte
                        parents[adjacent] = (current_case[0], current_case[1])  # Stocker le parent
                        if method == 'dijkstra':
                            open_list.append((adjacent[0], adjacent[1], g))
                        else:
                            open_list = Solver.place_case_in_list((adjacent[0], adjacent[1], g, h), open_list,
                                                                  index_case_in_list)
                    else:
                        # Mettre à jour le parent si un chemin plus court est trouvé
                        existing_case = open_list[index_case_in_list]
                        if g < existing_case[2]:
                            parents[adjacent] = (current_case[0], current_case[1])  # Mise à jour du parent
                            if method == 'dijkstra':
                                open_list[index_case_in_list] = (adjacent[0], adjacent[1], g)
                            else:
                                open_list[index_case_in_list] = (adjacent[0], adjacent[1], g, h)

        if existance_chemin:
            end_time = time.time()
            elapsed_time = end_time - start_time
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
                current = parents.get(current, depart)
            path.reverse()

            # Marquer le chemin optimal avec des points
            path.pop(-1)
            for case in path:
                grid.set_case(case[0], case[1], Point())

            print("Un chemin a été trouvé")
            print(grid.__str__())

<<<<<<< HEAD
    def solve_grid_pythagore(grid : Grille) -> Grille :
        """
        Résout la grille en suivant l'algorithme Pythagore.
        Place des objets Point() sur le chemin le plus court trouvé.
        :return: la grille résolue
        """
        # Initialisation des listes d'ouverture et de fermeture
        open_list: list[tuple[int, int, int, int]] = []  # Liste des cases à explorer
        close_list: list[tuple[int, int]] = []  # Liste des cases déjà explorées
        parents: dict[tuple[int, int], tuple[int, int]] = {}  # Dictionnaire des parents

        # Définir la case départ et la case arrivée sous forme de tuple
        depart = grid.get_case_location_start()
        arrive = grid.get_case_location_end()
        print(f"Départ : {depart}, Arrivée : {arrive}")

        # Corriger la création de tuple
        open_list.append((depart[0], depart[1], 0, Solver.get_heuristic_pythagore(depart, arrive)))

        existance_chemin = False
        # Boucle de résolution
        while open_list:
            print(f"Open liste actuelle {open_list}")
            print(f"Close liste actuelle {close_list}")

            # Trouver la case avec la plus faible f = g + h
            #open_list.sort(key=lambda x: x[2] + x[3])  # Trier par coût total (g + h)
            current_case = open_list.pop(0)

            # Ajouter la case actuelle à la liste fermée
            close_list.append((current_case[0], current_case[1]))

            # Vérifier si on est arrivé
            if (current_case[0], current_case[1]) == arrive:
                existance_chemin = True
                break

            # Ajouter les cases adjacentes à la liste d'ouverture
            for adjacent in grid.get_case_adjacentes(current_case[0], current_case[1]):
                if adjacent not in close_list:
                    g = current_case[2] + 1
                    h = Solver.get_heuristic_pythagore(adjacent, arrive)
                    index_case_in_list = Solver.case_in_list(adjacent, open_list)

                    if index_case_in_list == -1:  # Si la case n'est pas dans la liste ouverte
                        parents[adjacent] = (current_case[0], current_case[1])  # Stocker le parent
                        open_list = Solver.place_case_in_list((adjacent[0], adjacent[1], g, h), open_list,
                                                              index_case_in_list)
                    else:
                        # Mettre à jour le parent si un chemin plus court est trouvé
                        existing_case = open_list[index_case_in_list]
                        if g < existing_case[2]:
                            parents[adjacent] = (current_case[0], current_case[1])  # Mise à jour du parent
                            open_list[index_case_in_list] = (adjacent[0], adjacent[1], g, h)  # Mise à jour des coûts

        if existance_chemin:
            close_list.pop(0)
            close_list.pop(-1)
            # Marquer les cases visitées avec des étoiles
            for case in close_list:
                grid.set_case(case[0], case[1], Etoile())
            # Retracer le chemin optimal en utilisant le dictionnaire des parents
            chemin = []
            current = parents[arrive]
            while current != depart:
                chemin.append(current)
                current = parents[current]
            chemin.reverse()
            # Placer des objets Point() sur le chemin
            for case in chemin:
                grid.set_case(case[0], case[1], Point())

            print("Un chemin a été trouvé")
            print(grid.__str__())
            return grid
        else:
            print("Aucun chemin n'a pu être trouvé")
            return grid
=======
            return grid,elapsed_time,len(close_list),len(path)
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Aucun chemin n'a pu être trouvé")
            return grid,elapsed_time,len(close_list),0

>>>>>>> 7dfbafa (Code terminer si on fais les graphique à la main)

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

    def case_in_list(case: tuple[int, int], liste_ouverte: list[tuple[int, int, int, float]]) -> int:
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

    def place_case_in_list(case : tuple[int, int, int, int], liste_ouverte : list[tuple[int, int, int, float]], remove_case_index : int) -> list(tuple[int, int, int, int]) :
        """
        :param case : case à placer dans la liste
        :param liste_ouverte : liste ouverte dans laquelle il faut placer la nouvelle case
        :param remove_case_index : index de la case à retirer dans la liste ouverte si elle est présente
        :return la liste ouverte mise à jour
        """
        if not liste_ouverte :
            liste_ouverte = []
            liste_ouverte.append(case)
            return liste_ouverte
        f_cible = case[2] + case [3]
        if remove_case_index != -1:
            # Si la nouvelle case déja présente, mais est moins intéressante que l'ancienne
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

