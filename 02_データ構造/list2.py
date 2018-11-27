"""This is a test program."""
s: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)

s[0] = 'X' # 文字列の時はエラーになるが, listの時はできます
print(s)

s[2:5] = ['C', 'D', 'E'] # スライスを使って, 3番目から5番目までを一気に変えることもできる
print(s)

s[2:5] = [] # 3番目から5番目までを空にする
print(s)

s[:] = [] # sの中身全てが空になる
print(s)

n: list = [1, 2, 3]
n.append(4) # nの最後に4を追加
print(n)

n.insert(0, 10) # 1番初めに10を追加
print(n)

print(n.pop()) # 最後の要素を切り取り
print(n)
print(n.pop(0)) # 1番目の要素を切り取り
print(n)

del n[0] # 1番目の要素を削除
print(n)
del n # n自体を完全削除

n: list = [1, 2, 2, 2, 3]
n.remove(2) # nの中の1番目の2を削除
print(n)

a: list = [1, 2, 3]
b: list = [4, 5, 6]
x: list = a + b # aとbを結合したものをxに代入
print(x)

a += b # aの後ろのbを結合
print(a)

c: list = [7, 8, 9]
a.extend(c) # これもaの後ろにcを結合
print(a)
