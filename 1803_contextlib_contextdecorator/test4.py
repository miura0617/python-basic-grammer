import contextlib


# # 上記コードは読解しにくいので、contextlibで以下のように書ける
# @contextlib.contextmanager
# def tag(name):
#     print('<{}>'.format(name))
#     yield
#     print('</{}>'.format(name))

class tag(contextlib.ContextDecorator):
    def __init__(self, name):
        self.name = name
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)

    # クラスが作られた後に入ってくる __enter__関数
    def __enter__(self):
        print(self.start_tag)

    # クラスの最後に入ってくる __exit__関数
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print(self.end_tag)

# 関数に対してデコレーターをつけなくても、withステートメントとしても使える
with tag('h2'):
    raise Exception('error')
    print('test')
