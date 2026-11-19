# funkcja lambda
# skrócony zapis funkcji
# konczy sie return
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(5, 90))  # -85

odejmij2 = lambda a, b: a - b
print(odejmij2(6, 90))  # -84

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

#
lista = [1, 2, 14, 24, 50, 67, 80, 100, 200, 500]
# *2
