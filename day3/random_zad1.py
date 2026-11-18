import random

# działania na liczbach losowych

# Return random integer in range [a, b], including both end points.
print(random.randint(1, 100))  # int od 1 do 100 włącznie

print(random.randrange(1, 100))  # od 1 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # 0.6030281207968737 od 0 do 0.999999
print(random.random() * 7)  # 2.5429644423743794 od 0 do 6.999999

lista = ["Radek", "Tomek", "Zenek", "Ania", "Kasia"]
print(lista[random.randrange(len(lista))])  # Zenek

print(random.choice(lista))  # Zenek

# ctrl shift f - wyszukiwanie w projekcie
lista_kul = list(range(1, 50))  # od 1 do 49
kula = random.choice(lista_kul)
lista_kul.remove(kula)
print(kula)  # 23
print(lista_kul)
print(kula in lista_kul)

print(random.choices(lista_kul, k=6))  # [5, 9, 36, 42, 36, 14], z powtórzeniami
print(random.sample(lista_kul, k=6))  # [18, 21, 28, 17, 10, 6], bez powtórzeń
print(random.sample(lista_kul, 6))  # [49, 20, 34, 35, 32, 6], [21, 24, 30, 4, 44, 19]
