class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class TCar(Car):
    def run(self):
        print('fast') # 親のメソッドを上書きした

class SCar(Car):
    def __init__(self, model='S', enable_auto_run=False): # 初期化も上書きした
        # self.model = model とするのは,冗長なので,
        super().__init__(model) # として, 親のやり方を呼んでくる.
        self.enable_auto_run = enable_auto_run
    def rum(self):
        print('super fast') # 親のメソッドを上書きした

car = Car()
tcar = TCar('TLexus')
scar = SCar('Model X')

print(tcar.model) # TLexus と表示
print(scar.model) # Model X と表示
