"""This is a test program."""
y: list = [1, 2, 3]
x: int = 1

if x in y: # yの中にxが入っているならば,
    print('in')

if 100 not in y: # yの中に100が入っていないならば,
    print('not in')

is_ok: bool = True
if not is_ok: # Trueでないならば, (ifはTrueなら通るので, helloはprintされない)
    print('hello')

# 以下のような使い方はあまりしない
a: int = 1
b: int = 2
if not a == b: # if a != b: とする
    print('a not equal b')
if not a < b: # if a >= b: とする
    print('a is bigger than b')
