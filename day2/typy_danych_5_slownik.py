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
