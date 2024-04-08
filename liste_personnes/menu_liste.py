#On retrouve ici le menu de la liste des personnes.

from liste_personnes.liste import Personne
from liste_personnes.liste_dao import ListePersonneDao

def menu_liste():
    while True:

        print("\nMenu des Personnes.\n")
        print("1- Ajouter une personne.")
        print("2- Afficher toutes les personnes.")
        print("3- Recherche par nom.")
        print("4- Recherche par age.\n")
        print("5- Quitter\n")

        choix = input("Sélectionnez une option (1-4): ")

        if choix == '1':

            nom = input("Tapez le nom de la personne : ")
            age = input("Tapez l'âge de la personne : ")

            personne = Personne(nom, age)
            message = ListePersonneDao.ajouter_personne(personne)

            print(message)
            
        elif choix == '2':

            personnes, message = ListePersonneDao.afficher_personne()

            if personnes:

                for personne in personnes:

                    print(f"Nom : {personne[0]}, Age : {personne[1]}")

            else:

                print(message)

        elif choix == '3':

            nom = input("Tapez le nom de la personne que vous recherchez : ")
            resultats, message = ListePersonneDao.rechercher_personne(nom)

            if resultats:
                    
                    print(f"Nom : {resultats[0]}, Age : {resultats[1]}")

            else:

                print(message)

        elif choix == '4':

            min_age = input("Tapez l'âge minimum : ")
            max_age = input("Tapez l'âge maximum : ")

            resultat, message = ListePersonneDao.filtre_age(int(min_age), int(max_age))

            if resultat:

                for personne in resultat:

                    print(f"Nom : {personne[0]}, Age : {personne[1]}")

            else:

                print(message)

        elif choix == '5':

            print("Fin des opérations")

            return
        
        else:

            print("Votre choix est invalide")