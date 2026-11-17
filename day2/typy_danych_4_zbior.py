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
