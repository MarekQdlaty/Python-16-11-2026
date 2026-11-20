from abc import ABC, abstractmethod


class Ptak(ABC):
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

    @abstractmethod  # metoda abstarkcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """Klasa Kura, dziedziczy po klasie Ptak"""

    def __init__(self, gatunek):
        # musimy wywołąc nadrzędny konstruktor
        # super() - klasa nadrzędna
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):  # musi byc
        print("ko ko ko ko")


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzel", 50)
# or1.latam()
# # Tu Orzel Lecę z szybkością 50
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()

kur2 = Kura("Kura zielononóżka")
kur2.latam()  # Tu Kura zielononóżka Ja nie latam.
kur2.wydaj_odglos() # ko ko ko ko
