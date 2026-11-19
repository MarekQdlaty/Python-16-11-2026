a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


print(f"Zmienna z góry (globalna) {a}")  # Zmienna z góry (globalna) 10
dodaj()  # 15
print(f"Zmienna z góry (globalna) {a}")  # Zmienna z góry (globalna) 10
dodaj2()  # 20
print(f"Zmienna z góry (globalna) {a}")  # Zmienna z góry (globalna) 10
