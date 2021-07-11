def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')                    # add_num関数の前後でやりたい処理を追加（デコレーション）できる
        result = func(*args, **kwargs)
        print('end')                      # add_num関数の前後でやりたい処理を追加（デコレーション）できる
        return result
    return wrapper

# デコレーターprint_infoを宣言
@print_info
def add_num(a, b):
    return a + b

r = add_num(a, b)  # デコレータが返しているwrapper関数を呼び出すことになる
print(r)

# print('start')
# r = add_num(10, 20)
# print('end')
