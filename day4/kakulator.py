# napisac aplikację kalkulator
# while True
# menu z opcjami
# wyświetlić łądnie wynik 5 * 8 = 40
# obsłużyc wyjatki


while True:
    print(f"""
1. Dodawanie
5. Koniec""")

    odp = input("Podaj opcję z menu: ")

    if odp == '5':
        break
    try:
        a = float(input("podaj liczbę a: "))
        b = float(input("podaj liczbę b: "))

        if odp == "1":
            print(f"Dodawanie {a} + {b} = {a + b}")
        else:
            print("Błedna operacja!")
    except ZeroDivisionError:
        print("Dzielenie przez zero")
    except Exception as e:
        print("Błąd:", e)
    finally:
        print("Obliczenia wykonane")

# 1. Dodawanie
# 5. Koniec
# Podaj opcję z menu: 1
# podaj liczbę a: 6
# podaj liczbę b: 9
# Dodawanie 6.0 + 9.0 = 15.0
# Obliczenia wykonane
#
# 1. Dodawanie
# 5. Koniec
# Podaj opcję z menu:
