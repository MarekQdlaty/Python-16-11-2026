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


print(Human.__doc__)
# Klasa Human opisująca człowieka w Pythonie
#  cd day5
#  pydoc -b kl1.py - serwer dokumentacji
#  pydoc -w kl1 - plik html z dokumentacyją

cz1 = Human()
print(cz1)
# <__main__.Human object at 0x0000020C7A0B4C20>
