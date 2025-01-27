from app.src.engine.generator import Generator
def display_menu() -> str:
    """
       Affiche le menu principal et demande à l'utilisateur de choisir ce qui veut faire
       :return: le choix de l'utilisateur
       """
    # Affichage menu principal et choix de l'utilisateur
    # 1. Joueur vs Joueur
    # 2. Joueur vs IA
    # 3. IA vs IA
    # 4. Quitter
    print("""
       +----------------------------------------+
       | Bienvenue dans le logiciel PathSolver! |
       | Sélectionnez une action à effectuer :  |
       |     1. Importer un labyrinthe          |
       |     2. Générer un labyrinthe           |
       |     3. Résoudre un labyrinthe          |
       |     4. Quitter                         |
       +----------------------------------------+
       """)
    choix_input = input("Votre choix : ")
    while choix_input not in ["1", "2", "3" ,"4"]:
        print("Choix invalide, veuillez choisir un nombre entre 1 et 4")
        choix_input = input("Votre choix : ")

    return choix_input

if __name__ == '__main__':
    grid = None
    print("""
    ██████╗     █████╗    ████████╗   ██╗  ██╗   ███████╗   ████████╗   ██╗      ██╗   ██╗   ███████╗   ██████╗  
    ██╔══██╗   ██╔══██╗   ╚══██╔══╝   ██║  ██║   ██╔════╝   ██║   ██║   ██║      ██║   ██║   ██╔════╝   ██╔══██╗
    ██████╔╝   ███████║      ██║      ███████║   ███████╗   ██║   ██║   ██║      ██║   ██║   ███████╗   ██████╔╝
    ██╔═══╝    ██║  ██║      ██║      ██╔══██║   ╚════██╗   ██║   ██║   ██║      ╚██╗ ██╔╝   ██╔════╝   ██╔══██╗
    ██║        ██║  ██║      ██║      ██║  ██║   ██████╔╝   ████████║   ██████╗   ╚████╔╝    ███████╗   ██║  ██║
    ╚═╝        ╚═╝  ╚═╝      ╚═╝      ╚═╝  ╚═╝   ╚═════╝    ╚═══════╝   ╚═════╝    ╚═══╝     ╚══════╝   ╚═╝  ╚═╝
    """)
    choix = 0
    while choix != "4":
        choix = display_menu()
        if choix == "1":
            print("TODO")
            # TODO
        elif choix == "2":
            # Sélection de la hauteur de la grille à générer
            hauteur = 2
            print("Veuillez renseigner une hauteur de la grille à générer(>=3)")
            hauteur = input("Votre choix : ")
            while hauteur < 3:
                print("Hauteur invalide, veuillez renseigner une hauteur supérieure ou égale à 3")
                hauteur = input("Votre choix : ")

            # Sélection de la largeur de la grille à générer
            largeur = 2
            print("Veuillez renseigner une largeur de la grille à générer(>=3)")
            largeur = input("Votre choix : ")
            while largeur < 3:
                print("Hauteur invalide, veuillez renseigner une largeur supérieure ou égale à 3")
                largeur = input("Votre choix : ")

            # Sélection du taux d'appartion des croix dans la grille à générer
            taux = -1
            print("Veuillez renseigner un taux de génération de murs (exemple 0.2)")
            taux = input("Votre choix : ")
            while taux < 0 or taux > 1:
                print("Taux invalide, veuillez renseigner un taux entre 0 et 1")
                taux = input("Votre choix : ")

            # Sélection de l'option du départ et d'arrivé éloignées
            option = None
            print("Voulez-vous que le départ et l'arrivé soit éloignées (oui ou non)")
            option = input("Votre choix : ")
            while option not in ["oui", "non"]:
                print("Choix invalide, veuillez choisir une réponse entre oui ou non")
                option = input("Votre choix : ")
            if option == "oui":
                option = True
            else:
                option = False
            grid = Generator.generate_grid(int(largeur), int(hauteur), float(taux), option)
            print("Grille générée avec succès!")
            print(grid.__str__())
        elif choix == "3":
            if grid is None:
                print("Veuillez d'abord importer ou générer une grille!")
            else :
                print("exportation de la grille")
                #TODO exporter la grille 
    print("Au revoir!")