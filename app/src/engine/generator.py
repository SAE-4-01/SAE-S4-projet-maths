from app.src.engine.case import Depart, Arrive, Rond, Croix
from app.src.engine.grille import Grille
import random

class Generator:
    def generate_grid(grid: Grille, taux: float, option: bool) -> Grille:
        """
        Génère une grille avec un certain taux de CROIX parmi les cases.
        :param grid: La grille utilisée pour la génération.
        :param taux: Taux d'apparition de cases CROIX dans la grille.
        :param option: Active la génération des cases de départ et d'arrivée prédéfinies.
        :return: La grille générée en respectant le taux et l'option.
        """
        nb_case = grid.get_nb_case()
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
        for i in range(grid.nb_ligne):
            for j in range(grid.nb_colonne):
                grid.set_case(i, j, ensemble_case[index_lecture])
                index_lecture += 1

        return grid
