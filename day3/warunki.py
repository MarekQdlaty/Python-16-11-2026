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

punkty = int(input("Podaj liczbę punktów: "))

if punkty >= 90:
    print("Bardzo dobry")
elif punkty >= 60:
    print("Egzamin zdany")
else:
    print("Niezdany")

a = "Radek"
# jezeli długosc tekstu wieksza niz 3 to wypisac:
# Długość wynosi: ... i jest większa niż 3.
