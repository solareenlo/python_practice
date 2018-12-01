# classの中身を書き換えるときは__xxxを上書きしてないかどうか気をつける
class Car(object):
    def __init__(self,
            model='XXX',
            enable_auto_run=False,
            passwd='123'):
        self.model = model
        self.__enable_auto_run = enable_auto_run
        self.passwd = '456'

class T(object):
    pass

t = T()
t.name = 'Taro'
t.age = 20
print(t.name, t.age) # Taro 20 と表示

car = Car()
print(car.model) # XXX と表示
# print(car.__enable_auto_run) # これはエラーになるが,
car.__enable_auto_run = True
print(car.__enable_auto_run) # これはTrueになっちゃう.
