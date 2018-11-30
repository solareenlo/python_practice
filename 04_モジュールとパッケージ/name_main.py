import package.talk.animal2

# 以下の4行が通常の書き方
# こうすることで, このファイルがモジュールとして他のファイルから呼び出された時に,
# ここだけで実行したいことと, 渡したいものに分けておける.
def main():
    print(package.talk.animal2.sing())

if __name__ == '__main__': # __name__が__main__ということは, このファイルが直接実行さてたということ. つまり, 外部モジュールとして渡っていかないということ.
    main()
