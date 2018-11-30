"""This is a test program."""
animal = 'cat'

def f():
    """test func"""
    global animal
    print(animal) # cat と表示
    animal = 'dog'
    print(animal) # dog と表示
    print('locals: ', locals()) # locals: {} と表示
    print(f.__name__) # f と表示
    print(f.__doc__) # test func と表示

f()
print('global: ', animal) # global: dog と表示

print('global: ', globals()) # global:  {'__name__': '__main__', '__doc__': 'This is a test program.', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10d7a1198>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'namespace.py', '__cached__': None, 'animal': 'dog', 'f': <function f at 0x10d7381e0>} と表示
print(__name__) # __main__ と表示
print(__doc__) # This is a test program. と表示
