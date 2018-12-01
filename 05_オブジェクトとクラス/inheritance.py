class Person(object):
    def talk(self):
        print('talk')
    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

class PersonCarRobot(Car, Person): # 多重継承するときは, (Car, Person)のように書く
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.fly() # fly と表示
person_car_robot.run() # car run と表示 クラスを多重継承したもののうち, 左にある方のクラスのメソッドを先に継承するので. runメソッドは2つありますが.
person_car_robot.talk() # talk と表示
