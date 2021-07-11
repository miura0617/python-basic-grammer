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

# 関数に対してデコレーターをつけている
@tag('h2')
def f(content):
    print(content)

f('test')
