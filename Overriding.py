class Car:
    def __init__(self):
        self.value='Need for Speed'
    def Show(self):
        print(self.value)
class Ford(Car):
    def __init__(self):
        self.value='300 Km/h'
    def Show(self):
        print(self.value)
o1=Car()
o2=Ford()

o1.Show()
o2.Show()
        
        

