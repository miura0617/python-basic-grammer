# outer関数をエンクロージャー、inner関数をクロージャーという
def outer(a, b):
    def inner():
        return a + b
    
    return inner

print(outer(1, 2))


f = outer(1, 2)
print('### 何らかの処理 ###')
print('### 何らかの処理 ###')
print('### 何らかの処理 ###')
print('### 何らかの処理 ###')
r = f()   # 代入した1, 2を気にせず、最後にf関数のみ実行したいときに使われる
print(r)

