"""This is a test program."""
def g():
    for i in range(10):
        yield i
g = g()
print(next(g)) # 0 と表示
print(next(g)) # 1 と表示
print(next(g)) # 2 と表示

# generatorの内包表記の書き方
g = (i for i in range(10))
print(next(g)) # 0 と表示
print(next(g)) # 1 と表示
print(next(g)) # 2 と表示
for i in g:
    print(i) # 3 4 5 6 7 8 9 と表示
