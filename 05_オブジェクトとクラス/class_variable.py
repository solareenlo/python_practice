# クラス変数は全てのオブジェクトで共有されるので気を付けて
class Person(object):
    kind = 'human' # 全てのobjectで共有される
    def __init__(self, name):
        self.name = name
    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you() # A human と表示
b = Person('B')
b.who_are_you() # B human と表示



class T(object):
    words = []
    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words) # ['add 1', 'add 2'] と表示

d = T()
d.add_word('add 3')
d.add_word('add 4')
print(d.words) # ['add 1', 'add 2', 'add 3', 'add 4'] と表示

# c と d それぞれに文字列を格納したい場合は,
class T2(object):
    def __init__(self): # ここで初期化してあげる.
        self.words = []
    def add_word(self, word):
        self.words.append(word)

c = T2()
c.add_word('add 1')
c.add_word('add 2')
print(c.words) # ['add 1', 'add 2'] と表示

d = T2()
d.add_word('add 3')
d.add_word('add 4')
print(d.words) # ['add 3', 'add 4'] と表示
