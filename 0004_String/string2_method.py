s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My') # 'My'という文字列から始まっているか調べるメソッド
print(is_start)

is_start = s.startswith('X')  # 'X'という文字列から始まっているか調べるメソッド
print(is_start)

print('#########################')

print(s.find('Mike'))         # 文字列sの前から見て、指定した文字列の先頭文字のインデックスを返す
print(s.rfind('Mike'))        # 文字列sの後ろから見て、指定した文字列の先頭文字のインデックスを返す
print(s.count('Mike'))        # 文字列sの中に、指定した文字列が何個入っているか返す
print(s.capitalize())         # 先頭の文字を大文字、それ以外を小文字に変換する
print(s.title())              # 各ワードの先頭文字を、すべて大文字にする
print(s.upper())              # すべての文字を大文字にする
print(s.lower())              # すべての文字を小文字にする
print(s.replace('Mike', 'Nancy'))   # 文字列の置換


