dictionary = {"imie": "Radek", 'nazwisko': "Kowalski"}

# klucz, wartośc, para

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)

# imie
# nazwisko

# wartości
for i in dictionary.values():
    print(i)
# Radek
# Kowalski

# pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "<=>", v)

# imie <=> Radek
# nazwisko <=> Kowalski
