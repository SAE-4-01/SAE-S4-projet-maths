import os
from datetime import datetime
from app.src.engine.grille import Grille


class Exporter:
    """
    Classe d'exportation de la grille sous forme de fichier txt
    """
    @staticmethod
    def export_grille(grid: Grille, folder_path="../ressources/sortie/"):
        """
        Exporte la grille dans un fichier texte à l'emplacement spécifié
        """
        try:
            # Vérifier si le dossier existe et le créer si nécessaire
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)

            # Construire le chemin du fichier
            file_path = os.path.join(
                folder_path,
                f"grille_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            )
            # Convertir la grille en chaîne
            contenu = grid.to_str()
            if not isinstance(contenu, str):
                raise ValueError("La méthode to_str() doit retourner une chaîne de caractères")

            # Écrire dans le fichier
            with open(file_path, "w", encoding="utf-8") as fichier:
                fichier.write(contenu)
            print(f"Grille exportée avec succès dans '{file_path}'")
        except FileNotFoundError:
            print(f"Erreur : Le chemin spécifié '{folder_path}' est introuvable.")
        except IOError as io_err:
            print(f"Erreur d'écriture dans le fichier : {io_err}")
        except Exception as e:
            print(f"Erreur inattendue lors de l'exportation : {e}")
