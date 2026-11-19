# {
#   "name": "John",
#   "age": 30,
#   "city": null
# }
# json - dane typy klucz wartosc
# wymiana danych pomiedzy klient serwer
# odpowiednikiem jsona w pythonie jest słownik
# zawsze podwójne słownik

# orjson
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(person_dict)
print(type(person_dict))  # <class 'dict'>

# zapis do pliku
with open("nasze_dane.json", "w") as f:
    json.dump(person_dict, f)
