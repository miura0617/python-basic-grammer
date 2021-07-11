s = """\
AAA
BBB
CCC
DDD
"""

with open('test2.txt', 'r+') as f: # 存在しないファイルをrモードで開く
    print(f.read())
    f.seek(0)
    f.write(s)

