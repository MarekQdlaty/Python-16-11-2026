# napisac funkcję obliczającą średnią ocen
# ma działacz  dowolną liczba ocen
# ma obsłużyc błędy
# dodać imię ucznia
import statistics


def srednia(*cyfry):  # * dowolna ilosć arg pozycyjnych
    print(cyfry)  # (1, 2, 3)

    count = len(cyfry)
    suma = 0
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Błąd:", e)
    else:  # gdy nie ma błedu
        print(avg)
        print(avg_p)
        print(statistics.mean(cyfry))
    finally:
        print("Następny uczzen")


srednia()
srednia(1, 2)
srednia(1, 2, 3)


def srednia2(*cyfry):
    if cyfry:
        print(statistics.mean(cyfry))


srednia2()
srednia2(1, 2)
srednia2(1, 2, 3)
