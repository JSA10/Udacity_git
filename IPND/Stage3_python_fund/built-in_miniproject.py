#built-in Python mini-project

# experimenting with abs and map

# abs() = returns absolute value of any number
# map(function, iterable, ...) = applies a function to an iterable object (e.g. list)

messy = (-1, 3, -7, 9.7, 20, -44, -22, -0.70)

def clean(some_vector):
    c = map(abs, some_vector)
    print(c)

clean(messy)

