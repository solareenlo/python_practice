# 書き方その1 (フルパスで読み込んでる)
# import package.utils01
# r = package.utils01.say_twice('hello')

# 書き方その2 (モジュールからインポートしてる)
# from package import utils01
# r = utils01.say_twice('hello')
from package import utils01 as u # asを使って, モジュールの名前を変えることもできる. けど, あまりオススメされていません.
r = u.say_twice('hello')

# 書き方その3 (これはオススメされてない. ここのものなのか, どこかのモジュールのものなのか分からなくなるため)
# from package.utils01 import say_twice
# r = say_twice('helo')

print(r)
