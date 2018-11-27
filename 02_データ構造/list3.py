"""This is a test program."""
r: list = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3)) # 3がどこのインデックスにあるか教えてくれる 出力は2
print(r.index(3, 4)) # 4のインデックスからスタートの, 3のインデックスを教えてくれる この場合の出力は7

print(r.count(3)) # 3の個数を数えてくれる

if 5 in r: # rの中に5がある場合,
    print('exit') # exitを出力してね

r.sort() # 昇順にrをソートしてくれる
print(r)

r.sort(reverse=True) # 逆順にrをソートしてくれる
print(r)

r.reverse() # 逆順にrをソートしてくれる
print(r)

s: str = 'My name is Mike.'
to_split: list = s.split(' ') # 文字列を空白で区切って, listに入れてくれる
print(to_split)

x: str = ' '.join(to_split) # listの区切りを空白に置き換えてから, 1つの文字列にしてくれる
print(x)
