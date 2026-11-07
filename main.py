#version 1

def affichier_menu():
    print("GESTION DES TACHEs")
    print("1.Ajoute une tache")
    print("2.Afficher les taches")
    print("3.Rechercher  une tache")
    print("0.Quitter ")


def lancer_application():
    taches = []
    
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()
        
        if choix == "1":
            titre = input("Titre de la tâche : ").strip()
            if titre == "":
                print("Erreur : Le titre ne peut pas être vide.")
            else:
                taches.append(titre)
                print("Tâche ajoutée avec succès.")
                
        elif choix == "2":
            if not taches:
                print("La liste des tâches est vide.")
            else:
                print("--- Liste des tâches ---")
                for index, tache in enumerate(taches, start=1):
                    print(f"{index}. {tache}")
                    
        elif choix == "3":
            mot_cle = input("Entrez le mot-clé à rechercher : ").strip().lower()
            resultats = [t for t in taches if mot_cle in t.lower()]
            if not resultats:
                print("Aucune tâche ne contient ce mot-clé.")
            else:
                print("--- Résultats de la recherche ---")
                for r in resultats:
                    print(f"- {r}")
                    
        elif choix == "0":
            print("Fermeture du programme...")
            break
        else:
            print("Option invalide, veuillez choisir entre 0 et 3.")

if _name_ == "_main_":
    lancer_application