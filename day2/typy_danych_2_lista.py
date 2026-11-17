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
