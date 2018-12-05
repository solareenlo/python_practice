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

def read_csv(dir_pass, file_name, color=None):
    """ ファイルを読み込み """
    file_pass = os.path.join(dir_pass, file_name)
    with open(file_pass, 'r', encoding='utf-8') as template:
        contents = template.read()
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter="=" * 64, sep=os.linesep)
        contents = termcolor.colored(contents, color)
        return string.Template(contents)

# 初めの挨拶を表示して, ユーザー名を取得
TEMPLATE = read_csv(FILE_PASS, 'hello.md', ROBOT_COLOR)
USER_NAME = input(TEMPLATE.substitute({'robot_name': ROBOT_NAME}))

# csvファイルのデータを格納する箱を用意
DATA = collections.defaultdict(int)

# ranking.csvが無い場合は作成する
if not os.path.exists(CSV):
    pathlib.Path(CSV).touch()

# csvファイルを開いて, csvデータを配列に格納
with open(CSV, 'r+') as csv_file:
    READER = csv.DictReader(csv_file)
    for row in READER:
        DATA[row[NAME]] = int(row[COUNT])

if DATA:
    SORTED_DATA = sorted(DATA, key=DATA.get, reverse=True)
    NEW_RECOMMEND_RESTAURANT = SORTED_DATA[0]
    while True:
        TEMPLATE = read_csv(FILE_PASS, 'greeting.md', ROBOT_COLOR)
        IS_YES = input(TEMPLATE.substitute({
            'robot_name': ROBOT_NAME,
            'user_name': USER_NAME,
            'restaurant': NEW_RECOMMEND_RESTAURANT}))
        if IS_YES.lower() == 'y' or IS_YES.lower() == 'yes':
            break
        if IS_YES.lower() == 'n' or IS_YES.lower() == 'no':
            SORTED_DATA.remove(NEW_RECOMMEND_RESTAURANT)
            print(SORTED_DATA)
            if not SORTED_DATA:
                break
            NEW_RECOMMEND_RESTAURANT = SORTED_DATA[0]

# どのレストランが好きか尋ねて, テストラン名を保存
TEMPLATE = read_csv(FILE_PASS, 'which_restaurant.md', ROBOT_COLOR)
RESTARANT = input(TEMPLATE.substitute({'robot_name': ROBOT_NAME, 'user_name': USER_NAME}))

# レストランの数を1つ増やす
DATA[RESTARANT.title()] += 1

# csvファイルに保存
with open(CSV, 'w+') as csv_file:
    WRITER = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
    WRITER.writeheader()
    for name, count in DATA.items():
        WRITER.writerow({NAME: name, COUNT: count})

# 最後の挨拶を表示
TEMPLATE = read_csv(FILE_PASS, 'thanks.md', ROBOT_COLOR)
print(TEMPLATE.substitute({'robot_name': ROBOT_NAME, 'user_name': USER_NAME}))
