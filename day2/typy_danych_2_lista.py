# kolekcja

# lista - zachowuje koljność, pozwala przechować dowolną ilość danych, różnego typu na raz

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodawnaie elemntów do listy
lista.append("Piotr")
lista.append("Dariusz")
lista.append("Daniel")
lista.append("Radek")
lista.append("Marek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Natalia")
print(lista)
# ['Piotr', 'Dariusz', 'Daniel', 'Radek', 'Marek', 'Tomek', 'Zenek', 'Natalia']

print(len(lista))  # 8

# ['Piotr', 'Dariusz', 'Daniel', 'Radek', 'Marek', 'Tomek', 'Zenek', 'Natalia']
#    0         1          2          3       4        5        6         7

print(lista[1])  # Dariusz
print(lista[3])  # Radek

# print(lista[10])  # IndexError: list index out of range

print(lista[7])
print(len(lista) - 1)
print(lista[-1])  # Natalia

print(lista[-2])
# ['Piotr', 'Dariusz', 'Daniel', 'Radek', 'Marek', 'Tomek', 'Zenek', 'Natalia']
#    0         1          2          3       4        5        6         7
#    -8        -7         -6         -5      -4       -3       -2        -1

# slicowanie - fragment
print(lista[0:3])  # [start:stop], ['Piotr', 'Dariusz', 'Daniel'] -> 012
print(lista[:3])  # ['Piotr', 'Dariusz', 'Daniel']

print(lista[2:])  # ['Daniel', 'Radek', 'Marek', 'Tomek', 'Zenek', 'Natalia'], włącznie z ostatnim
print(lista[2:7])  # ['Daniel', 'Radek', 'Marek', 'Tomek', 'Zenek'] bez ostatniego

print(lista[2:10])  # ['Daniel', 'Radek', 'Marek', 'Tomek', 'Zenek', 'Natalia']
print(lista[15:20])  # []

print(lista[:])
# ['Piotr', 'Dariusz', 'Daniel', 'Radek', 'Marek', 'Tomek', 'Zenek', 'Natalia']

#    0         1          2          3       4        5        6         7
#    -8        -7         -6         -5      -4       -3       -2        -1

print(lista[2:0])  # []
print(lista[-2:0])  # [] -> [6:0]
print(lista[0:-2])  # [0:6] # ['Piotr', 'Dariusz', 'Daniel', 'Radek', 'Marek', 'Tomek']
print(lista[-5:-2])  # ['Radek', 'Marek', 'Tomek']

a = None
b = None
print(lista[a:b])  # [:]
# ['Piotr', 'Dariusz', 'Daniel', 'Radek', 'Marek', 'Tomek', 'Zenek', 'Natalia']

# wygenerowac liste z zakresu 0 do 14
# lista_15 = [0, 1, 2...]
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[::2])  # [start:stop:krok], [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[::3])  # [start:stop:krok], [0, 3, 6, 9, 12]

print(lista_15[::-1])  # odwrotna kolejność
# [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(list(range(5, 15, 2)))  # [5, 7, 9, 11, 13] (start, stop, krok)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista1 + lista2)  # [1, 2, 3, 4, 5, 6]

lista1.append(list(range(5, 9)))  # jako lista w lista
print(lista1)  # [1, 2, 3, [5, 6, 7, 8]]

lista2.extend(list(range(5, 8)))  # jako kolejne elementy listy
print(lista2)  # [4, 5, 6, 5, 6, 7]

# python nie ma tablic

tablica = [[1, 2], [3, 4]]
print(tablica)  # [[1, 2], [3, 4]]
# numpy - biblioteka do pracy z tablicami/macierzami

print(lista)
# ['Piotr', 'Dariusz', 'Daniel', 'Radek', 'Marek', 'Tomek', 'Zenek', 'Natalia']

# nadpisanie na wskazanym indeksie
lista[6] = "Mirek"
print(lista)
# ['Piotr', 'Dariusz', 'Daniel', 'Radek', 'Marek', 'Tomek', 'Mirek', 'Natalia']

# lista[:-2] = "Mirek"
# print(lista)
# # ['M', 'i', 'r', 'e', 'k', 'Mirek', 'Natalia']

# dopisanie elementu na wskazanym indeksie
lista.insert(1, "Ola")
print(lista)
# ['Piotr', 'Ola', 'Dariusz', 'Daniel', 'Radek', 'Marek', 'Tomek', 'Mirek', 'Natalia']

# sprawdzenie indeksu
print(lista.index("Radek"))  # 4
