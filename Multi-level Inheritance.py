class Car:
    def Sports_Car(self):
        print('Racing Cars')
class Bugatti(Car):
    def Power(self):
        print('1200 HP')
class Bugatti_Chiron(Bugatti):
    def Speed(self):
        print('Top Speed 400 km/h')
b=Bugatti_Chiron()
b.Power()
b.Speed() 
b.Sports_Car()       
