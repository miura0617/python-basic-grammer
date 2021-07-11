print('hello')
print("hello")

print("I don't know")

# I don'までが文字列と認識され、それ以降は'が足りないので文字列として認識されずにエラーとなる
# print('I don't know')
# \で解決できる
print('I don\'t know')

print('say "I don\'t know"')
# "の数が合わず、認識できない
# print("say "I don\'t know"")
# \で解決できる
print("say \"I don't know\"")

# \nで改行できる
print('hello. How are you?')
print('hello. \nHow are you?')

# ファイルパス中の\nが改行とみなされてしまう
print('C:\name\name')
# 解決策として、raw文字列として指定する
print(r'C:\name\name')

# 複数行をPrintする場合
# ただし最初と最後に空白行が入る
print("####################")
print("""
line1
line2
line3
""")
print("####################")

# 空白行を入れない方法
# \を入れると、次の行から始めてくださいという指示になる
print("####################")
print("""\
line1
line2
line3\
""")
print("####################")

# 文字列の繰り返し
print('Hi,' * 3 + 'Mike')

# 文字列の見やすさ
s = ('aaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

# 文字列のインデックス
word = 'python'
print(word[0])
print(word[1])
print(word[-1])
# 文字列のスライス
print(word[0:2])
print(word[2:5])
print(word[:2]) # 省略可能
print(word[2:]) # 省略可能

# python を jython に置き換える
# word[0] = 'j' # これはできない
word = 'j' + word[1:]
print(word)

# 長さを求める
print(len(word))
