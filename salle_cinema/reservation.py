# On retrouve ici les getters et setters

class SalleCinema:
    def __init__(self, nom, place, place_speciale):
        self.__nom = nom
        self.__place = place
        self.__place_speciale = place_speciale

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        self.__place = value

    @property
    def place_speciale(self):
        return self.__place_speciale

    @place_speciale.setter
    def place_speciale(self, value):
        self.__place_speciale = value