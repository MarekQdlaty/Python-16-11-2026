class Human:
    """Klasa Human opisująca człowieka w Pythonie"""

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstrukotr)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print("Mam na imię:", self.imie)

    # wypisz_wiek(), wypisz_wzrost()

    # __str__
    def __str__(self):
        return f"{self.imie=}, {self.wiek=}, {self.plec=}, {self.wzrost=}"


cz1 = Human("Radek", 45, 190, "m")
cz1.powitanie()  # Mam na imię: Radek
print(cz1)
# self.imie='Radek', self.wiek=45, self.plec='m', self.wzrost=190

cz2 = Human("Anna", 23, 170)
print(cz2)
# self.imie='Anna', self.wiek=23, self.plec='k', self.wzrost=170
