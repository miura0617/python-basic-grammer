class Person(object):
    def talk(self):
        print('talk')
    
    def run(self):
        print('person run')
    
class Car(object):
    def run(self):
        print('car run')

class PersonCarRobot(Person, Car):  # 多重継承
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()  # 多重継承した順が早いPersonクラスのrunメソッドが呼ばれる
person_car_robot.fly()

