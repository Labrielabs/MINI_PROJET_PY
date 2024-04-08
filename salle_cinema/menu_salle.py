# Nous retrouvons ici le menu des réservations de places de Cinéma

from salle_cinema.reservation import SalleCinema
from salle_cinema.reservation_dao import ReservationDao

def menu_salle():
    while True:

        print("\nMenu Réservations de Places - Salle Cinéma\n")

        print("1- Réserver une place")
        print("2- Afficher Places Réservées")
        print("3- Vérifier le nombre de Places Disponibles")
        print("4- Rechercher les Réservations d'une Personne")
        print("5- Réserver une Place Spéciale")
        print("6- Annuler une Réservation\n")
        print("7- Quitter\n")
        
        choix = input("Faites un Choix: ")

        if choix == "1":

            nom = input("À quel nom devons-nous faire la réservation : ")
            place = input("Quel siège souhaitez-vous réserver : ")

            reservation = SalleCinema(nom, place, place_speciale=0)
            message = ReservationDao.reserver_place(reservation)

            print(message)

            
        elif choix == "2":

            reservations, message = ReservationDao.afficher_places_reservees()

            print(message)

            for reserv in reservations:

                print(f"Place {reserv[0]} réservée ")

            
        elif choix == "3":

            message = ReservationDao.nombre_places_disponibles()

            print(message)

            
        elif choix == "4":

            nom = input("Tapez le nom pour rechercher parmi les réservations : ")

            reservations = ReservationDao.filtrer_reservations_par_personne(nom)

            for reserv in reservations:

                print(f"Place {reserv[1]} réservée pour {nom}: ")

                
        elif choix == "5":

            nom = input("À quel nom doit-on faire la réservation en place spéciale ? : ")
            place_speciale = input("Quelle place spéciale souhaitez-vous réserver ? : ")

            reservation = SalleCinema(nom, place=None, place_speciale=place_speciale) 
            message = ReservationDao.reserver_place_speciale(reservation)

            print(message)


        elif choix == "6":

            nom = input("Tapez le nom lié à la réservation que vous souhaitez annuler : ")

            message = ReservationDao.annuler_reservation(nom)

            print(message)


        elif choix == "7":

            print("Fin des opérations")

            return
        
        
        else:

            print("Votre choix est invalide")