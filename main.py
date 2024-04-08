# Nous retrouvons ici le menu principal de l'application.

from file_attente.File_attente import File
from file_attente.File_dao import FileAttente
from file_attente.menu_file import menu_file

from liste_personnes.liste import Personne
from liste_personnes.liste_dao import ListePersonneDao
from liste_personnes.menu_liste import menu_liste

from salle_cinema.reservation import SalleCinema
from salle_cinema.reservation_dao import ReservationDao
from salle_cinema.menu_salle import menu_salle

def main_menu():
    while True:
        print("\nGestionnaire Centralisé Automatique (GCA)\n")
        print("1- File d'Attente")
        print("2- Liste")
        print("3- Réservations")
        print("4- Quitter\n")
        
        choix = input("Votre choix : ")

        if  choix == "1":
            menu_file()
        elif  choix == "2":
            menu_liste()
        elif   choix == "3":
            menu_salle()
        elif choix == "4":
            print("\nMerci d'avoir utilisé le GCA\n")
            break
        else:
            print('Votre choix est invalide')

main_menu()
