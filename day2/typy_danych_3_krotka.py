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
