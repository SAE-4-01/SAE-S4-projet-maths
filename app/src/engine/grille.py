from app.src.engine.case import Depart, Arrive, Rond, Croix, Point, Etoile, Case


class Grille:
    """
    La classe Grille permet de gérer la grille composé de case
    """

    def __init__(self, nb_ligne: int, nb_colonne: int):
        """
        Constructeur de la classe Grille
        """
        if nb_ligne <= 2:
            raise ValueError("Le nombre de lignes doit être supérieur à 2")
        if nb_colonne <= 2:
            raise ValueError("Le nombre de colonnes doit être supérieur à 2")

        # grille à résoudre
        # la base de la grille commence à la ligne 0 et à la colonne 0
        self.nb_ligne = nb_ligne
        self.nb_colonne = nb_colonne
        self.grille: list[list[Depart | Arrive | Rond | Croix | Point | Etoile | None]] = \
            [[None for _ in range(nb_colonne)] for _ in range(nb_ligne)]

    def get_grille(self):
        """
        :return: la grille
        """
        return self.grille

    def get_case(self, ligne: int, colonne: int) -> Case :
        """
        Permet de récupérer une case de la grille
        :param ligne: l'indice de la ligne
        :param colonne: l'indice de la colonne
        :return: la case demandée
        """
        if ligne < 0 or ligne >= self.nb_ligne:
            raise IndexError("La ligne demandée est hors des limites de la grille")
        if colonne < 0 or colonne >= self.nb_colonne:
            raise IndexError("La colonne demandée est hors des limites de la grille")

        return self.grille[ligne][colonne]

    def set_case(self, ligne: int, colonne: int, case: Depart | Arrive | Rond | Croix | Point | Etoile):
        """
        Permet de changer l'état d'une case
        :param ligne: l'indice de la ligne
        :param colonne: l'indice de la colonne
        :param case: la case à remplacer
        """
        if ligne < 0 or ligne >= self.nb_ligne:
            raise IndexError("La ligne demandée est hors des limites de la grille")
        if colonne < 0 or colonne >= self.nb_colonne:
            raise IndexError("La colonne demandée est hors des limites de la grille")

        self.grille[ligne][colonne] = case

    def __str__(self):
        """
        Représentation en chaîne de caractères de la grille
        """
        affichage = ""

        # Affichage des indices des colonnes
        for i in range(self.nb_colonne):
            affichage += f"  {i} "

        affichage += "\n" + " ___" * self.nb_colonne + "\n"

        # Parcours des lignes de haut en bas
        for lig in range(self.nb_ligne):
            for col in range(self.nb_colonne):
                case = " "

                if self.get_case(lig, col) is not None:
                    case = self.get_case(lig, col).get_caractere()

                affichage += f"| {case} "

            affichage += "|\n" + ("|___" * self.nb_colonne) + "|\n"

        return affichage

    def get_nb_case(self):
        """
        :return: le nombre de cases dans la grille
        """
        return self.nb_ligne * self.nb_colonne

    def get_case_location_start(self) -> tuple[int, int]:
        # Parcours des lignes de haut en bas
        for lig in range(self.nb_ligne):
            for col in range(self.nb_colonne):
                if isinstance(self.get_case(lig, col), Depart) :
                    return lig, col
    def get_case_location_end(self) -> tuple[int, int]:
        # Parcours des lignes de haut en bas
        for lig in range(self.nb_ligne):
            for col in range(self.nb_colonne):
                if isinstance(self.get_case(lig, col), Arrive) :
                    return lig, col

    def get_case_adjacentes(self, lig: int, col: int) -> list[tuple[int, int]]:
        """
        :param lig: l'indice de la ligne
        :param col: l'indice de la colonne
        :return: une liste des cases adjacentes (non diagonaux) à la case demandée
        """
        cases_adjacentes = []

        # Cas limites
        # Privilégie les cases à droite et en dessous
        if col > 0:
            if not isinstance(self.get_case(lig, col - 1),Croix):
                cases_adjacentes.append((lig, col - 1))
        if lig < self.nb_ligne - 1 :
            if not isinstance(self.get_case(lig + 1, col),Croix):
                cases_adjacentes.append((lig + 1, col))
        if lig > 0:
            if not isinstance(self.get_case(lig - 1, col),Croix):
                cases_adjacentes.append((lig - 1, col))
        if col < self.nb_colonne - 1 :
            if not isinstance(self.get_case(lig, col + 1),Croix):
                cases_adjacentes.append((lig, col + 1))

        return cases_adjacentes