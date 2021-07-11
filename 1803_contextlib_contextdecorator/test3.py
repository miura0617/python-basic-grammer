import contextlib


# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print('<{}>'.format(name))
#             r = f(content)
#             print('</{}>'.format(name))
#             return r
#         return _wrapper
#     return _tag
# 
# # デコレーターにデフォルト引数を渡すときの書き方
# @tag('h2')
# def f(content):
#     print(content)
# 
# # f = tag(f)
# 
# f('test')

# 上記コードは読解しにくいので、contextlibで以下のように書ける
@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield
    print('</{}>'.format(name))


def f():
    print('test0')
    # 関数に対してデコレーターをつけなくても、withステートメントとしても使える
    with tag('h2'):
        print('test')
        # ネストすることもできる
        with tag('h5'):
            print('test2')

f()