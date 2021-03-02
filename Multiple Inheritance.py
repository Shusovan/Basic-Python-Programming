class One:
    def Add(self,a,b):
        return a+b
class Two:
    def Sub(self,a,b):
        return a*b
class Three(One,Two):
    def Divide(self,a,b):
        return a/b
d=Three()
print(d.Add(10,20))
print(d.Sub(10,20))
print(d.Divide(10,20))
    
        

