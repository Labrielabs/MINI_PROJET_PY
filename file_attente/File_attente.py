# On retrouve ici les getters et setters

class File:
    def __init__(self, nom, prioritaire):
        self.__nom = nom
        self.__prioritaire = prioritaire

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prioritaire(self):
        return self.__prioritaire

    @prioritaire.setter
    def prioritaire(self, value):
        self.__prioritaire = value