#On retrouve ici le menu de la file d'attente.

from file_attente.File_attente import File
from file_attente.File_dao import FileAttente

def menu_file():
    while True:

        print("\nMenu de la File d'Attente\n")
        print("1- Ajouter une Personne Prioritaire à la File")
        print("2- Ajouter une Personne à la File")
        print("3- Supprimer une Personne de la File\n")
        print("4- Quitter")
        
        choix = input("Faites votre Choix: ")

        if choix == "1":
            nom = input("Tapez le Nom de la Personne Prioritaire à Ajouter : ")
            personne_prioritaire = File(nom=nom, prioritaire=True)
            message = FileAttente.ajouter_personne_prioritaire(personne_prioritaire)

            print(message)
            
        elif choix == "2":
            nom = input("Entrez le nom de la personne à ajouter à la file d'attente : ")
            nouvelle_personne = File(nom=nom, prioritaire=False)
            message = FileAttente.ajouter_personne_en_attente(nouvelle_personne)

            print(message)
               
        elif choix == "3":
            message = FileAttente.supprimer_personne_de_attente()

            print(message)
            
        elif choix == "4":
            print("Fin des opérations")

            return
        
        else:
            print("Votre choix n'est pas valide.")
