class Car:
    def Speed(self):
        pass
class Ford(Car):
    def Speed(self):
        print('300 km/h')
class Bugatti(Car):
    def Speed(self):
        print('400 km/h')
f=Ford()
f.Speed()

b=Bugatti()
b.Speed()
