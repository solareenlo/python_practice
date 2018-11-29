"""This is a test program."""
def menu(**kwargs):
    """**付けると複数のkeyとvalueを辞書化してくれる"""
    print(kwargs)

menu(entree='beef', drink='coffee') # {'entree': 'beef', 'drink': 'coffee'} と表示

d: dict = {
    'entree': 'beef',
    'drink': 'coffee',
    'dessert': 'ice'
    }
# **dはd内を展開して関数に持って行ってくれる
menu(**d) # {'entree': 'beef', 'drink': 'coffee', 'dessert': 'ice'} と表示
