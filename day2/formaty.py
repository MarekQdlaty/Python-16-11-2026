user = "Tomek"  # str
wiek = 51  # int
liczba = 908897654345321  # int

wersja = 3.9001
print(type(wersja))  # <class 'float'> zmiennoprzecinkowe

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 51 lat.
# %s - str
# %d - digit

# TypeError: %d format: a real number is required, not str
# print("Witaj %d, masz teraz %s lat." % (user, wiek))

