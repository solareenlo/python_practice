""" This is a test program."""
import os
import string
import csv
import collections
import pathlib

import termcolor

ROBOT_NAME = 'Robobo'
ROBOT_COLOR = 'green'
FIELDNAMES = ['NAME', 'COUNT']

# 会話内容を納めたファイルへのファイルパスを設定
FILE_PASS = os.path.dirname(os.path.abspath(__file__))
FILE_PASS = os.path.join(FILE_PASS, 'robot')
FILE_PASS = os.path.join(FILE_PASS, 'templates')

# 初めの挨拶を表示
HELLO_FILE_PASS = os.path.join(FILE_PASS, 'hello.md')
with open(HELLO_FILE_PASS, 'r', encoding='utf-8') as template_file:
    CONTENTS = template_file.read()
    CONTENTS = CONTENTS.rstrip(os.linesep)
    CONTENTS = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
        contents=CONTENTS, splitter="=" * 64, sep=os.linesep)
    CONTENTS = termcolor.colored(CONTENTS, ROBOT_COLOR)
    CONTENTS = string.Template(CONTENTS)

# ユーザーの名前を取得
USER_NAME = input(CONTENTS.substitute({'robot_name': ROBOT_NAME}))

# どのレストランが好きか尋ねる
WHICH_FILE_PASS = os.path.join(FILE_PASS, 'which_restaurant.md')
with open(WHICH_FILE_PASS, 'r', encoding='utf-8') as template_file:
    CONTENTS = template_file.read()
    CONTENTS = CONTENTS.rstrip(os.linesep)
    CONTENTS = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
        contents=CONTENTS, splitter="=" * 64, sep=os.linesep)
    CONTENTS = termcolor.colored(CONTENTS, ROBOT_COLOR)
    CONTENTS = string.Template(CONTENTS)

# 好きなレストラン名を取得
RESTARANT = input(CONTENTS.substitute({'robot_name': ROBOT_NAME, 'user_name': USER_NAME}))

HANTEI = False
COUNTER = 0

# csvファイルのデータを格納する箱を用意
DATA = collections.defaultdict(int)

# ranking.csvが無い場合は作成する
if not os.path.exists('ranking.csv'):
    pathlib.Path('ranking.csv').touch()

# csvファイルを開く
with open('ranking.csv', 'r+') as csv_file:
    READER = csv.DictReader(csv_file)
    for row in READER:
        DATA[row['NAME']] = int(row['COUNT'])

# レストランの数を1つ増やす
DATA[RESTARANT.title()] += 1

# csvファイルに保存
with open('ranking.csv', 'w+') as csv_file:
    WRITER = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
    WRITER.writeheader()
    for name, count in DATA.items():
        WRITER.writerow({'NAME': name, 'COUNT': count})

# 最後の挨拶を表示
THANKS_FILE_PASS = os.path.join(FILE_PASS, 'thanks.md')
with open(THANKS_FILE_PASS, 'r', encoding='utf-8') as template_file:
    CONTENTS = template_file.read()
    CONTENTS = CONTENTS.rstrip(os.linesep)
    CONTENTS = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
        contents=CONTENTS, splitter="=" * 64, sep=os.linesep)
    CONTENTS = termcolor.colored(CONTENTS, ROBOT_COLOR)
    CONTENTS = string.Template(CONTENTS)
print(CONTENTS.substitute({'robot_name': ROBOT_NAME, 'user_name': USER_NAME}))
