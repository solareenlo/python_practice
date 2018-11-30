"""This is a test program."""
l: list = [1, 2, 3]
i = 5

# del l # NameError を出すためにあります.

try:
    print(l[i])
except IndexError as ex: # indexが範囲外の時に表示
    print("Don't worry: {}".format(ex))
except NameError as ex: # そんなのありませんというときに表示
    print(ex)
except Exception as ex: # これは全般的なエラーに使えるが, これは使わないようにする. きちんとエラー処理をするようにする.
    print('other:{}'.format(ex))
else:
    print('done') # きちんと処理が終わった時に表示される.
finally:
    print('clean up') # エラーでもエラーじゃなくても表示される. エラーはclean up が表示されてから表示される.

print('done') # これはあまり使わない.
