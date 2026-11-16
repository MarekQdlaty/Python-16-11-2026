tekst = "Witaj Świecie"

print(tekst)
print(type(tekst))
# <class 'str'>

# teksty są niemutowalne
# Return a copy of the string converted to uppercase.
tekst.upper()
print(tekst)
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)

# lower, capitalize, title
print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie
print(tekst.title())  # Witaj Świecie

print(tekst)
print(len(tekst))  # 13 długosc

# Witaj świecie
# 0123456789... indeks, numerowane od zera

print(tekst[1])
print(tekst[3])
print(tekst[6])
# i
# a
# Ś

print(tekst[0])  # W

print(tekst.index("a"))  # index 3
print(tekst.count("e"))  # wystepuje 2 razy
print(tekst.index("e"))  # indeks 9, miejsce 10

print(tekst.lower().count("w"))  # występuje 2 razy

# Witaj świecie
# 0123456789...

print(tekst.count("j", 0, 4))  # wystepuje 0 razy, z prawej nie bierze pod uwagę
print(tekst.count("a", 3, 4))  # jeden raz

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "
