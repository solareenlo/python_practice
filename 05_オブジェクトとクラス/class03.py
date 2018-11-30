class Person(object):
    def __init__(self, name): # コンストラクタ
        self.name = name

    def __del__(self): # デストラクタ
        print('good bye')

person = Person('sola')

del person # personオブジェクトをデストラクタする. ので, ここでgood byeが表示される.

print('hey')
