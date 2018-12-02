import datetime

now = datetime.datetime.now()
print(now) # 現在の時間を表示
print(now.isoformat()) # 標準時間で表示
print(now.strftime('%d/%m/%y-%H:%M:%S.%f')) # 自分なりにカスタマイズして表示

today = datetime.date.today()
print(today) # 年月日だけ表示
print(today.isoformat()) # 国際標準規格で表示
print(today.strftime('%d/%m/%y')) # カスタマイズして表示

t = datetime.time(hour=1, minute=10, second=5, microsecond=100) # 自分で時間を指定できる
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))

print(now)
dw = datetime.timedelta(weeks=1) # 1週間分をdwに代入. のちに現在の時間ら足し算・引き算を行うため.
dd = datetime.timedelta(days=1)
dh = datetime.timedelta(hours=1)
dm = datetime.timedelta(minutes=1)
ds = datetime.timedelta(seconds=1)
dms = datetime.timedelta(microseconds=1)
print(now - dd - dh - dm - ds - dms)

import time
print('###')
time.sleep(2) # 2秒後に以下が発生
print('###')
print(time.time()) # 1970年0:0:0.0から現在までの時刻を秒で表示



# time関数の使い所の1つはファイルのバックアップの時のファイル名に使える
import os
import shutil

file_name = 'test.md'

if os.path.exists(file_name):
    shutil.copy(file_name, '{}.{}'.format(file_name, now.strftime('%Y_%m_%d_%H_%M_%S'))) # ファイルのバックアップが日付と共に作られる

with open(file_name, 'w') as f:
    f.write('test')
