import re


# 文字列の操作
s = 'My name is ... Mike'
print(s.split())        # 文字列のsplitメソッド

p = re.compile(r'\W+')  # 正規表現\Wで英数字意外でマッチ
print(p.split(s))


# 文字列の置換
p = re.compile(r'(blue|white|red)')
print(p.sub('color', 'blue socks and red shoes'))   # subは置換の意味
print(p.sub('color', 'blue socks and red shoes', count=1))   # 何個置き換えるか指定できる
print(p.subn('color', 'blue socks and red shoes'))  # 何個置き換えたか知ることができる



def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d')
print(p.sub(hexrepl, '12345 55 11 test test2'))
