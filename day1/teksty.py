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
