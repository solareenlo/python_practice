class Car(object):
    def run(self):
        print('run')

class ACar(Car):
    pass # 何もしないという意味

class BCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run() # run と表示

a_car = ACar()
a_car.run() # run と表示

b_car = BCar()
b_car.run() # run と表示
b_car.auto_run() # auto run と表示
