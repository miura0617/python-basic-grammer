class Person(object):   # objectはpython2.xの名残りで残しておいた方がいい
    # コンストラクタ
    def __init__(self, name):
        self.name = name     # selfで自分自身に変数を保持する

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)       # 同じクラスのメソッドを呼び出せる
    
    def run(self, num):
        print('run' * num)

    # デストラクタ
    def __del__(self):     # オブジェクトが使われなくなったときに実行される
        print('Good Bye')

person = Person('Mike')
person.say_something()

# del person

print('#############')

