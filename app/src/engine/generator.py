from app.src.engine.case import Depart, Arrive, Rond, Croix
from app.src.engine.grille import Grille
import random

class Generator:
    @staticmethod
    def string_to_grid(grid_string: str) -> Grille:
        """
        Convertit une chaîne représentant la grille en un objet Grille.

        :param grid_string: Une chaîne représentant la grille, avec des lignes séparées par des sauts de ligne.
        :return: Un objet Grille rempli avec les cases de la chaîne.
        """
        # Découpe la chaîne en lignes
        lines = grid_string.strip().split("\n")

        # Crée une nouvelle grille avec le nombre de lignes et de colonnes
        grid = Grille(len(lines), len(lines[0]))

        # Remplir la grille avec les cases correspondantes
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == "X":
                    grid.set_case(i, j, Croix())
                elif char == "O":
                    grid.set_case(i, j, Rond())
                elif char == "D":
                    grid.set_case(i, j, Depart())
                elif char == "A":
                    grid.set_case(i, j, Arrive())
                else:
                    print(f"Caractère invalide : {char} à la position ({i}, {j})")
                    return None

        return grid
    def generate_grid(nb_colonne: int,nb_ligne: int, taux: float, option: bool) -> Grille:
        """
        Génère une grille avec un certain taux de CROIX parmi les cases.
        :param grid: La grille utilisée pour la génération.
        :param taux: Taux d'apparition de cases CROIX dans la grille.
        :param option: Active la génération des cases de départ et d'arrivée prédéfinies.
        :return: La grille générée en respectant le taux et l'option.
        """
        grid = Grille(nb_ligne, nb_colonne)
        nb_case = nb_colonne * nb_ligne
        ensemble_case = []

        # Générer les cases aléatoires en respectant le taux
        for _ in range(nb_case):
            if random.random() <= taux:
                ensemble_case.append(Croix())
            else:
                ensemble_case.append(Rond())

        # Gérer les cases de départ et d'arrivée
        if option:
            ensemble_case[0] = Depart()
            ensemble_case[-1] = Arrive()
        else:
            # Choisir une case aléatoire pour le départ
            depart_index = random.randint(0, nb_case - 1)
            ensemble_case[depart_index] = Depart()

            # Choisir une case différente pour l'arrivée
            arrive_index = depart_index
            while arrive_index == depart_index:
                arrive_index = random.randint(0, nb_case - 1)
            ensemble_case[arrive_index] = Arrive()

        # Remplir la grille avec les cases générées
        index_lecture = 0
        for i in range(nb_colonne):
            for j in range(nb_ligne):
                grid.set_case(j, i, ensemble_case[index_lecture])
                index_lecture += 1

        return grid
