"""This is a test program."""
def print_info(func):
    """decorete"""
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info # add_numをprint_infoでデコテートするということ
def add_num(a, b):
    """add two nums"""
    return a + b
R = add_num(10, 20)
print(R) # start end 30 と縦に表示

# 上記の5行と下記の5行は同じこと
# def add_num(a, b):
#     return a + b
# f = print_info(add_num)
# r = f(10, 20)
# print(r) # start end 30 と縦に表示

# デコレーターとは, 対象関数(ここではadd_num)に前後処理を付け加えたい時に使う
