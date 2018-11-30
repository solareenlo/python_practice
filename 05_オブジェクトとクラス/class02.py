class Person(object):
    def __init__(self, name): # 初期化を実行.  nameという引数をもらって,
        self.name = name # 自分自身のself.nameに代入

    def say_something(self): # selfをもらって,
        print("I'm {}. hello.".format(self.name)) # printする.
        self.run(3) # もちろん自分自身のメソッドも呼び出せる.

    def run(self, num):
        print('run' * num)

person = Person('sola')
person.say_something() # I'm sola. hello. runrunrun と表示される
