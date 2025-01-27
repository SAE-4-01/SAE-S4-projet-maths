class Checker:
    @staticmethod
    def grille_checker(grid_string: str) -> bool:
        """
        Vérifie si la grille est valide selon les contraintes spécifiées.

        :param grid_string: Une chaîne représentant la grille, avec des lignes séparées par des sauts de ligne.
        :return: True si la grille est valide, False sinon.
        """
        # Découper la grille en lignes
        lines = grid_string.strip().split("\n")

        # Vérifier que la grille est rectangulaire
        num_columns = len(lines[0])
        if any(len(line) != num_columns for line in lines):
            print("Erreur : La grille n'est pas rectangulaire.")
            return False

        # Vérifier que la grille est au moins 3x3
        num_rows = len(lines)
        if num_rows < 3 or num_columns < 3:
            print("Erreur : La grille doit être au moins de taille 3x3.")
            return False

        # Vérifier le contenu de la grille
        d_count = 0
        a_count = 0
        for line in lines:
            for char in line:
                if char == "D":
                    d_count += 1
                elif char == "A":
                    a_count += 1
                elif char not in {"X", "O"}:
                    print(f"Erreur : Caractère invalide détecté : {char}")
                    return False

        # Vérifier qu'il y a exactement un D et un A
        if d_count != 1:
            print(f"Erreur : Nombre de 'D' invalide : {d_count} (doit être 1).")
            return False
        if a_count != 1:
            print(f"Erreur : Nombre de 'A' invalide : {a_count} (doit être 1).")
            return False

        return True
