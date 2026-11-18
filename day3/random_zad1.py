import random

# działania na liczbach losowych

# Return random integer in range [a, b], including both end points.
print(random.randint(1, 100))  # int od 1 do 100 włącznie

print(random.randrange(1, 100))  # od 1 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # 0.6030281207968737 od 0 do 0.999999
print(random.random() * 7)  # 2.5429644423743794 od 0 do 6.999999
