# On retrouve ici les requetes SQL, la classe FileAttente et les méthodes de classe.

import database as db
from file_attente.File_attente import File


class FileAttente:
    connexion = db.connexion_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass
        
        

    @classmethod
    def ajouter_personne_en_attente(cls, fil:File):
        sql = "INSERT INTO fileattente (nom, prioritaire) VALUES (%s,%s)"
        params = (fil.nom, bool(fil.prioritaire)) # Le type bool est converti en TINYINT (0-1) par MySQL dans le choix du datatype.

        try:
            FileAttente.cursor.execute(sql, params)
            FileAttente.connexion.commit()
            statut = "prioritaire" if fil.prioritaire else "non-prioritaire"
            message = f"{fil.nom} a été ajouté(e) en tant que client {statut}."

        except Exception as e:
            print(f"Erreur {e} pendant l'ajout à la file")
        return message
    

    @classmethod        
    def ajouter_personne_prioritaire(cls,fil:File):
        fil.prioritaire = True
        return FileAttente.ajouter_personne_en_attente(fil)

    @classmethod
    def supprimer_personne_de_attente(cls):
        sql_prioritaire = "SELECT id, nom FROM fileattente WHERE prioritaire = TRUE ORDER BY id ASC LIMIT 1"
        sql_non_prioritaire = "SELECT id, nom FROM fileattente WHERE prioritaire = FALSE OR prioritaire IS NULL ORDER BY id ASC LIMIT 1"
        sql_suppression = "DELETE FROM fileattente WHERE id = %s"

        try:
            FileAttente.cursor.execute(sql_prioritaire)
            personne = FileAttente.cursor.fetchone()

            if not personne:
                FileAttente.cursor.execute(sql_non_prioritaire)
                personne = FileAttente.cursor.fetchone()

            elif personne:
                id_personne, nom_personne = personne
                FileAttente.cursor.execute(sql_suppression, (id_personne,))
                FileAttente.connexion.commit()
                message = f"Succès! {nom_personne} ne figure plus dans la file d'attente."
        
        except Exception as e:
            message = f"Erreur : {e} pendant la suppression de {nom_personne} de la file d'attente. "

        return message
