""" This is a test program."""
import os
import string
import csv

import termcolor

ROBOT_NAME = 'Robobo'

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
    CONTENTS = termcolor.colored(CONTENTS, 'green')
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
    CONTENTS = termcolor.colored(CONTENTS, 'green')
    CONTENTS = string.Template(CONTENTS)

# 好きなレストラン名を取得
RESTARANT = input(CONTENTS.substitute({'robot_name': ROBOT_NAME, 'user_name': USER_NAME}))

HANTEI = False
COUNTER = 0

# レストラン名をcsvに格納(まだ実装途中)
if os.path.exists('ranking.csv') is False:
    with open('ranking.csv', 'w') as csv_file:
        FIELDNAMES = ['NAME', 'COUNT']
        WRITER = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        WRITER.writeheader()
        WRITER.writerow({'NAME': RESTARANT, 'COUNT': 1})
else:
    with open('ranking.csv', 'r') as csv_file:
        READER = csv.DictReader(csv_file)
        for row in READER:
            if row['NAME'] == RESTARANT:
                COUNTER = int(row['COUNT'])
                COUNTER += 1
                print(COUNTER)
                row['COUNT'] = COUNTER
                HANTEI = True
    if HANTEI is False:
        with open('ranking.csv', 'a') as csv_file:
            FIELDNAMES = ['NAME', 'COUNT']
            WRITER = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
            WRITER = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
            WRITER.writerow({'NAME': RESTARANT, 'COUNT': 1})

# 最後の挨拶を表示
THANKS_FILE_PASS = os.path.join(FILE_PASS, 'thanks.md')
with open(THANKS_FILE_PASS, 'r', encoding='utf-8') as template_file:
    CONTENTS = template_file.read()
    CONTENTS = CONTENTS.rstrip(os.linesep)
    CONTENTS = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
        contents=CONTENTS, splitter="=" * 64, sep=os.linesep)
    CONTENTS = termcolor.colored(CONTENTS, 'green')
    CONTENTS = string.Template(CONTENTS)
print(CONTENTS.substitute({'robot_name': ROBOT_NAME, 'user_name': USER_NAME}))
