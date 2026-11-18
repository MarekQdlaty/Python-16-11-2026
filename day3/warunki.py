# instrukcje warunkowe
# instrukce sterowania przepływem programu

# if
# w zaleznosci od warunku (True lub False) wykonuje jeden lub drugi blok programu
# wyrażenie zwraca bool

odp = True

if odp: print("test")
# test

if odp:
    # blok programu wykonany gdy warunek True
    print('test')
# test

# debugger - pozwala analizowac program linijka po linijce
# puapka - miejsca wstrzymania programu
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Ciag dalszy")

odp = "Radek"

if odp:
    print("Działa")
# Działa

if odp == "Radek":
    print("Jestem Radek")
else:
    print("To nie Radek")
# Jestem Radek

odp = "Tomek"
if odp == "Radek":
    print("Jestem Radek")
elif odp == "Tomek":
    print("Jestem Tomek")
else:
    print("Ani Radek ani Tomek")

# Jestem Tomek

odp = 0
if odp:
    print("True")
else:
    print("False")
# False

# pobieramy od uzytkownika liczbe od 0 do 100
# jesli wynik wynosi 90  i wiecej -> Bardzo dobry
# jesli od 60 do 89 -> Egzamin zdany
# jesli ponizej 60 -> niezdany

# punkty = int(input("Podaj liczbę punktów: "))
#
# if punkty >= 90:
#     print("Bardzo dobry")
# elif punkty >= 60:
#     print("Egzamin zdany")
# else:
#     print("Niezdany")

a = "Radek"
# jezeli długosc tekstu wieksza niz 3 to wypisac:
# Długość wynosi: ... i jest większa niż 3.

if len(a) > 3:
    print(f"Długosc wynosi: {len(a)} i jest większy niż 3")
# Długosc wynosi: 5 i jest większy niż 3

n = len(a)
if n > 3:
    print(f"Długosc wynosi: {n} i jest większy niż 3")
# Długosc wynosi: 5 i jest większy niż 3

# operator morsa, walrus operator
if (n := len(a)) > 3:
    print(f"Długosc wynosi: {n} i jest większy niż 3")

# pobrac zarobki
# jesli zarobki mniejsze niz 10_000 podatek 0%
# dla pozostałych podatek 90%
# wypisz obliczony podatek
print(f"{90:.2%}")

# dodac podatek 20% dla przedziału 10000 do 39999
# dodac podatek 40% dla przedziału 40000 do 100000

# zarobki = int(input("Podaj zarobki: "))

# # kolejnosć ma znaczenie
# podatki = 0
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f'podatek wynosi: {zarobki * podatek:.2f} pln.')

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi: {rabat}")

# operator warunkowy
rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")

# napisac test z...
# trzy patania
# dodac punktację


# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
# odp = input("Co jest stolicą Polski?")
# punkty = 0
# if odp.strip().casefold() == "Warszawa".strip().casefold():
#     print("Odpowiedź prawidłowa")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Sprawdź w ksiązce na stronie 23")
#
# print("Wynik:", punkty)
#
# odp = input("Co jest stolicą Austarlii?")
# if odp.strip().casefold() == "Canbera".strip().casefold():
#     print("Odpowiedź prawidłowa")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Sprawdź w ksiązce na stronie 23")
#
# print("Wynik:", punkty)
#
# odp = input("Co jest stolicą Niemiec?")
# if odp.strip().casefold() == "Berlin".strip().casefold():
#     print("Odpowiedź prawidłowa")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Sprawdź w ksiązce na stronie 23")
#
# print("Wynik:", punkty)

# Co jest stolicą Polski?Warszawa
# Odpowiedź prawidłowa
# Wynik: 1
# Co jest stolicą Austarlii?Canbera
# Odpowiedź prawidłowa
# Wynik: 2
# Co jest stolicą Niemiec?Berlin
# Odpowiedź prawidłowa
# Wynik: 3


# zasymulujemy system zbierania logów
# typ_systemu: console, email -> inny
# console: "Stało się coś strasznego"
# email: "System email"

# jesli system jest email:
# odczytac zmienna error_level
# error, medium, inny
# do listy błedów dopisac tłumaczenie błedu

lista_b = []
typ_systemu = "email"
error_level = "medium"

if typ_systemu == "console":
    print("Stało się coś strasznego")
elif typ_systemu == "email":
    print("System email")
    # tu jestem w email
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny błąd")
else:
    print("Inny system")

print(lista_b)
