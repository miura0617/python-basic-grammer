import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())

# 自分の表示形式でも表示できる
print(now.strftime('%d/%m/%y-%H%M%S%f'))
print('###########################')
# 年月日のみ扱う
today = datetime.date.today()
print(today)
print(today.isoformat)
print(today.strftime('%d/%m/%y'))
print('###########################')

# 時間だけを扱い、かつ自分で時間を作れる
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))
print('###########################')

# 去年を調べたいとき、datetime.timedeltaを使う
print(now)
d = datetime.timedelta(weeks=1) # 1週間前
d = datetime.timedelta(days=365)
#d = datetime.timedelta(hours=1)
#d = datetime.timedelta(minutes=1)
#d = datetime.timedelta(seconds=1)
#d = datetime.timedelta(microseconds=1)
print(now - d)

import time

print('###')
time.sleep(2)
print('###')
print(time.time()) # エポックタイムで表示。1970年1月1日からの経過した秒数


import os
import shutil

file_name = 'test.txt'

# ファイルのバックアップ
if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(\
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))

# 上記でバックアップ作成後、ファイルを書き換える
with open(file_name, 'w') as f:
    f.write('test')

