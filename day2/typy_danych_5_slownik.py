# słownik para {klucz : wartosc}
# {'user' : 'Radek'}
# klucze nie mogą się powtarzac
# słownik jest odpowiednikiem jsona w pythonie

# pusty słownik
dictionary = {}
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

dict_1 = dict()
print(dict_1)  # {}
print(type(dict_1))  # <class 'dict'>

# dodawanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)
# {'imie': 'Radek'}

# klucz wiek
dictionary['wiek'] = 41
print(dictionary)  # {'imie': 'Radek', 'wiek': 41}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 41])
# dict_items([('imie', 'Radek'), ('wiek', 41)])

# nadpisanie
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 41}

dictionary['imie'] = ['Radek', "Tomek", "Anna"]
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Anna'], 'wiek': 41}

# Tomek
print(dictionary['imie'])  # ['Radek', 'Tomek', 'Anna']
print(dictionary['imie'][1])  # Tomek

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary['Imie'.lower()])  # ['Radek', 'Tomek', 'Anna']

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

print(chr(223))  # ß
# \uhh - kod szesnastkowy unicode
print("s\u00DFa")  # sßa
# \N{name}
print("\N{LATIN SMALL LETTER SHARP S}")  # ß

name1 = "GROSS"
name2 = "groß"

print(name1 == name2)
print(name1.lower() == name2.lower())  # False
# Return a version of the string suitable for caseless comparisons.
print(name1.casefold() == name2.casefold())  # True
