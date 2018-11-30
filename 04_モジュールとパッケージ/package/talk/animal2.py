def sing():
    return 'Hey'
def cry():
    return 'wow'

if __name__ == '__main__': # 外部モジュールとしては以下の1行は渡っていかないということ.
    print(sing())
