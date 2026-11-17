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

# f-string
print(f"Witaj {user}, masz {wiek} lat.")  # Witaj Tomek, masz 51 lat.

# %i - int, %f - float
print("Używam wersji Pythona %i" % 3)  # żywam wersji Pythona 3
print("Używam wersji Pythona %f" % 3)  # Używam wersji Pythona 3.000000
print("Używam wersji Pythona %.2f" % 3.9)  # Używam wersji Pythona 3.90
print("Używam wersji Pythona %.1f" % 3.9)  # Używam wersji Pythona 3.9
print("Używam wersji Pythona %.0f" % 3.9)  # Używam wersji Pythona 4 zaokrągla
print("Używam wersji Pythona %.f" % 3.9)  # Używam wersji Pythona 4

x = 3.8769
print(f"%.2f" % x)  # 3.88
print(x)  # 3.8769

y = round(x, 2)
print(y)  # 3.88


