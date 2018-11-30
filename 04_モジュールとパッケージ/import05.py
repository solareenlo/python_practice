# importのエラー処理もtry, exceptで行う.
# バージョンごとにファイルが移動した時などに大変便利.
try:
    from package import utils02 # 古いバージョンの時にこちらを実行して欲しい時に用いる
except:
    from package.tools import utils02 # 新しいバージョンの時にこちらを実行して欲しい時に用いる

print(utils02.say_twice('hello!'))
