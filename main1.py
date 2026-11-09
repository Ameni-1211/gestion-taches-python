
def afficher_menu():
    print("GESTION DES TACHES")
    print("1. Ajouter une tache")
    print("2. Afficher les taches")
    print("3. Rechercher une tache")
    print("0. Quitter")


def lancer_application():
    taches = []

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            titre = input("Titre de la tache : ").strip()

            if titre == "":
                print("Erreur : Le titre ne peut pas etre vide.")
            else:
                taches.append(titre)
                print("Tache ajoutee avec succes.")

        elif choix == "2":
            if not taches:
                print("La liste des taches est vide.")
            else:
                print("--- Liste des taches ---")
                for i in range(len(taches)):
                    print(i + 1, "-", taches[i])

        elif choix == "3":
            mot_cle = input("Mot-cle a rechercher : ").strip().lower()
            resultats = []

            for t in taches:
                if mot_cle in t.lower():
                    resultats.append(t)

            if not resultats:
                print("Aucune tache trouvee.")
            else:
                print("--- Resultats de la recherche ---")
                for r in resultats:
                    print("-", r)

        elif choix == "0":
            print("Fermeture du programme...")
            break

        else:
            print("Option invalide, choisissez entre 0 et 3.")


if __name__ == "__main__":
    lancer_application()
