"""This is a test program."""
# 位置引数の例.
def menu(entree, drink, dessert):
    print('entree = ', entree) # entree = rice と表示
    print('drink = ', drink) # drink = milk と表示
    print('dessert = ', dessert) # dessert = ice と表示
menu('rice', 'milk', 'ice')

# キーワード引数の例
def menu2(entree, drink, dessert):
    print(entree) # rice と表示
    print(drink) # milk と表示
    print(dessert) # ice と表示
menu2(dessert='ice', drink='milk', entree='rice')

# デフォルト引数の例
def menu3(entree='beef', drink='milk', dessert='ice'):
    print(entree) # beef と表示
    print(drink) # milk と表示
    print(dessert) # ice と表示
menu3()

# 位置引数, キーワード引数, デフォルト引数をそれぞれ混ぜて使うことももちろんできます.
