import os
from datetime import datetime
from app.src.engine.grille import Grille


class Exporter :
    """
    Classe d'exportation de la grille sous forme de fichier txt
    """
    @staticmethod
    def export_grille(grid : Grille, folder_path="../ressources/sortie/"):
        """
        Exporte la grille dans un fichier texte à l'emplacement spécifié
        """
        try:
            file_path = folder_path + "grille_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + (".txt")


            contenu = grid.to_str()
            with open(file_path, "w") as fichier:
                fichier.write(contenu)
            print(f"Grille exportée avec succès dans '{file_path}'")
        except Exception as e:
            print(f"Erreur lors de l'exportation : {e}")
