""" 引数にいろんなparser(構文解析をするプログラム)をするよ """
from optparse import OptionParser
from optparse import OptionGroup # 別のカテゴリーのオプションをつけたい時に用いる

def main():
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='File name') # ファイルをparserしたい時
    parser.add_option('-n', '--num', action='store', type='int',
                      dest='num') # 数をparserしたい時

    parser.set_defaults(verbose=True) # -vと-qを入力しないとverboseはTrueになる. ということ.
    parser.add_option('-v', action='store_true', dest='verbose') # -vが入力されるとverboseはTrueになる.ということ.
    parser.add_option('-q', action='store_false', dest='verbose') # -qが入力されるとverboseはFalseになる.ということ.

    parser.add_option('-r', action='store_const', const='root',
                      dest='user_name') # -rが入力されるとuser_nameがrootになるということ.

    parser.add_option('-e', dest='env') # -e test と入力すると, 'env': 'test'となる.
    def is_release(option, opt_str, value, parser):
        if parser.values.env == 'prd':
            raise parser.error("Can't release")
        setattr(parser.values, option.dest, True) # ここでは'release': Trueにするということ
    parser.add_option('--release', action='callback',
                      callback=is_release, dest='release') # コールバック関数も設定できる.
    # --release -e prd となると, raiseで設定したエラーが返ってくる.

    group = OptionGroup(parser, 'Secound Options')
    group.add_option('-g', action='store_true', help='Group option')
    parser.add_option_group(group) # これで--helpした時に, 上とは違うGroupでhelpが出現する.

    options, args = parser.parse_args()
    print(options)
    print(options.filename)
    print(args)

if __name__ == '__main__':
    main()
