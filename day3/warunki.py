# instrukcje warunkowe
# instrukce sterowania przepływem programu

# if
# w zaleznosci od warunku (True lub False) wykonuje jeden lub drugi blok programu
# wyrażenie zwraca bool

odp = True

if odp: print("test")
# test

if odp:
    # blok programu wykonany gdy warunek True
    print('test')
# test

# debugger - pozwala analizowac program linijka po linijce
# puapka - miejsca wstrzymania programu
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Ciag dalszy")

odp = "Radek"

if odp:
    print("Działa")
# Działa

if odp == "Radek":
    print("Jestem Radek")
else:
    print("To nie Radek")
# Jestem Radek

odp = "Tomek"
if odp == "Radek":
    print("Jestem Radek")
elif odp == "Tomek":
    print("Jestem Tomek")
else:
    print("Ani Radek ani Tomek")
