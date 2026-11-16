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

# strip() - usunięcie białych znaków, usuwa spacje z przodu i z tyłu
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode("utf-8")
print(encode_s)
# b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'>
# \xc5\x9a kod Ś w uicode
# \x dane w postaci szesnastkowej

print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
print(len(imie))  # dugosc 5

# "Mam na imię ... ."
print("Mam na imię " + str(imie) + ".")  # Mam na imię Radek.

print("Mam na imię", imie, "\b.")  # Mam na imię Radek.
# \b - backspace

# f-string - wstrzyknięcie zawaertości zmiennej do tekstu
tekst_format = f"Mam na imię {imie}."
print(tekst_format)  # Mam na imię Radek.

tekst_format = f"\tMam na imię {imie}.\n Lubię Pythona.\b"
print(tekst_format)
# "	 Mam na imię Radek.
#  Lubię Pythona"
# \t tab
# \n - nowa linia
# \b - backspace

print(f"""
    Mam na imię {imie}
i lubię Pythona
""")
# "    Mam na imię Radek
# i lubię Pythona"

#
"""
Komentarz
    wielolinikowy - dokumentacja
    """

print(print.__doc__)
#
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.

print("Imie:", imie)  # Imie: Radek
print("Imie:", imie, sep="_ _")  # Imie:_ _Radek

print("Radek", end="-")
print("Tomek")  # Radek-Tomek
print("Kolejna linia")
# Radek-Tomek
# Kolejna linia

starszy = "Witaj %s"  # %s - str
print(starszy % imie)  # Witaj Radek

# zabraniam używać
print("Witaj {}".format("Radek"))
