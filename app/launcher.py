import os
import copy

from app.src.engine.generator import Generator
from app.src.engine.solver import Solver
from app.src.importer import Importer
from app.src.exporter import Exporter

def display_menu_principal() -> str:
    """Affiche le menu principal et demande à l'utilisateur de choisir ce qui veut faire."""
    print("""
       +----------------------------------------+
       | Bienvenue dans le logiciel PathSolver! |
       | Sélectionnez une action à effectuer :  |
       |     1. Importer une grille             |
       |     2. Générer une grille              |
       |     3. Trouver un chemin               |
       |     4. Afficher la grille              |
       |     5. Exporter la grille              |
       |     6. Comparaison des heuristiques    |
       |     7. Quitter                         |
       +----------------------------------------+
       """)
    choix_input = input("Votre choix : ")
    while choix_input not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Choix invalide, veuillez choisir un nombre entre 1 et 7")
        choix_input = input("Votre choix : ")
    return choix_input

def display_menu_resolution() -> str:
    """Affiche le menu pour choisir une heuristique."""
    print("""
       +----------------------------------------+
       | Veuillez choisir un calcul             |
       | d'heuristique :                        |
       |     1. Dijkstra                        |
       |     2. Manhattan                       |
       |     3. Euclidienne                     |
       |     4. Retour                          |
       +----------------------------------------+
       """)
    choix_input = input("Votre choix : ")
    while choix_input not in ["1", "2", "3", "4"]:
        print("Choix invalide, veuillez choisir un nombre entre 1 et 4")
        choix_input = input("Votre choix : ")
    return choix_input

def choisir_fichier() -> str:
    """Méthode pour choisir un fichier depuis le répertoire spécifié."""
    fichiers = [f for f in os.listdir("ressources/entree/") if os.path.isfile(os.path.join("ressources/entree/", f))]
    print("Liste des fichiers trouvés :")
    index = 0
    for fichier in fichiers:
        index += 1
        print(f"{index} - {fichier}")

    fichier_incorrect = True
    while fichier_incorrect:
        fichier_input = input("Veuillez entrer le numéro du fichier : ")
        if int(fichier_input) > 0 and int(fichier_input) <= index:
            fichier_incorrect = False
        else:
            print("Fichier inexistant")
    return "ressources/entree/" + fichiers[int(fichier_input) - 1]

def display_menu_comparaison() -> tuple[str, str]:
    """Affiche le menu pour choisir une comparaison d'heuristique."""
    print("""
       +----------------------------------------+
       | Veuillez choisir un premier calcul     |
       | d'heuristique à comparer :             |
       |     1. Dijkstra                        |
       |     2. Manhattan                       |
       |     3. Euclidienne                     |
       +----------------------------------------+
       """)
    choix_input_1 = input("Votre choix : ")
    while choix_input_1 not in ["1", "2", "3"]:
        print("Choix invalide, veuillez choisir un nombre entre 1 et 3")
        choix_input_1 = input("Votre choix : ")
    print("""
        +----------------------------------------+
        | Veuillez choisir une autre méthode     |
        | de calcul d'heuristique différente de  |
        | la première pour la comparer :         |
        |     1. Dijkstra                        |
        |     2. Manhattan                       |
        |     3. Euclidienne                     |
        +----------------------------------------+
        """)
    choix_input_2 = input("Votre choix : ")
    while choix_input_2 not in ["1", "2", "3"] or choix_input_2 == choix_input_1:
        print("Choix invalide, veuillez choisir un nombre entre 1 et 3 et différent du premier")
        choix_input_2 = input("Votre choix : ")
    return choix_input_1, choix_input_2

def display_menu_information_generation() -> tuple[int, int, float, bool]:
    """Affiche le menu pour renseigner les informations de génération de grille."""
    print("Veuillez renseigner une hauteur de la grille à générer(>=3)")
    hauteur = input("Votre choix : ")
    while int(hauteur) < 3:
        print("Hauteur invalide, veuillez renseigner une hauteur supérieure ou égale à 3")
        hauteur = input("Votre choix : ")

    print("Veuillez renseigner une largeur de la grille à générer(>=3)")
    largeur = input("Votre choix : ")
    while int(largeur) < 3:
        print("Largeur invalide, veuillez renseigner une largeur supérieure ou égale à 3")
        largeur = input("Votre choix : ")

    print("Veuillez renseigner un taux de génération de murs (exemple 0.2)")
    taux = input("Votre choix : ")
    while float(taux) < 0 or float(taux) > 1:
        print("Taux invalide, veuillez renseigner un taux entre 0 et 1")
        taux = input("Votre choix : ")

    print("Voulez-vous que le départ et l'arrivée soient éloignées (oui ou non)")
    option = input("Votre choix : ")
    while option not in ["oui", "non", "o", "n"]:
        print("Choix invalide, veuillez choisir une réponse entre oui ou non")
        option = input("Votre choix : ")
    if option in ["oui", "o"]:
        option = True
    else:
        option = False
    return int(largeur), int(hauteur), float(taux), option

