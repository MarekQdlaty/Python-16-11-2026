def all_params(a, b, /, c=42, d=345):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_params(10, 10)
# a=10, b=10
# c=42, d=345

all_params(1, 2, 3)
all_params(1, 2, 3, 4)
all_params(1, 2, 3, d=4)
all_params(1, 2, c=3, d=4)

# / oddziela argumenty pozycyjne
# TypeError: all_params()
# got some positional-only arguments passed as keyword arguments: 'a, b'
# all_params(a=1, b=2, c=3, d=4)
