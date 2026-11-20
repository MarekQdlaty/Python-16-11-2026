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


cz1 = Human("Radek", 45, 190, "m")
