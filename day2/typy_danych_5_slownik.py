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