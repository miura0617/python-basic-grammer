class Car(object):
    def run(self):
        print('run')

# Carが持っている機能を引き継いで、ToyotaCarが機能追加する
class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print('#######################')
toyota_car = ToyotaCar()    # ToyotaCarクラス内はpassでrun()メソッドを持たないが、Carクラスを引き継いでいるので使える
toyota_car.run()

print('#######################')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()
