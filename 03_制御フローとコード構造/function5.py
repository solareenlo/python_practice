"""This is a test program."""

def say_something(*args):
    """*argsが引数をまとめてtupleに格納してくれる"""
    print(args) # ('Hi!', 'Mike', 'Nance') と表示
    for arg in args:
        print(arg) # Hi! Mike Nance と縦に表示

say_something('Hi!', 'Mike', 'Nance')



def say_something2(word, *args):
    """もちろん, デフォルト引数と組み合わせて*argsも使えます"""
    print(word) # Hi! と表示
    for arg in args:
        print(arg) # Mike Nance と縦に表示

say_something2('Hi!', 'Mike', 'Nance')
