from app.src.engine.checker import Checker
from app.src.engine.generator import Generator
from app.src.engine.grille import Grille

class Importer :
    """
    Classe de gestion de l'importation du fichier txt
    """
    @staticmethod
    def load_grid_from_file(file_path: str) -> Grille | None:
        """
        Charge une grille depuis un fichier texte.

        :param file_path: Le chemin du fichier texte à importer.
        :return: La grille sous forme de chaîne de caractère à partir du fichier.
        """
        try:
            # Ouvrir et lire le fichier
            with open(file_path, 'r') as file:
                grid_string = file.read()
            # Verification de la validité de la grille
            grid_ok = Checker.grille_checker(grid_string)
            # Convertir la chaîne en grille
            if grid_ok:
                grid = Generator.string_to_grid(grid_string)
            else:
                grid = None
                print("Erreur de conversion de la chaîne en grille.")
            return grid

        except FileNotFoundError:
            print(f"Le fichier {file_path} n'a pas été trouvé.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")
        return None
