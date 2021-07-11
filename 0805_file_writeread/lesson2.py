s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'w+') as f: # 書き込み＋読み込み
    print(f.read())               # w+で開いた瞬間、新しいtext.txtができるので空ファイルである
    #f.write(s)                   # これないと書き出し直後はEOFを指す
    #f.seek(0)                    # seek(0)で位置を戻す



