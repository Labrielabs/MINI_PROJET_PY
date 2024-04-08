# On retrouve ici le module contenant la fonction de connexion à notre base de données

import mysql.connector as mysql


def connexion_db():
    return mysql.connect(
        user="root",
        password="MariaDB",
        host="localhost",
        database='liste_cinoche'
    )
