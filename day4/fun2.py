# funkcje zwracające wynik

a = 9
b = 98


def dodaj():
    return a + b  # zwraca wynik dodawania


print(dodaj())  # 107
wynik = dodaj()
print(wynik)  # 107


# funkcja odejmij, z trzema arg domyslnymi
def odejmj(a=0, b=0, c=0):
    return a - b - c


print(odejmj())
print(odejmj(1, 2, 3))
print(odejmj(1, 2))

print(50 * "-")
print(odejmj(a=1, b=2, c=6))

print(odejmj(1, 2, c=90))
# --------------------------------------------------
# -7
# -91

print(dodaj() + dodaj())  # 214
