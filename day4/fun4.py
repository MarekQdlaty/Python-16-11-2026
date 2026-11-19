# napisac funkcję obliczającą średnią ocen
# ma działacz  dowolną liczba ocen
# ma obsłużyc błędy
# dodać imię ucznia

def srednia(*cyfry):  # * dowolna ilosć arg pozycyjnych
    print(cyfry)  # (1, 2, 3)

    count = len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Błąd:", e)
    else:  # gdy nie ma błedu
        print(avg)
    finally:
        print("Następny uczzen")


srednia()
srednia(1, 2)
srednia(1, 2, 3)
