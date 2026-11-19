# pętla - mozliwosc wykonia kodu wielokrotnie
# for - pętla iterayjna

for i in range(10):  # od 0 do 9
    print(i)

print(50 * "-")
for i in range(20):  # od 0 do 19
    pass  # nic nie rób

print(i)  # 19

for i in range(5, 10):  # od 5 do 9
    print(i)

for _ in range(10):  # niema zmienna
    print("Test podłoga")
    print(_)

for i in range(3):
    for j in range(3):
        print(f"{i=}, {j=}")

for i in range(5):
    print(i * 2)
    print(i + 2)

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# parzyste do listy
lista3 = []
for i in range(10):
    if i % 2 == 0:
        lista3.append(i)

print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

# przerobic zadanie lotto na petle
# wylosowane do nowej listy
import random

lista_wyl = []
lista_kul = list(range(1, 50))

for _ in range(6):
    kula = random.choice(lista_kul)
    lista_kul.remove(kula)
    # print(kula)
    lista_wyl.append(kula)

print(lista_wyl)  # [8, 11, 45, 7, 9, 25]

# wypisac elementy z listy lista_wyl
for i in range(len(lista_wyl)):  # i jest indeksem
    print(lista_wyl[i])

for i in lista_wyl:  # pod i podstawi kolejne elementy
    print(i)

lista_nazwy = ['Ala', 'Tomek', "Zenek", "Basia"]

for p in lista_nazwy:
    print(p)

# Ala
# Tomek
# Zenek
# Basia

# 0 Ala