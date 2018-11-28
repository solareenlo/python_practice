"""This is a test program."""
x: dict = {'a': 1}
y: dict = x # xからyへの参照渡し(xのアドレスをyに渡してる)になっている
y['a'] = 100
print(x, y) # {'a': 100} {'a': 100} と表示 なぜなら, y: dict = x が参照渡しになっているため

x: dict = {'a': 1}
y: dict = x.copy() # xの中身自体をyへ完コピしてる
y['a'] = 100
print(x, y) # {'a': 1} {'a': 100}
