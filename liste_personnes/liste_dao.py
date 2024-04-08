# On retrouve ici les requetes SQL, la classe ListePersonneDao et les méthodes de classe.

import database as db
from liste_personnes.liste import Personne

class ListePersonneDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass
       
   
    @classmethod
    def ajouter_personne(cls, pers: Personne):
        sql = "INSERT INTO personnes (nom, age) VALUES (%s, %s)"
        params = (pers.nom, pers.age)

        try:
            ListePersonneDao.cursor.execute(sql, params)
            ListePersonneDao.connexion.commit()
            ListePersonneDao.cursor.close()

            message = f"Ajout de {pers.nom} avec succès."

        except Exception as e:
            message = "Erreur pendant l'ajout."

        return message

    @classmethod
    def afficher_personne(cls):
        sql = "SELECT * FROM personnes"

        try:
            ListePersonneDao.cursor.execute(sql)
            personnes = ListePersonneDao.cursor.fetchall()

            message = "Succès au chargement des données."

        except Exception as e:
            print(e)
            personnes = []

            message = "Erreur lors du chargement des données."

        return personnes, message

    @classmethod
    def rechercher_personne(cls, nom):
        sql = "SELECT nom, age FROM personnes WHERE nom = %s"

        try:
            ListePersonneDao.cursor.execute(sql, (nom,))
            resultats = ListePersonneDao.cursor.fetchone()

            message = "Succès à la recherche."

        except Exception as e:
            resultats = []
            message = "Erreur pendant la recherche:"

        return resultats, message

    @classmethod
    def filtre_age(cls, min_age, max_age):
        sql = "SELECT nom, age FROM personnes WHERE age BETWEEN %s AND %s"

        try:
            ListePersonneDao.cursor.execute(sql, (min_age, max_age))
            resultat = ListePersonneDao.cursor.fetchall()
            
            message = "Succès au filtrage par âge."

        except Exception as e:
            resultat = []
            message = "Erreur pendant le filtrage par âge."

        return resultat, message