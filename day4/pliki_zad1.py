# działania z plikami
# filehandler

# context manager
# with - context manager w pythonie
# Character
# Meaning
# 'r'
# open for reading (default)
# 'w'
# open for writing, truncating the file first
# 'x'
# create a new file and open it for writing
# 'a'
# open for writing, appending to the end of the file if it exists
# 'b'
# binary mode
# 't'
# text mode (default)
# '+'
# open a disk file for updating (reading and writing)
with open("test.log", "w", encoding="utf-8") as file:
    file.write("Powitanie\n")
    file.write("Jeszcze jedno\n")

# file.write("")  # ValueError: I/O operation on closed file.

# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x", encoding="utf-8") as file:
#     file.write("Powitanie\n")
#     file.write("Jeszcze jedno\n")

with open("test.log", "w", encoding="utf-8") as file:
    file.write("Powitanie\n")
    file.write("Jeszcze wersja 2\n")

with open("test.log", "a", encoding="utf-8") as file:
    file.write("Dodane\n")
    file.write("Dośdane\n")

with open("test.log", "r", encoding="utf-8") as file:
    lines = file.read()

print(lines)
# Powitanie
# Jeszcze wersja 2
# Dodane

# chardet
