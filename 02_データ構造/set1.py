"""This is a test program."""
a: set = {1, 2, 2, 2, 3, 2, 4, 4, 3, 4, 5}
print(a) # {1, 2, 3, 4, 5} と表示

b: set = {2, 3, 3, 6}
print(b)

print(a - b) # {1, 4, 5} と表示
print(b - a) # {6} と表示
print(a & b) # {2, 3} と表示
print(a | b) # {1, 2, 3, 4, 5, 6} と表示
print(a ^ b) # {1, 4, 5, 6} と表示
