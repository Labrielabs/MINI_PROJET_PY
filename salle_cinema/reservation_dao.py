# On retrouve ici les requetes SQL, la classe ReservationDao et les méthodes de classe.

import database as db
from salle_cinema.reservation import SalleCinema

class ReservationDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass
        
        

    @classmethod
    def reserver_place(cls, reserv:SalleCinema): 
            sql = "INSERT INTO reservation (nom, place) VALUES (%s, %s)"
            params = (reserv.nom, reserv.place)

            try:
                ReservationDao.connexion.cursor()
                ReservationDao.cursor.execute(sql, params)
                ReservationDao.connexion.commit()

                message = f"Réservé la place {reserv.place} pour {reserv.nom}."

            except Exception as e:

                message = f"Erreur pendant l'ajout: {e}"
            
            return message
    
    
    @classmethod
    def afficher_places_reservees(cls):
        sql = "SELECT place FROM reservation"

        try:
            ReservationDao.cursor.execute(sql)
            reservations = ReservationDao.cursor.fetchall()
            ReservationDao.cursor.close()

            message = "Réussi"

        except Exception as e:

            message = f"Erreur pendant l'affichage des réservations: {e}"

        return reservations, message
    

    @classmethod
    def nombre_places_disponibles(cls):
        capacite_totale = 50
        sql = "SELECT COUNT(*) FROM reservation"

        try:
            ReservationDao.cursor.execute(sql)
            (nombre_reservations,) = ReservationDao.cursor.fetchone()
            places_disponibles = capacite_totale - nombre_reservations

            message = f"Places Disponibles : {places_disponibles}"

        except Exception as e:

            print(f"Erreur pendant l'affichage des places restantes : {e}")

        return message
    
    
    @classmethod
    def filtrer_reservations_par_personne(cls,nom):
        sql = "SELECT * FROM reservation WHERE nom = %s"

        try:
            ReservationDao.connexion.cursor()
            ReservationDao.cursor.execute(sql, (nom,))
            reservations = ReservationDao.cursor.fetchall()
    
        except Exception as e:

            print(f"Erreur : {e} pendant le filtrage des réservations au nom de : {nom}")

        return reservations
    
    
    @classmethod
    def annuler_reservation(cls, nom):
        sql = "DELETE FROM reservation WHERE nom = %s"

        try:
            ReservationDao.connexion.cursor()
            ReservationDao.cursor.execute(sql, (nom,))
            ReservationDao.connexion.commit()
            
            message = f"Réservations de {nom} annulées avec succès."

        except Exception as e:

            print(f"Erreur : {e} pendant l'annulation des réservations de {nom}")

        return message
    
    
    @classmethod
    def reserver_place_speciale(cls,reserv:SalleCinema):
        sql = "INSERT INTO reservation (nom, place_speciale) VALUES (%s, %s)"
        params = (reserv.nom, reserv.place_speciale)

        try:
            ReservationDao.connexion.cursor()
            ReservationDao.cursor.execute(sql, params)
            ReservationDao.connexion.commit()

            message = f"Place spéciale {reserv.place_speciale} réservée au nom de {reserv.nom}."

        except Exception as e:
            
            message = f"Erreur : {e} pendant la réservation."
            
        return message