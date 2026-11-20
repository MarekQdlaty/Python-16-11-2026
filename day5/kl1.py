# klasa - przepis, szablon
# cechy (zmienne)
# metody (funkcja)
# obiekt - instancja klasy
# pardygmaty: hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
# klasa musi byc najpierw zadeklaorowana
# tworzenie obiektu -> __init__ (konstruktor)
# __del__ - destruktor

# PascalCase, UpperCamelCase
class Human:
    """Klasa Human opisująca człowieka w Pythonie"""

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print("Mam na imię:", self.imie)

    # napisac metode
    # ruszaj()
    # w zaleznosci od płci
    # ruszyłem, ruszyłam
    # self - obiekt


print(Human.__doc__)
# Klasa Human opisująca człowieka w Pythonie
#  cd day5
#  pydoc -b kl1.py - serwer dokumentacji
#  pydoc -w kl1 - plik html z dokumentacyją

cz1 = Human()
print(cz1)
# <__main__.Human object at 0x0000020C7A0B4C20>
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz1.imie = "Ania"
cz1.wiek = 35

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Ania
# 35
# k

cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 67
cz2.plec = "m"

print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Radek
# 67
# m

cz1.powitanie()
cz2.powitanie()
# Mam na imię: Ania
# Mam na imię: Radek
