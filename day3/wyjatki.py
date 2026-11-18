# wyjątki - błędy wykonywania programu

# print(5 / 0)

# Traceback (most recent call last):
#   File "C:\Users\cscomarch\PycharmProjects\PythonProject\-16-11-2026\day3\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1

try:
    # print(5 / 0)
    # print("Ania" + 2)
    # int("Q")
    # raise KeyError("Błąd klucza")  # rzucenie wyjątku
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Błąd:", e)
else:  # gdy nie ma błedu
    print(wynik)
finally:  # wykona sie zawsze
    print("Kolejny wiersz")
print("Dalsza część...")

# 30.0
# Kolejny wiersz
# Dalsza część...