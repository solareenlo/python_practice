class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self): # クラスが呼び出されると, 文字列を返す特殊メソッド
        return 'Word!!!'

    def __len__(self): # クラスへ渡された引数の長さを返す
        return len(self.text)

    def __add__(self, word): # 文字列を足し合わせる
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
ww = Word('testtest')
print(w) # World!!!と表示
print(len(w)) # 4 と表示
print(w + ww) # testtesttest と表示
print(w == ww) # False と表示

"""
色々な特殊メソッドがあります.
__eq__( self, other ) self == other
__ne__( self, other ) self != other
__lt__( self, other ) self < other
__gt__( self, other ) self > other
__le__( self, other ) self <= other
__ge__( self, other ) self >= other

__add__( self, other ) self + other
__sub__( self, other ) self - other
__mul__( self, other ) self * other
__floordiv__( self, other) self // other
__truediv__( self, other ) self / other
__mod__( self, other ) self % other
__pow__( self, other ) self ** other

__str__( self, other ) str( self )
__len__( self, other ) len( self )
"""
