class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

# Carが持っている機能を引き継いで、ToyotaCarが機能追加する
class ToyotaCar(Car):
    def run(self):     # 継承元のCarクラスのrunメソッドをオーバーライド
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)    # super()は親クラスCarを指し、その__init__関数を呼び出す
        self.enable_auto_run = enable_auto_run
    def run(self):     # 継承元のCarクラスのrunメソッドをオーバーライド
        print('super fast')
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print('#######################')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()

print('#######################')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()
