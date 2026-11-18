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

zarobki = int(input("Podaj zarobki: "))

podatki = 0
if zarobki < 10_000:
    podatek = 0
else:
    podatek = 0.9

print(f'podatek wynosi: {zarobki * podatek} pln.')
