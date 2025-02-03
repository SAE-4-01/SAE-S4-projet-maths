import os

def export_grille(self, chemin_fichier="grille_exportée.txt"):
    """
    Exporte la grille dans un fichier texte à l'emplacement spécifié
    """
    try:
        # Vérification de l'existence du répertoire
        dossier = os.path.dirname(chemin_fichier)
        if dossier and not os.path.exists(dossier):
            os.makedirs(dossier)

        contenu = self.to_str()
        with open(chemin_fichier, "w") as fichier:
            fichier.write(contenu)
        print(f"Grille exportée avec succès dans '{chemin_fichier}'")
    except Exception as e:
        print(f"Erreur lors de l'exportation : {e}")


grille = Grille(4, 4)
grille.export_grille("/chemin/vers/mon/dossier/grille.txt")
