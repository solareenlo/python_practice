"""This is a test program."""
t: tuple = (1, 2, 3, 1, 2, 3)
print(t)
# t[0] = 100 これは使えない
print(t[0], t[-1], t[2:5]) # これらは使える
print(t.index(1), t.index(1, 1)) # これらも使える
print(t.count(1)) # これも使える
# 何が言いたいかというと, tupleは読み込み専用として使えるということ
# データの中身を変えて欲しくない時に使います

t: tuple = ([1, 2, 3], [4, 5, 6]) # tupleの中にlistは入れられる
t[0][0] = 100 # tupleの中のlistの中身は変更可
print(t) # ([100, 2, 3], [4, 5, 6])と出力

t = 1, 2, 3 # 型を指定せずに左のように書くと1, 2, 3は(1, 2, 3)と認識されてtupleとしてtに入る
print(t) # (1, 2, 3)と出力
t = 1,
print(t) # (1,)と出力
t = 1
print(t) # 1と出力

t = () # tupleとして登録される
t = (1) # intとして登録される
t = ('1') # strとして登録される
t = ('1',) # tupleとして登録される

new_tuple: tuple = (1, 2, 3) + (4, 5, 6) # 1番初めに足すことはできる
print(new_tuple)
# new_tuple: tuple = (1) + (4, 5, 6) これはできない, なぜなら(1)がintだから
# new_tupel: tuple = (1,) + (4, 5, 6) これはできる, なぜなら(1,)がtupleだから
