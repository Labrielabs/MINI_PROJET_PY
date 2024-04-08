# On retrouve ici les getters et setters

class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
