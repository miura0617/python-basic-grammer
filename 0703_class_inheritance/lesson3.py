class Car(object):
    def run(self):
        print('run')

# 継承しない場合、runメソッドが大量に発生し、コード量がましてしまう
class ToyotaCar(object):
    def run(self):
        print('run')   

class TeslaCar(object):
    def run(self):
        print('run')

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
