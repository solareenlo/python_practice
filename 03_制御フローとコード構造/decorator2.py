"""This is a test program."""
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# decoratorを重ねる時は, 上が下を包み込みます
@print_info
@print_more
def add_num(a, b):
    return a + b
r = add_num(10, 20)
print(r)
# 上記の6行は下記の3行と同じこと
# f = print_info(print_more(add_num))
# r = f(10, 20)
# print(r)
