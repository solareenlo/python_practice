""" This is a test program."""
import os
import string
import csv
import collections
import pathlib

import termcolor

ROBOT_NAME = 'Robobo'
ROBOT_COLOR = 'green'
CSV = 'ranking.csv'
NAME = 'Restaurant Name'
COUNT = 'Count'
FIELDNAMES = [NAME, COUNT]

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

# csvファイルのデータを格納する箱を用意
DATA = collections.defaultdict(int)

# ranking.csvが無い場合は作成する
if not os.path.exists(CSV):
    pathlib.Path(CSV).touch()

# csvファイルを開く
with open(CSV, 'r+') as csv_file:
    READER = csv.DictReader(csv_file)
    for row in READER:
        DATA[row[NAME]] = int(row[COUNT])

# オススメのレストランを尋ねる
# SORTED_DATA = sorted(DATA, key=DATA.get, reverse=True)
# print(SORTED_DATA[0])
if DATA:
    while True:
        RECOMMEND_RESTAURANT_FILE_PASS = os.path.join(FILE_PASS, 'greeting.md')
        SORTED_DATA = sorted(DATA, key=DATA.get, reverse=True)
        NEW_RECOMMEND_RESTAURANT = SORTED_DATA[0]
        with open(RECOMMEND_RESTAURANT_FILE_PASS, 'r', encoding='utf-8') as template_file:
            CONTENTS = template_file.read()
            CONTENTS = CONTENTS.rstrip(os.linesep)
            CONTENTS = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
                contents=CONTENTS, splitter="=" * 64, sep=os.linesep)
            CONTENTS = termcolor.colored(CONTENTS, ROBOT_COLOR)
            CONTENTS = string.Template(CONTENTS)
        IS_YES = input(CONTENTS.substitute({
            'robot_name': ROBOT_NAME,
            'user_name': USER_NAME,
            'restaurant': NEW_RECOMMEND_RESTAURANT}))
        if IS_YES.lower() == 'y' or IS_YES.lower() == 'yes':
            break
        if IS_YES.lower() == 'n' or IS_YES.lower() == 'no':
            break

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

# レストランの数を1つ増やす
DATA[RESTARANT.title()] += 1

# csvファイルに保存
with open(CSV, 'w+') as csv_file:
    WRITER = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
    WRITER.writeheader()
    for name, count in DATA.items():
        WRITER.writerow({NAME: name, COUNT: count})

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
