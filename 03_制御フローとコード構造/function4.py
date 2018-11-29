"""This is a test program."""
def test_func(x, l=None):
    """
        l=Noneの所に, l=[]とすると,
        l=[]のlは, 参照渡しになっているので,
        2回目にl=[]を使った時に,
        lが初期化されずにバグの原因になるので,
        Pythonでは, 関数のデフォルト引数として,
        空の文字列や整数を渡すのは良いが,
        空のlistやdictionaryを渡すのはご法度.
        よって, 以下のif文を用いて初期化する.
    """
    if l is None:
        l = []
    l.append(x)
    return l

r: int = test_func(100)
print(r) # [100] と表示
r: int = test_func(100)
print(r) # [100] と表示



def test2_func(x, l=[]):
    """l=[]は2回目に呼び出された時に初期化されていないので注意!"""
    l.append(x)
    return l

r: int = test2_func(100)
print(r) # [100] と表示
r: int = test2_func(100)
print(r) # [100, 100] と表示
