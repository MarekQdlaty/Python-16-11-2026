# snake_case
# PEP8
from idlelib.colorizer import prog_group_name_to_tag

print()  # wypisz/wydrukuj
print("Radek")
print('Radek')

# ctrl / - komentarz
# print('Radek")
#   File "C:\Users\cscomarch\PycharmProjects\PythonProject\-16-11-2026\day1\pierwszy.py", line 8
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 8)
#
# Process finished with exit code 1

# ctrl alt l - formatowanie kodu

print("Raadek")
print("Raadek")
print("Raadek")
print("Raadek")
print("Raadek")
print("Raadek")
print("Raadek")
print("Raadek")
print("Raadek")

# ctrl d - powielanie

# type() - sprawdzenie typu
print(type("Radek"))  # <class 'str'> dane tekstowe

print("38" + "90")  # konkatenacja,  łączenie, 3890

print("Radek" + "1")

print(38 + 90)  # 128
print(type(38))  # <class 'int'>, liczby całowite

import sys

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

# print("29" + 90)  # TypeError: can only concatenate str (not "int") to str

# rzutowanie
# int(), str()
print(int("39") + int(30))

print(168 * "39")

# zmienna - pudełko na dane
