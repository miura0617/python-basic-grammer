import re
"""
match()     文字列の先頭で正規表現とマッチするか判定
search()    文字列を操作して、正規表現がどこにマッチするか調べる
findall()   正規表現にマッチする部分文字列を全て探しだしリストとして返す
finditer()  重複しないマッチオブジェクトのイテレータを返す
"""


m = re.match('ab?', 'a')    # ?はひとつ前の文字が0または1回を指す
print(m)
m = re.match('ab?', 'ab')
print(m)
m = re.match('ab?', 'abb')  # abにはヒットするが、abb全体にはヒットしない
print(m)

print('###########')

m = re.match('ab*', 'abb')  # *は0回以上の繰り返しを指す
print(m)

print('###########')

m = re.match('ab+', 'a')    # +は1回以上の繰り返しを指す
print(m)
m = re.match('ab+', 'ab')   # +は1回以上の繰り返しを指す
print(m)

print('###########')

m = re.match('a{3}', 'a')   # {3}は回数指定できる
print(m)
m = re.match('a{3}', 'aa')  # {3}は回数指定できる
print(m)
m = re.match('a{3}', 'aaa') # {3}は回数指定できる
print(m)

m = re.match('a{2, 4}', 'a')        # {2, 3}は2～4つと指定できる
print(m)
m = re.match('a{2, 4}', 'aa')       # {2, 3}は2～4つと指定できる
print(m)
m = re.match('a{2, 4}', 'aaaaa')    # {2, 3}は2～4つと指定できる
print(m)

print('###########')

m = re.match('[a-c]', 'a')          # アルファベットa～cの間の文字を指定
print(m)
m = re.match('[a-c]', 'x')          
print(m)
m = re.match('[a-z]', 'x')          
print(m)
m = re.match('[a-zA-Z]', 'Y')       
print(m)
m = re.match('[a-zA-Z0-9]', '1')    
print(m)
m = re.match('[a-zA-Z0-9]', '_')    
print(m)
m = re.match('[a-zA-Z0-9_]', '_')   
print(m)

m = re.match('\w', '_')             # \wは任意の英数文字と_(アンダースコア)を意味するので、上のコードを省略して書ける
print(m)
m = re.match('\w', '@')             # \wは任意の英数文字と_(アンダースコア)を意味するので、上のコードを省略して書ける
print(m)

m = re.match('\W', '@')             # \W（大文字）は任意の英数文字と_(アンダースコア)意外を指定したい場合
print(m)
m = re.match('\W', 'a')             # \W（大文字）は任意の英数文字と_(アンダースコア)意外を指定したい場合
print(m)
m = re.match('[^a-zA-Z0-9_]', '@')  # ^をつけると、\W（大文字）と同じ意味になる   
print(m)
m = re.match('[^a-zA-Z0-9_]', 'a')  # ^をつけると、\W（大文字）と同じ意味になる   
print(m)

print('###########')

m = re.match('[0-9]', '1') 
print(m)
m = re.match('\d', '1')             # 0-9を\dで置き換えられる
print(m)
m = re.match('\d', 'a')            
print(m)
m = re.match('\D', '1')             # \Dで0-9意外とできる            
print(m)
m = re.match('\D', 'a')            
print(m)

print('###########')

m = re.match('[a|b]', 'a')          # a|bはaまたはbを指す            
print(m)
m = re.match('[a|b]', 'x')            
print(m)
m = re.match('(abc)+', 'abc')            
print(m)
m = re.match('(abc)+', 'abcabc')            
print(m)
m = re.match('\s', ' ')             # \sは半角スペースとマッチするか       
print(m)
m = re.match('\s', '')              # \sは半角スペースとマッチするか       
print(m)
m = re.match('\s', '1')             # \sは半角スペースとマッチするか       
print(m)
m = re.match('\S', ' ')             # \Sは半角スペース意外ならマッチ       
print(m)
m = re.match('\S', '')              # \Sは半角スペース意外ならマッチ       
print(m)
m = re.match('\S', '1')             # \Sは半角スペース意外ならマッチ       
print(m)

print('###########')

m = re.match('\*', '*')             # \*は正規表現で予約文字になっている*（アスタリスク）を判定したいとき       
print(m)
m = re.match('\?', '?')                    
print(m)

print('###########')

m = re.search('^abc', 'test abc')   # ^を使って、re.search（）で先頭文字の始まりをマッチしているか確認する
print(m)
m = re.search('^abc', 'abctest abc')
print(m)

m = re.search('abc$', 'abctest abc')    # $は文字列の最後が指定した文字列か確認する
print(m)
m = re.search('abc$', 'abctest abctest')   # $は文字列の最後が指定した文字列か確認する
print(m)