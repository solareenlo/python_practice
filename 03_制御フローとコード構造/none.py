"""This is a test program."""
is_empty: object = None
print(is_empty) # None と表示

if is_empty == None:
    print('None!') # None! と表示
if is_empty is None:
    print('None!') # None! と表示
if is_empty is not None:
    print('None!') # 何も表示されない

print(1 == True) # True と表示 objectとしてTrueかどうかを判定
print(1 is True) # False と表示 objectの中身が同じかどうかを判定
print(True == True) # True と表示
print(True is True) # True と表示
print(None == None) # True と表示
print(None is None) # True と表示

# 何が言いたい方というと, isやis notはNoneであるかどうかを判定する時によく使われるということ
# Noneとは空のobjectですよ. という意味
