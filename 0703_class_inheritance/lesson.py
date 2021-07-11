class Car(object):
    def run(self):
        print('run')

# Carが持っている機能を引き継いで、ToyotaCarが機能追加する
class ToyotaCar(Car):
    pass

car = Car()
car.run()

toyota_car = ToyotaCar()    # ToyotaCarクラス内はpassでrun()メソッドを持たないが、Carクラスを引き継いでいるので使える
toyota_car.run()
