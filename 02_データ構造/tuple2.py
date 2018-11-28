"""This is a test program."""
num_tuple: tuple = (10, 20)
x, y = num_tuple # これをtupleのunpackingという
print(x, y) # 10 20 と出力

x, y = (10, 20)
print(x, y) # 10 20 と出力

x, y = 10, 20
print(x, y) # 10 20 と出力

i = 10
j = 20
tmp: int = i
i = j
j = tmp
print(i, j) # 20 10 と出力

a: int = 100
b: int = 200
a, b = b, a # tupleを使うと数値の入れ替えも簡単に行える
print(a, b) # 200 100 と出力
