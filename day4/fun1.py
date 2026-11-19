# funkcja - wydzielony fragment kodu, można wywołać w dowolnym momencie
# funkcja musi najpierw zadeklarowana
# urchomienie funkcji poprzez jej wywołania

a = 6
b = 8


# deklaracja funkcji
def dodaj():
    print(a + b)


# wywołanie funkcji
dodaj()  # 14


def dodaj2(a, b):  # obowiazkowe
    print(a + b)


# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 90)  # 95


# ominiecie problemu braku przeciążanie
def odejmij(a, b, c=0):
    print(a - b - c)


# po  pozycji
odejmij(1, 2)
odejmij(1, 2, 3)

# po nazwie
odejmij(c=9, b=90, a=89)  # -10

# mieszany
odejmij(1, 2, c=90)  # -91

# odejmij(b=1, 1, 2)  # SyntaxError: positional argument follows keyword argument

# print(dodaj() + dodaj())
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
