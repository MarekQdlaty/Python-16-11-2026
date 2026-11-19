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


odejmij(1, 2)
odejmij(1, 2, 3)
