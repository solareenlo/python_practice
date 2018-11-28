"""This is a test program."""
# True は, 空で無いと全部Trueになる
# False, 0, 0.0, '', [], (), {}, set()　全部False
is_ok: list = [1, 2, 3]

if is_ok:
    print('OK!') # is_ok がTrueだとこっちを出力
else:
    print('No!') # is_ok がFalseだとこっちを出力
