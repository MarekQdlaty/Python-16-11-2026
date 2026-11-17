# zbior (set) - przechowuja unikalne wartości
# nie zachowują kolejności
# nie mają indeksu
# hashowane

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 777]
zbior = set(lista)  # rzutowanie na zbiór
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

sortowanie = sorted(zbior)
print(sortowanie)
# [11, 22, 33, 44, 55, 66, 777]

# pusty zbiór
zb2 = set()  # tylko i wyłącznie słówkiem set()
print(zb2)  # set() - pusty zbiór
print(type(zb2))  # <class 'set'>

# dodanie do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(24)
zbior.add(18)
zbior.add(33)
zbior.add(33)
zbior.add(25)
zbior.add(33)
zbior.add(33)
zbior.add(12)
zbior.add(33)
print(zbior)
# {33, 66, 777, 11, 44, 12, 18, 22, 55, 24, 25}

# usunięcie ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 12, 18, 22, 24, 25}

# pop()
print(zbior.pop())  # 33 usunie pierwszy element

zmienna = zbior.pop()
print(f"Zmienna: {zmienna}")  # Zmienna: 66
print("Zmienna:", zmienna)  # Zmienna: 66

zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}
