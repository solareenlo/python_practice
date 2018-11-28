"""This is a test program."""
i: list = [1, 2, 3]
j: list = i # iのアドレスがjに代入された(参照渡しになってる)

print('j = ', j) # [1, 2, 3]と出力される
print('i = ', i) # [1, 2, 3]と出力される

j[0] = 100 # 参照渡しになっているので, iの先頭にも100が入る

print('j = ', j) # [100, 2, 3]と出力される
print('i = ', i) # [100, 2, 3]と出力される



# なので, 別々のコピーを作るためには,
x: list = [1, 2, 3]
y: list = x.copy() # xの値をyにコピーしてる
# y: list = x[:] これでもyにxがコピーされる
y[0] = 100

print('x = ', x) # [1, 2, 3]と出力される
print('y = ', y) # [100, 2, 3]と出力される



a: int = 20
b: int = a # 数値は参照渡しでなく, 値渡し
b: int = 5
print(a, b) # 20 5と出力される
print(id(a), id(b)) # aとbのidは違う

a: list = ['a', 'b']
b: list = a
b[0] = 'c'
print(a, b) # ['c', 'b'] ['c', 'b']と出力される
print(id(a), id(b)) # aとbのidは同じ
