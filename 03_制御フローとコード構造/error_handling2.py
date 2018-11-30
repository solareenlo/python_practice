"""This is a test program."""
class UppercaseError(Exception): # 自分で例外処理を作成できる. class名は独自のものにして, 誰が見ても分かり易いようにする.
    pass

def check():
    words = ['APPLE', 'orage', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word) # エラーの時にwordを返す. raiseを使って, 自分で例外処理に渡せる.

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next.') # エラーの時に表示.
    print(exc) # APPLE と表示. エラーの時に表示.
