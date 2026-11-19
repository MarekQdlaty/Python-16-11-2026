# argumenty po nazwie, keywords

def connect(**opcje):
    print(opcje)  # {'a': 10}
    name = opcje.get('name')
    if name:
        print(name)


connect(a=10)
connect(a=10, name="Radek")  # Radek


# {'a': 10}
# {'a': 10, 'name': 'Radek'}
# Radek

def all_args(*args, **kwargs):
    print(args, kwargs)
