import sys

wiek = 47  # int
rok = 2026  # int
temp = 36.6  # float
temp2 = 36, 6  # <class 'tuple'>, krotka
print(type(temp2))

print(wiek + rok)  # 2073
print(wiek - rok)  # -1979
print(wiek * rok)  # 95222
print(wiek / rok)  # 0.02319842053307009
print(wiek // rok)  # 0

print(rok / wiek)  # 43.1063829787234
print(rok // wiek)  # 43

print(rok % wiek)  # modulo - reszta z dzielenia
print(43 * wiek)  # 2021
print(rok - 201)

print(10 % 3)

print(wiek ** rok)

print(len(str(wiek ** rok)))  # 3388
# print(len(str(wiek ** rok ** 2)))  # 3388
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345

# decimal() - pozwala ominąć problem zaokrąglenia

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# typ logiczny
# prawda, fałsz
# True, False
# 1, 0

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, boolean

# na int
print(int(True))  # 1
print(int(False))  # 0

# bool()
print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True

print(bool("Radek"))  # True
print(bool(""))  # False

print(None)  # odpowiednik null, stan nieokreślony, nie wiem
print(bool(None))  # False

# operacja logiczne
print(49 * "-")

# and - i
print(True and True)
print(True and False)
# True
# False

print(49 * "-")
# or - lub
print(True or True)
print(True or False)
print(False or False)
# True
# True
# False

print(49 * "-")
# not - negacja
print(not True)  # False
print(not False)  # True

a = 6
b = 9

print(f"Porównanie {a} > {b} = {a > b}")
print(f"Porównanie {a} < {b} = {a < b}")
print(f"Porównanie {a} >= {b} = {a >= b}")
print(f"Porównanie {a} <= {b} = {a <= b}")
# Porównanie 6 > 9 = False
# Porównanie 6 < 9 = True
# Porównanie 6 >= 9 = False
# Porównanie 6 <= 9 = True
print(f"Porównanie {a <= b = }")  # Porównanie a <= b = True

# enable ligatures
print(f"Porównanie {a} == {b} = {a == b}")  # dwa znaki równa
print(f"Porównanie {a} != {b} = {a != b}")  # ! = różne
