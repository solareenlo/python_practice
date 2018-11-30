# classの定義の仕方
# class Person: と書くのはPython3の書き方
class Person(object):
    def say_something(self):
        print('hello')

person: object = Person()
person.say_something()
