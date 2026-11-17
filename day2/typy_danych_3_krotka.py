# krotka (tupla) - kolekcja tylko do odczytu, niemutowalna
# pozwala efektywniej zarządzac pamiecią
# krotke jako stałą - szczególny przypadek zmiennej

tupla_imiona = "Zenek", "Tomek", "Marek", "Ania"
print(type(tupla_imiona))
print(tupla_imiona)
# <class 'tuple'>
# ('Zenek', 'Tomek', 'Marek', 'Ania')

# tupla_liczby = 43, 55, 22.34, 11, 200
tupla_liczby = (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla jednoelementowa
tupla_jeden = (45,)
tupla_jeden = 45,
print(type(tupla_jeden))
print(tupla_jeden)

del tupla_jeden
# print(tupla_jeden)  # NameError: name 'tupla_jeden' is not defined

# tupla_liczby[0] = 123  # TypeError: 'tuple' object does not support item assignment

print(tupla_imiona)  # ('Zenek', 'Tomek', 'Marek', 'Ania')

print(tupla_imiona.index("Tomek"))  # index 1
print(tupla_imiona.count("Tomek"))  # wystepuje 1 raz

print(len(tupla_imiona))  # 4 elementy

tup = 1, 2
print(type(tup))  # <class 'tuple'>

# a - pierwszy, b - drugi

a = tup[0]
b = tup[1]
print(a, b)  # 1 2

# rozpakowanie krotki
c, d = tup  # 1, 2
print(c, d)

# zamiana wartosci
a, b = b, a
print(a, b)  # 2 1

print(tupla_imiona)  # ('Zenek', 'Tomek', 'Marek', 'Ania')
# name1, name2, name3
# name1, name2, name3 = tupla_imiona
# ValueError: too many values to unpack (expected 3, got 4)
name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Zenek Tomek ['Marek', 'Ania']

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Zenek', 'Tomek'] Marek Ania
name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Zenek ['Tomek', 'Marek'] Ania

# sorted() - sortowanie, zwraca nową listę
print(sorted(tupla_imiona))
# ['Ania', 'Marek', 'Tomek', 'Zenek']

lista = list(tupla_imiona)
print(lista)  # ['Zenek', 'Tomek', 'Marek', 'Ania']
