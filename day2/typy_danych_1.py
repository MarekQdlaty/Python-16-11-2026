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
