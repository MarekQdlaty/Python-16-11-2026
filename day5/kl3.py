class Ptak:
    """Klasa opisująca ptaka w Pythonie"""

    def __init__(self, gatunek, szybkosc):
        """
        Inicjalizacja
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)
