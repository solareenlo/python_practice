class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class TCar(Car):
    def rum(self):
        print('fast')

class SCar(Car):
    def __init__(self,
            model='Model X',
            enable_auto_run=False,
            passwd='123'):
        super().__init__(model)
        # self.enable_auto_run = enable_auto_run # 外部から読み書きできる
        self._enable_auto_run = enable_auto_run # @propertyを使って, 外部から読み込みはできるけど, 書き込みはできないようにする
        # self.__enable_auto_run = enable_auto_run # クラスの中からはアクセスできるけど外からはアクセスできない.
        self.passwd = passwd

    @property # propertyのgetter(読み込みの部分)
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter # 書き換えて良いということ.
    def enable_auto_run(self, is_enable):
        if self.passwd == '456': # パスワードが456であれば書き換えて良いということ.
            self._enable_auto_run = is_enable
        else: # 任意のエラー処理を書ける
            raise ValueError

    def run(self):
        print('very fast')

    def auto_run(self):
        print('auto run')

scar = SCar('Model X', passwd='456')
scar.enable_auto_run = True
print(scar._enable_auto_run) # True と表示
print(scar.model) # Model X と表示
