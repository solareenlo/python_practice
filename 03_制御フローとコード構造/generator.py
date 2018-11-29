"""This is a test program."""
l = ['Good moring', 'Good afternoon', 'Good night']

for i in l:
    print(i) # Good morning Good afternoon Good night と縦に表示

print('###############')

def greeting():
    yield 'Good moring'
    print('somethin3')
    yield 'Good afternoon'
    yield 'Good night'

def counter(num=10):
    for _ in range(num):
        yield 'run'

g = greeting()
r = counter()
print(next(g)) # Good morning と表示
print(next(r)) # run と表示
print(next(r)) # run と表示
print(next(r)) # run と表示
print(next(g)) # Good afternoon と表示
print(next(r)) # run と表示
print(next(r)) # run と表示
print(next(g)) # Good night と表示

# for文は一度にイテレートするが, generatorは順番に処理を実行できる
