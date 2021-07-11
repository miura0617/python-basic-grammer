import re
"""
match()     文字列の先頭で正規表現とマッチするか判定
search()    文字列を操作して、正規表現がどこにマッチするか調べる
findall()   正規表現にマッチする部分文字列を全て探しだしリストとして返す
finditer()  重複しないマッチオブジェクトのイテレータを返す
"""


m = re.match('a.c', 'abc')  # matchは文字列の先頭文字から判定する
print(m)
print(m.group())

print('##############')

m = re.search('a.c', 'test abc test')   # searchは文字列内を探索するので、文字列の途中にマッチする文字列があってもよい
print(m)
print(m.span())
print(m.group())
m = re.search('a.c', 'test abc test abc')   # 2つ目のabcは抽出されない
print(m.group())

print('##############')

m = re.findall('a.c', 'test abc test abc')  # 2つ目のabcも抽出される
print(m)

print('##############')

m = re.finditer('a.c', 'test abc test abc')
print(m)        # mはイテレータオブジェクトが返ってくる
print([w.group() for w in m])
