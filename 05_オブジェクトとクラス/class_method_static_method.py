class Person(object):
    sex = 'female'
    def __init__(self):
        self.x = 100

    @classmethod # クラスのメソッドとして存在するので, オブジェクトが生成されてなくても呼び出せる.
    def what_is_your_sex(cls):
        return cls.sex

    @staticmethod # 静的メソッド(いつでも呼び出せる). クラスの外側にあっても良いけど, このクラスに関わりがあるので, こんな書き方もできる程度に覚えておこう.
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a.what_is_your_sex()) # female と表示 (オブジェクトのfemale)

print(Person.sex) # female と表示 (クラス変数のfemale)
print(Person.what_is_your_sex()) # female と表示 (クラスメソッドのfemale)

Person.about('2000') # about human 2000
