import abc # 抽象クラスを使うための標準ライブラリ

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age
    @abc.abstractmethod # 必ず以下のmethodは子クラスで実装してくださいね, という意味
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        raise Exception('No drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self): # Personクラスの抽象クラスでdriveを定義しているので, ここが無いとエラーになる
        print('ok')

baby = Baby()
# baby.drive() # Exception: No drive とエラーになる
adult = Adult()
adult.drive() # ok と表示
