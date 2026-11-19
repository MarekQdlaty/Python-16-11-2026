# funkcja lambda
# skrócony zapis funkcji
# konczy sie return
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(5, 90))  # -85

odejmij2 = lambda a, b: a - b
print(odejmij2(6, 90))  # -84

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

#
lista = [1, 2, 14, 24, 50, 67, 80, 100, 200, 500]
# *2
l1 = []
for i in lista:
    l1.append(i * 2)
print(l1)
# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

l2 = [i * 2 for i in lista]
print(l2)
# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

l3 = []


def zmien(x):
    return x * 2


for i in lista:
    l3.append(zmien(i))
print(l3)
# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# map() - pobiera elemnty kolekcji i wykonuje na nich funkcje
# funkce wyzszego rzedu
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# lambda jako funkcja anonimowa
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 3, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 5, lista))}")

# filtrowanie
l4 = []
for i in lista:
    if i < 3:
        l4.append(i)
print(l4)  # [1, 2]
# filter()
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter(): [1, 2]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 50, lista))}")

# Zastosowanie filter(): [1, 2]
# Zastosowanie filter(): [14, 24, 50, 67, 80, 100, 200, 500]
# Zastosowanie filter(): [67, 80, 100, 200, 500]

print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 100, lista))}")
print(
    f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 100, lista))}")  # Zastosowanie filter(): [14, 24, 50, 67, 80]

# reduce()
