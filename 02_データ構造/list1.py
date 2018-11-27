"""This is a test program."""
l: list = [1, 2, 3, 4, 5, 6, 7]
print(l) # 配列lを表示
print(l[0]) # 1番目を表示
print(l[-1]) # 最後の要素を表示
print(l[-2]) # 最後から2番目を表示

print(l[0:2]) # 1番から2番目までを表示
print(l[:2]) # 1番から2番目までを表示
print(l[2:5]) # 3番から5番目までを表示
print(l[2:]) # 3番から最後までを表示
print(l[:]) # 1番から最後までを表示
print(len(l)) # 要素の個数を返す
print(type(l)) # 型を返す

print(list('abcdefg')) # 文字列abcdefgを配列['a', 'b', 'c', 'd', 'e', 'f', 'g']にしてくれる

print(l[::2]) # 2つ飛ばしで値を取ってきてくれる
print(l[::-1]) # 後ろから1つずつ値をとる

a: list = ['a', 'b', 'c']
n: list = [1, 2, 3]
x: list = [a, n] # 配列の入れ子もできる
print(x) # 出力は [['a', 'b', 'c'], [1, 2, 3]]
print(x[0]) # 出力は ['a', 'b', 'c']
print(x[0][1]) # 出力はb
