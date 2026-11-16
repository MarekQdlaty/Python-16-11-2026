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

name = "Radek"
print(name)
# Radek
print(type(name))

# typowanie dynamiczne
age = 89
print(type(age))  # <class 'int'>
print(age)  # 89

age = "Radek"
print(type(age))  # <class 'int'>
print(age)  # Radek

# print(age + 1)  # TypeError: can only concatenate str (not "int") to str

# print(int(age) + 1) # ValueError: invalid literal for int() with base 10: 'Radek'
age = "89"
print(int(age) + 1)  # 90

# hint
name: str = "Radek"
name = 90

print(name)  # 90

# mypy, pyright, ruff
# pip - menadzer pakiety
#  pip install mypy
#  mypy .\day1\pierwszy.py
# (.venv) PS C:\Users\cscomarch\PycharmProjects\PythonProject\-16-11-2026> mypy .\day1\pierwszy.py
# day1\pierwszy.py:3: error: Cannot find implementation or library stub for module named "idlelib.colorizer"  [import-not-found]
# day1\pierwszy.py:3: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
# day1\pierwszy.py:68: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# day1\pierwszy.py:75: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# day1\pierwszy.py:79: error: Name "name" already defined on line 58  [no-redef]
# day1\pierwszy.py:80: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 5 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\cscomarch\PycharmProjects\PythonProject\-16-11-2026>
