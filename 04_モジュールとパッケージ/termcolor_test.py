# pip install <第三者のPythonファイル名>
# pipを使うことで第三者のPythonファイルをインストールして使うことができます.
# https://pypi.python.org/pypiにたくさんあります.
# 今回はtermcolorを使います.

from termcolor import colored

print('test') # test と表示
print(colored('test', 'red')) # 赤色のtest が表示

print(help(colored)) # coloredのhelpが表示される