if __name__ == '__main__':
    grid = None
    grid_saved = None
    print("""
    ██████╗     █████╗    ████████╗   ██╗  ██╗   ███████╗   ████████╗   ██╗      ██╗   ██╗   ███████╗   ██████╗  
    ██╔══██╗   ██╔══██╗   ╚══██╔══╝   ██║  ██║   ██╔════╝   ██║   ██║   ██║      ██║   ██║   ██╔════╝   ██╔══██╗
    ██████╔╝   ███████║      ██║      ███████║   ███████╗   ██║   ██║   ██║      ██║   ██║   ███████╗   ██████╔╝
    ██╔═══╝    ██║  ██║      ██║      ██╔══██║   ╚════██╗   ██║   ██║   ██║      ╚██╗ ██╔╝   ██╔════╝   ██╔══██╗
    ██║        ██║  ██║      ██║      ██║  ██║   ██████╔╝   ████████║   ██████╗   ╚████╔╝    ███████╗   ██║  ██║
    ╚═╝        ╚═╝  ╚═╝      ╚═╝      ╚═╝  ╚═╝   ╚═════╝    ╚═══════╝   ╚═════╝    ╚═══╝     ╚══════╝   ╚═╝  ╚═╝
    """)
    choix = 0
    while choix != "7":
        choix = display_menu_principal()
        if choix == "1":
            path = choisir_fichier()
            grid_saved = Importer.load_grid_from_file(path)
            grid = None
        elif choix == "2":
            choix_generation = display_menu_information_generation()
            grid_saved = Generator.generate_grid(choix_generation[0], choix_generation[1], choix_generation[2], choix_generation[3])
            grid = None
            print("Grille générée avec succès!")
            print(grid_saved.__str__())
        elif choix == "3":
            if grid_saved is None:
                print("Veuillez d'abord importer ou générer une grille!")
            else:
                grid = copy.deepcopy(grid_saved)
                choix_heuristique = display_menu_resolution()
                if choix_heuristique == "1":
                    grid = Solver.solve_grid(grid, "dijkstra")[0]
                if choix_heuristique == "2":
                    grid = Solver.solve_grid(grid, "ville")[0]
                if choix_heuristique == "3":
                    grid = Solver.solve_grid(grid, "pythagore")[0]
        elif choix == "4":
            if grid is not None:
                print("Affichage de la grille")
                print(grid.__str__())
            elif grid_saved is not None:
                print("Affichage de la grille")
                print(grid_saved.__str__())
            else:
                print("Veuillez d'abord importer ou générer une grille!")
        elif choix == "5":
            if grid is not None:
                print("Exportation de la grille")
                Exporter.export_grille(copy.deepcopy(grid), "/ressources/sortie/")
            elif grid_saved is not None:
                print("Exportation de la grille")
                Exporter.export_grille(copy.deepcopy(grid_saved), "/ressources/sortie/")
            else:
                print("Veuillez d'abord importer ou générer une grille!")
        elif choix == "6":
            choix_heuristiques = display_menu_comparaison()
            print("Veuillez choisir un nombre de répétition de comparaison des heuristiques")
            nombre_repetition_calcul_heuristique = input("Votre choix : ")
            while int(nombre_repetition_calcul_heuristique) < 1:
                print("Nombre de répétitions invalide, veuillez renseigner un nombre supérieur ou égal à 1")
                nombre_repetition_calcul_heuristique = input("Votre choix : ")

            choix_generation = display_menu_information_generation()

            liste_resultat_1 = []
            liste_resultat_2 = []
            choix_heuristiques_str = []

            if choix_heuristiques[0] == "1" or choix_heuristiques[1] == "1":
                choix_heuristiques_str.append("dijkstra")
            if choix_heuristiques[0] == "2" or choix_heuristiques[1] == "2":
                choix_heuristiques_str.append("ville")
            if choix_heuristiques[0] == "3" or choix_heuristiques[1] == "3":
                choix_heuristiques_str.append("pythagore")

            for i in range(int(nombre_repetition_calcul_heuristique)):
                grille_resolvable = False
                while not grille_resolvable: # Régénère une grille tant qu'elle n'est pas résolvable peu poser des problèmes si le taux est
                # proche ou égal à 1
                    grid = Generator.generate_grid(choix_generation[0], choix_generation[1], choix_generation[2], choix_generation[3])
                    if Solver.solve_grid(grid, "ville")[3] != 0: # Test de la grille le plus rapide
                        grille_resolvable = True
                        break
                liste_resultat_1.append(Solver.solve_grid(grid, choix_heuristiques_str[0]))
                liste_resultat_2.append(Solver.solve_grid(grid, choix_heuristiques_str[1]))
    
            total_temps_execution_1 = 0
            total_temps_execution_2 = 0
            nombre_case_total_visite_1 = 0
            nombre_case_total_visite_2 = 0
            nombre_case_total_chemin_1 = 0
            nombre_case_total_chemin_2 = 0

            for i in liste_resultat_1:
                total_temps_execution_1 += i[1]
                nombre_case_total_visite_1 += i[2]
                nombre_case_total_chemin_1 += i[3]
            for i in liste_resultat_2:
                total_temps_execution_2 += i[1]
                nombre_case_total_visite_2 += i[2]
                nombre_case_total_chemin_2 += i[3]

            print(f"Bilan pour l'heuristique : {choix_heuristiques_str[0]}")
            print(f"Durée d'exécution totale : {total_temps_execution_1:.5f} seconde(s), soit en moyenne {total_temps_execution_1 / int(nombre_repetition_calcul_heuristique):.5f} par grille")
            print(f"Nombre de case totale visitée : {nombre_case_total_visite_1} case(s), soit en moyenne {nombre_case_total_visite_1 / int(nombre_repetition_calcul_heuristique)} par grille")
            print(f"Nombre de case totale appartenant au chemin {nombre_case_total_chemin_1} case(s), soit en moyenne {nombre_case_total_chemin_1 / int(nombre_repetition_calcul_heuristique)} par grille")
            print(f"Efficacité de l'heuristique : {nombre_case_total_chemin_1 / int(nombre_case_total_visite_1) * 100} % \n")

            print(f"Bilan pour l'heuristique : {choix_heuristiques_str[1]}")
            print(f"Durée d'exécution totale : {total_temps_execution_2:.5f} seconde(s), soit en moyenne {total_temps_execution_2 / int(nombre_repetition_calcul_heuristique):.5f} par grille")
            print(f"Nombre de case totale visitée : {nombre_case_total_visite_2} case(s), soit en moyenne {nombre_case_total_visite_2 / int(nombre_repetition_calcul_heuristique)} par grille")
            print(f"Nombre de case totale appartenant au chemin {nombre_case_total_chemin_2} case(s), soit en moyenne {nombre_case_total_chemin_2 / int(nombre_repetition_calcul_heuristique)} par grille")
            print(f"Efficacité de l'heuristique : {nombre_case_total_chemin_2 / int(nombre_case_total_visite_2) * 100} %")

    print("Au revoir!")
